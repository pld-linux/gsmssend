Summary:	GNOME user interface for SmsSend
Name:		gsmssend
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Vendor:		Eric Lassauge <lassauge@mail.dotcom.fr>
Source0:	http://lassauge.free.fr/smssend/%{name}-%{version}.tar.gz
BuildRequires:	SmsSend >= 2.1
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.8
URL:		http://lassauge.free.fr/linux.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GNOME-SmsSend is a gnome UI to the smssend tools written by Christophe
CALMEJANE 'Ze KiLleR / SkyTech'
http://zekiller.skytech.org/smssend_menu_en.html

It will detect the provider script files in the default locations
(current dir, ~/.smssend, and smssend default global) and create a
small UI for each one. When you click on the APPLY button it will
fork/exec smssend with proper options. All options to smssend can be
set through the preference dialog.

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/Network/Misc

%find_lang %{name}

gzip -9nf ChangeLog README NEWS TODO
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gsmssend
%{_applnkdir}/Network/Misc/gsmssend.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/gsmssend.*
