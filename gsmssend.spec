%define 	name	gsmssend
%define 	version	1.1
%define 	release	1
%define 	serial	1
%define 	prefix	/usr

Summary: 	GNOME user interface for SmsSend
Name:		%{name}
Version:	%{version}
Release:	%{release}
Serial:		%{serial}
Copyright:	GPL
Group:		Applications/Internet
Url:		http://lassauge.free.fr/linux.html
Vendor:		Eric Lassauge <lassauge@mail.dotcom.fr>
Source:		http://lassauge.free.fr/smssend/%{name}-%{version}.tar.gz
Packager:	Eric Lassauge <lassauge@mail.dotcom.fr>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk+ >= 1.2.8 SmsSend 2.1

%description
GNOME-SmsSend is a gnome UI to the smssend tools written by
Christophe CALMEJANE 'Ze KiLleR / SkyTech'
http://zekiller.skytech.org/smssend_menu_en.html

It will detect the provider script files in the default locations
(current dir, ~/.smssend, and smssend default global) and create a small UI
for each one. When you click on the APPLY button it will fork/exec
smssend with proper options.
All options to smssend can be set through the preference dialog.


%prep
%setup -q
CFLAGS=$RPM_OPT_FLAGS \
	./configure --prefix=%{prefix}

%build
make

%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
make -e prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README NEWS TODO
%{prefix}/bin/gsmssend
%{prefix}/share/gnome/apps/Internet/gsmssend.desktop
%{prefix}/share/pixmaps/gnome-smssend.png
%{prefix}/share/pixmaps/gsmssend
%{prefix}/man/*/gsmssend.*
%{prefix}/share/locale/*/LC_MESSAGES/gsmssend.mo
