%define name xvid
%define version 1.3.2
%define fname xvidcore-%{version}

%define major 4
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary: Video codec compatible with divx4
Name: %{name}
Version: %{version}
Release: %mkrel 1
Source0: http://downloads.xvid.org/downloads/%fname.tar.bz2
License: GPLv2+
Group: System/Libraries
URL: http://www.xvid.org
BuildRoot: %{_tmppath}/%{name}-buildroot
Epoch: 2
BuildRequires: yasm

%description
This is a video codec based on the original OpenDivX codec. It's
compatible with DivX and MPEG 4.

%package -n %libname
Group: System/Libraries
Summary: Video codec compatible with divx4
Provides: lib%{name} = %{version}-%{release}
Obsoletes: %{name}
Provides: %{name}

%description -n %libname 
This is a video codec based on the original OpenDivX codec. It's
compatible with DivX and MPEG 4.

%package -n %develname
Group:Development/C
Summary: Video codec compatible with divx4, devel files
Requires: %{libname} = %{epoch}:%{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{name}-devel %{mklibname -d %{name} 4}
Conflicts: xvid2-devel
Provides: lib%{name}-devel = %{version}-%{release}
Provides: xvid4-devel = %{version}-%{release}

%description -n %develname
This is a video codec based on the original OpenDivX codec. It's
compatible with DivX and MPEG 4.

This package contains the header files and static libraries needed to
build programs with the xvid codec using it's native API.

%prep
%setup -q -n xvidcore

%build
cd build/generic
%configure2_5x
%make

%install
rm -rf %{buildroot}
cd build/generic
%makeinstall
ln -s libxvidcore.so.%{major} %{buildroot}%{_libdir}/libxvidcore.so

%clean
rm -rf %{buildroot}

%if %mdvver < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname 
%defattr(-,root,root)
%doc LICENSE README
%_libdir/libxvidcore.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog CodingStyle TODO AUTHORS
%{_libdir}/libxvidcore.so
%{_libdir}/libxvidcore.a
%{_includedir}/xvid.h

