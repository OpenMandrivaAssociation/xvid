%define fname xvidcore-%{version}

%define major 4
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Video codec compatible with divx4
Name:		xvid
Version:	1.3.4
Release:	1
Source0:	http://downloads.xvid.org/downloads/%fname.tar.bz2
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.xvid.org
Epoch:		2
BuildRequires:	yasm

%description
This is a video codec based on the original OpenDivX codec. It's
compatible with DivX and MPEG 4.

%package -n %{libname}
Group:		System/Libraries
Summary:	Video codec compatible with divx4
Provides:	lib%{name} = %{version}-%{release}
Obsoletes:	%{name} < %{version}-%{release}
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This is a video codec based on the original OpenDivX codec. It's
compatible with DivX and MPEG 4.

%package -n %{develname}
Group:		Development/C
Summary:	Video codec compatible with divx4, devel files
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel %{mklibname -d %{name} 4}
Conflicts:	xvid2-devel
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	xvid4-devel = %{version}-%{release}

%description -n %{develname}
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
cd build/generic
%makeinstall

%files -n %{libname}
%_libdir/libxvidcore.so.%{major}*

%files -n %{develname}
%doc ChangeLog CodingStyle TODO AUTHORS LICENSE README
%{_libdir}/libxvidcore.so
%{_libdir}/libxvidcore.a
%{_includedir}/xvid.h

