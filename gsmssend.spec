Summary:	GNOME user interface for SmsSend
Summary(pl):	Interfejs u¿ytkownika dla GNOME do SmsSend
Name:		gsmssend
Version:	1.1
Release:	1
License:	GPL
Vendor:		Eric Lassauge <lassauge@mail.dotcom.fr>
Group:		X11/Applications
Source0:	http://lassauge.free.fr/smssend/%{name}-%{version}.tar.gz
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

%description -l pl
GNOME-SmsSend to gnomowy interfejs u¿ytkownika do narzêdzi smssend
napisanych przez Christophe'a Calmejane'a (KiLleR/SkyTech) -
http://zekiller.skytech.org/smssend_menu_en.html .

Ten program znajduje skrypty w standardowych miejscach (aktualny
katalog, ~/.smssend, globalna konfiguracja smssend) i tworzy ma³y
interfejs u¿ytkownika do ka¿dego z nich. Po naci¶niêciu przycisku
APPLY uruchamia smssend z odpowiednimi opcjami. Wszystkie opcje
smssend mog± byæ ustawione w okienku z opcjami.

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
