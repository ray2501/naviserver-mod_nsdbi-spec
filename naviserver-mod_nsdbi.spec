#
# spec file for package naviserver nsdbi module
#

Summary:        NaviServer nsdbi module
Name:           naviserver-mod_nsdbi
Version:        0.4
Release:        0
License:        MPL-1.1
Group:          Productivity/Networking/Web/Servers
Url:            http://bitbucket.org/naviserver/nsdbi
BuildRequires:  make
BuildRequires:  naviserver
BuildRequires:  naviserver-devel
Requires:       naviserver
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The nsdbi module is a shared library for the naviserver web server which
supports loadable database drivers.

%package devel
Summary:        Header Files for NaviServer nsdbi module
Group:          Productivity/Networking/Web/Servers
Requires:       naviserver-mod_nsdbi

%description devel
This package contains header files for NaviServer nsdbi module.

%prep
%setup -q %{name}-%{version}

%build
make NAVISERVER=/var/lib/naviserver

%install
mkdir -p %buildroot/var/lib/naviserver/bin
mkdir -p %buildroot/var/lib/naviserver/lib
mkdir -p %buildroot/var/lib/naviserver/include
make DESTDIR=%buildroot install NAVISERVER=/var/lib/naviserver

%clean
rm -rf %buildroot

%post -n naviserver-mod_nsdbi
/sbin/ldconfig

%postun -n naviserver-mod_nsdbi
/sbin/ldconfig

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/tcl/nsdbi
/var/lib/naviserver/lib/libnsdbi.so
/var/lib/naviserver/bin/nsdbitest.so

%files devel
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/include/nsdbi.h
/var/lib/naviserver/include/nsdbidrv.h

%changelog

