# The following should match PROGRAM, VERSION and RELEASE in the
# Makefile accompanying this program (and the .tgz defined in Source
# below.
%define name wulfstat
%define version 1.0.1
%define release %mkrel 7

Summary: A beowulf/cluster/LAN monitoring tool

Name: %name
Version: %version
Release: %release
Group: Monitoring
License: GPL
Source: http://www.phy.duke.edu/~rgb/wulfware/%{name}-%{version}.tgz
Buildrequires: libwulf-devel
Buildrequires: libxml2-devel
Buildrequires: ncurses-devel 
Buildroot: %{_tmppath}/%{name}root
Url: http://www.phy.duke.edu/~rgb/Beowulf/wulfstat.php

%description 
wulfstat is a simple yet powerful tty (ncurses) based cluster monitoring
tool.  It requires xmlsysd (running on each system to be monitored) to
efficiently provide it with system and proc-derived information that is
processed and provided to the user in one of several user-selectable
display formats.  With it a user can monitor things across en entire
beowulf, cluster, or workstation LAN systems descriptors such as load
average, memory consumption, swap, page, and interrupt activity and
network loads or can even retrieve and display such mundane information
is CPU make and base clock, system time, uptime or other potentially
useful but slowly varying system descriptors.  The information presented
is updated regularly after a user-selectable delay.  The tool allows
displays to be selected or changed while the application is running, and
more hosts or nodes can be displayed than will easily fit on a single
e.g. xterm by paging through them with key-based commands.

%prep
%setup -q -n %{name}

%build
make clean
%make

%install
%make PREFIX=%{buildroot}/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
# The wulfstat binary
%attr(755,root,root) %{_bindir}/wulfstat
# The wulfstat man page
%attr(644,root,root) %{_mandir}/man1/wulfstat.1.*

# The wulfstat docs (not much here, actually)
%doc README COPYING wulfhosts.example



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-7mdv2010.0
+ Revision: 434984
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-6mdv2009.0
+ Revision: 262178
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-5mdv2009.0
+ Revision: 256469
- rebuild
- fix spacing at top of description

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.0.1-3mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix wulf-devel BR
    - kill re-definition of %%buildroot on Pixel's request


* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.1-2mdk
- Fix BuildRequires

* Fri Sep 23 2005 Erwan Velu <erwan@seanodes.com> 1.0.1-1mdk
- 1.0.1

* Tue Mar 22 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 0.6.2-2mdk
- rebuild

* Fri Aug 13 2004 Erwan Velu <erwan@mandrakesoft.com> 0.6.2-1mdk
- 0.6.2

* Wed Jun 23 2004 Erwan Velu <erwan@mandrakesoft.com> 0.6.0-1mdk
- 0.6.0

* Fri Jun 18 2004 Erwan Velu <erwan@mandrakesoft.com> 0.5.9-1mdk
- Initial release

* Mon Apr 29 2002 Robert G. Brown <rgb@duke.edu>
- Working stably for a few weeks.  Going into beta.

* Wed Mar 13 2002 Robert G. Brown <rgb@duke.edu>
- set up and built for RH 7.2

