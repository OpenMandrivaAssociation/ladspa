%define name ladspa
%define oname ladspa_sdk
%define version 1.13
%define release %mkrel 4

Summary: LADSPA SDK example plugins
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ladspa.org/download/%{oname}_%version.tgz
Source1: ladspa.sh.bz2
Source2: ladspa.csh.bz2
License: LGPLv2+
Group: Sound
URL: http://www.ladspa.org
BuildRoot: %{_tmppath}/%{name}-buildroot
#for mkdirhier
BuildRequires: imake

%description
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

This package contains the example plugins from the LADSPA SDK.

%package devel
Summary:Linux Audio Developer's Simple Plugin API
Group: Development/C
Requires: %name = %version
%description devel
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

Definitive technical documentation on LADSPA plugins for both the host
and plugin is contained within copious comments within the ladspa.h
header file.

%prep
%setup -q -n %oname
cd doc
#fix links to the header file in the docs
perl -pi -e "s!HREF=\"ladspa.h.txt\"!href=\"file:///usr/include/ladspa.h\"!" *.html


%build
cd src
%make targets

%install
rm -rf %{buildroot}
cd src
%makeinstall INSTALL_PLUGINS_DIR=%buildroot%_libdir/ladspa INSTALL_INCLUDE_DIR=%buildroot%_includedir INSTALL_BINARY_DIR=%buildroot%_bindir
install -d -m 755 %buildroot%_sysconfdir/profile.d
bzcat %SOURCE1 > %buildroot%_sysconfdir/profile.d/ladspa.sh
bzcat %SOURCE2 > %buildroot%_sysconfdir/profile.d/ladspa.csh
#gw replace lib by lib64 if needed
perl -pi -e "s!/usr/lib!%_libdir!" %buildroot%_sysconfdir/profile.d/ladspa*sh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/COPYING
%attr(644,root,root) %_sysconfdir/profile.d/ladspa*sh
%_libdir/ladspa
%_bindir/*

%files devel
%defattr(-,root,root)
%doc doc/*.html doc/COPYING
%_includedir/ladspa.h
