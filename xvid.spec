%global optflags %{optflags} -O3

%define fname xvidcore-%{version}

%define major 4
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

# xvid is used by ffmpeg, ffmpeg is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif
%define lib32name lib%{name}%{major}
%define devel32name lib%{name}-devel

Summary:	Video codec compatible with divx4
Name:		xvid
Epoch:		2
Version:	1.3.7
Release:	2
Source0:	https://downloads.xvid.com/downloads/xvidcore-%{version}.tar.bz2
License:	GPLv2+
Group:		System/Libraries
URL:		https://labs.xvid.com/source/
BuildRequires:	yasm

%description
This is a video codec based on the original OpenDivX codec. It's
compatible with DivX and MPEG 4.

%package -n %{libname}
Group:		System/Libraries
Summary:	Video codec compatible with divx4
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This is a video codec based on the original OpenDivX codec. It's
compatible with DivX and MPEG 4.

%package -n %{develname}
Group:		Development/C
Summary:	Video codec compatible with divx4, devel files
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This is a video codec based on the original OpenDivX codec. It's
compatible with DivX and MPEG 4.

This package contains the header files and static libraries needed to
build programs with the xvid codec using it's native API.

%if %{with compat32}
%package -n %{lib32name}
Group:		System/Libraries
Summary:	Video codec compatible with divx4 (32-bit)

%description -n %{lib32name}
This is a video codec based on the original OpenDivX codec. It's
compatible with DivX and MPEG 4.

%package -n %{devel32name}
Group:		Development/C
Summary:	Video codec compatible with divx4, devel files (32-bit)
Requires:	%{develname} = %{epoch}:%{version}-%{release}
Requires:	%{lib32name} = %{epoch}:%{version}-%{release}

%description -n %{devel32name}
This is a video codec based on the original OpenDivX codec. It's
compatible with DivX and MPEG 4.

This package contains the header files and static libraries needed to
build programs with the xvid codec using it's native API.
%endif

%prep
%autosetup -n xvidcore -p1

%if %{with compat32}
# Looks like autoconf, but isn't...
mkdir build32
cp -a $(ls -1 |grep -v build32) build32/
cd build32/build/generic
%configure32 --host=i686-openmandriva-linux-gnu --disable-assembly
cd ../../..
%endif

cd build/generic
%configure

%build
%if %{with compat32}
cd build32/build/generic
%make_build
cd ../../..
%endif
cd build/generic
%make_build

%install
%if %{with compat32}
cd build32/build/generic
%make_install
cd ../../..
%endif
cd build/generic
%make_install

%files -n %{libname}
%{_libdir}/libxvidcore.so.%{major}*

%files -n %{develname}
%doc ChangeLog CodingStyle TODO AUTHORS LICENSE README
%{_libdir}/libxvidcore.so
%{_libdir}/libxvidcore.a
%{_includedir}/xvid.h

%if %{with compat32}
%files -n %{lib32name}
%_prefix/lib/libxvidcore.so.%{major}*

%files -n %{devel32name}
%doc ChangeLog CodingStyle TODO AUTHORS LICENSE README
%{_prefix}/lib/libxvidcore.so
%{_prefix}/lib/libxvidcore.a
%endif
