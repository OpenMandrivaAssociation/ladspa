# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define oname ladspa_sdk

Summary:	LADSPA SDK example plugins
Name:		ladspa
Version:	1.17
Release:	1
License:	LGPLv2+
Group:		Sound
Url:		http://www.ladspa.org
Source0:	http://www.ladspa.org/download/%{oname}_%{version}.tgz
Source1:	ladspa.sh
Source2:	ladspa.csh
#for mkdirhier
BuildRequires:	imake
BuildRequires:	pkgconfig(sndfile)

%description
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

This package contains the example plugins from the LADSPA SDK.

%files
%doc doc/COPYING
%attr(644,root,root) %{_sysconfdir}/profile.d/ladspa*sh
%{_bindir}/*
%{_libdir}/ladspa


%package devel
Summary:	Linux Audio Developer's Simple Plugin API
Group:		Development/C
Requires:	%{name} = %{version}

%description devel
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

Definitive technical documentation on LADSPA plugins for both the host
and plugin is contained within copious comments within the ladspa.h
header file.

%files devel
%doc doc/*.html doc/COPYING
%{_includedir}/ladspa.h

%prep
%setup -qn %{oname}_%{version}
cd doc
#fix links to the header file in the docs
sed -i -e "s!HREF=\"ladspa.h.txt\"!href=\"file:///usr/include/ladspa.h\"!" *.html

%build
cd src
%make targets

%install
cd src
%make_install \
	INSTALL_PLUGINS_DIR=%{buildroot}%{_libdir}/ladspa \
	INSTALL_INCLUDE_DIR=%{buildroot}%{_includedir} \
	INSTALL_BINARY_DIR=%{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %SOURCE1 %{buildroot}%{_sysconfdir}/profile.d/ladspa.sh
install -m 644 %SOURCE2 %{buildroot}%{_sysconfdir}/profile.d/ladspa.csh
#gw replace lib by lib64 if needed
sed -i -e "s!/usr/lib!%{_libdir}!" %{buildroot}%{_sysconfdir}/profile.d/ladspa*sh
