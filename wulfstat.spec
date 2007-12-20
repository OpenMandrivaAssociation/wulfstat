# The following should match PROGRAM, VERSION and RELEASE in the
# Makefile accompanying this program (and the .tgz defined in Source
# below.
%define name wulfstat
%define version 1.0.1
%define release %mkrel 2

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

