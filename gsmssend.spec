Summary:	GNOME user interface for SmsSend
Summary(pl.UTF-8):   Interfejs użytkownika dla GNOME do SmsSend
Name:		gsmssend
Version:	1.1
Release:	1
License:	GPL
Vendor:		Eric Lassauge <lassauge@mail.dotcom.fr>
Group:		X11/Applications
Source0:	http://lassauge.free.fr/smssend/%{name}-%{version}.tar.gz
# Source0-md5:	fd58dca0b7d89e37fbda41d4a4d09e81
URL:		http://lassauge.free.fr/linux.html
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	smssend >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GNOME-SmsSend is a gnome UI to the smssend tools written by Christophe
CALMEJANE 'Ze KiLleR / SkyTech'
http://zekiller.skytech.org/smssend_menu_en.html .

It will detect the provider script files in the default locations
(current dir, ~/.smssend, and smssend default global) and create a
small UI for each one. When you click on the APPLY button it will
fork/exec smssend with proper options. All options to smssend can be
set through the preference dialog.

%description -l pl.UTF-8
GNOME-SmsSend to gnomowy interfejs użytkownika do narzędzi smssend
napisanych przez Christophe'a Calmejane'a (KiLleR/SkyTech) -
http://zekiller.skytech.org/smssend_menu_en.html .

Ten program znajduje skrypty w standardowych miejscach (aktualny
katalog, ~/.smssend, globalna konfiguracja smssend) i tworzy mały
interfejs użytkownika do każdego z nich. Po naciśnięciu przycisku
APPLY uruchamia smssend z odpowiednimi opcjami. Wszystkie opcje
smssend mogą być ustawione w okienku z opcjami.

%prep
%setup -q

%build
%{__gettextize}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/Network/Misc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README NEWS TODO
%attr(755,root,root) %{_bindir}/gsmssend
%{_applnkdir}/Network/Misc/gsmssend.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/gsmssend.*
