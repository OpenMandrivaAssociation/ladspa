%define debug_package          %{nil}

%define name ladspa
%define oname ladspa_sdk
%define version 1.13
%define release %mkrel 5

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
rm -rf $RPM_BUILD_ROOT
cd src
%makeinstall INSTALL_PLUGINS_DIR=%buildroot%_libdir/ladspa INSTALL_INCLUDE_DIR=%buildroot%_includedir INSTALL_BINARY_DIR=%buildroot%_bindir
install -d -m 755 %buildroot%_sysconfdir/profile.d
bzcat %SOURCE1 > %buildroot%_sysconfdir/profile.d/ladspa.sh
bzcat %SOURCE2 > %buildroot%_sysconfdir/profile.d/ladspa.csh
#gw replace lib by lib64 if needed
perl -pi -e "s!/usr/lib!%_libdir!" %buildroot%_sysconfdir/profile.d/ladspa*sh

%clean
rm -rf $RPM_BUILD_ROOT

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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.13-4mdv2011.0
+ Revision: 666057
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.13-3mdv2011.0
+ Revision: 606395
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.13-2mdv2010.1
+ Revision: 521147
- rebuilt for 2010.1

* Fri Apr 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.13-1mdv2010.0
+ Revision: 368980
- new version
- drop patch
- fix license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.12-14mdv2009.0
+ Revision: 222015
- rebuild
- fix spacing at top of description

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.12-13mdv2008.1
+ Revision: 150437
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Jul 15 2007 Adam Williamson <awilliamson@mandriva.org> 1.12-12mdv2008.0
+ Revision: 52291
- rebuild for 2008

* Sun Jul 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.12-11mdv2008.0
+ Revision: 46428
- Import ladspa




* Fri Jun 30 2006 Götz Waschk <waschk@mandriva.org> 1.12-11mdv2007.0
- fix permissions of the profile.d scripts
- fix buildrequires

* Wed Jun  7 2006 Götz Waschk <waschk@mandriva.org> 1.12-10mdv2007.0
- fix rpmlint warnings about the profile.d-scripts
- fix build

* Sun Apr 30 2006 Stefan van der Eijk <stefan@eijk.nu> 1.12-9mdk
- rebuild for sparc

* Mon Jun 06 2005 Götz Waschk <waschk@mandriva.org> 1.12-8mdk
- Rebuild

* Fri Jun  4 2004 Götz Waschk <waschk@linux-mandrake.com> 1.12-7mdk
- add source URL
- drop prefix
- new g++

* Tue Jan 13 2004 Götz Waschk <waschk@linux-mandrake.com> 1.12-6mdk
- add scripts for setting the LADSPA_PATH variable (Daniel Lyddy)

* Mon Apr 28 2003 Götz Waschk <waschk@linux-mandrake.com> 1.12-5mdk
- fix distriblint warning

* Tue Apr  8 2003 Götz Waschk <waschk@linux-mandrake.com> 1.12-4mdk
- fix buildrequires

* Fri Dec 27 2002 Götz Waschk <waschk@linux-mandrake.com> 1.12-3mdk
- use versioned tarball
- new version

* Thu Aug 15 2002 Laurent Culioli <laurent@pschit.net> 1.12-2mdk
- Rebuild with gcc3.2

* Mon Aug 12 2002 Götz Waschk <waschk@linux-mandrake.com> 1.12-1mdk
- new version

* Mon Jul 29 2002 Götz Waschk <waschk@linux-mandrake.com> 1.11-3mdk
- gcc 3.2 build

* Tue May 28 2002 Götz Waschk <waschk@linux-mandrake.com> 1.11-2mdk
- gcc 3.1

* Thu Mar 21 2002 Götz Waschk <waschk@linux-mandrake.com> 1.11-1mdk
- initial package
