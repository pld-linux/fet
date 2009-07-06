# TODO:
#	- optflags
#	- fet doesn't respect locale settings
#
Summary:	FET is open source free software for automatically scheduling the timetable
Summary(hu.UTF-8):	FET egy nyílt forrású órarend-készítő program
Summary(pl.UTF-8):	Narzędzie do automatycznego układania planów dla szkół i uczelni
Name:		fet
Version:	5.10.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.lalescu.ro/liviu/fet/download/%{name}-%{version}.tar.bz2
# Source0-md5:	e6d32699bd61c02b8ed5ef2677a091e8
URL:		http://www.lalescu.ro/liviu/fet
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FET is open source free software for automatically scheduling the
timetable of a school, high-school or university. It uses a fast and
efficient timetabling algorithm.

%description -l hu.UTF-8
FET egy nyílt forrású szoftver, amely általános iskolák, középiskolák,
egyetemek órarendjét (időbeosztását) készíti el. Egy gyors és hatékony
algoritmust használ.

%description -l pl.UTF-8
FET jest oprogramowaniem o otwartych źródłach służącym do
automatycznego układania planów zajęć szkół i uczelni. Program ten
używa szybkiego i efektywnego algorytmu układającego harmonogramy.

%package examples
Summary:	Sample inputs to FET
Summary(hu.UTF-8):	Példafájlok FET-hez
Summary(pl.UTF-8):	Przykładowe pliki wejściowe dla programu FET
Group:		X11/Applications

%description examples
Sample input files to FET from all the world.

%description examples -l hu.UTF-8
Példafájlok FET-hez a világ minden tájáról.

%description examples -l pl.UTF-8
Przykładowe pliki wejściowe dla programu FET.

%package doc
Summary:	FET documentation by Volker Dirr
Summary(hu.UTF-8):	FET dokumentáció Volker Dirr "szerkesztésében"
Summary(pl.UTF-8):	Dokumentacja do programu FET autorstwa Volkera Dirra
Group:		X11/Applications

%description doc
FET documentation by Volker Dirr.

%description doc -l hu.UTF-8
FET dokumentáció Volker Dirr tollából.

%description doc -l pl.UTF-8
Dokumentacja do programu FET autorstwa Volkera Dirra.

%prep
%setup -q

%build
qmake-qt4 fet.pro \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}/translations}

install fet $RPM_BUILD_ROOT%{_bindir}
install doc/fet.1 $RPM_BUILD_ROOT%{_mandir}/man1
install translations/fet_*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__cp} -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/translations/fet_untranslated.qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CONTRIBUTORS GUESTBOOK LINKS README REFERENCES SPONSORS THANKS TODO TRANSLATORS doc/*/*
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%lang(ar) %{_datadir}/%{name}/translations/fet_ar.qm
%lang(ca) %{_datadir}/%{name}/translations/fet_ca.qm
%lang(de) %{_datadir}/%{name}/translations/fet_de.qm
%lang(fa) %{_datadir}/%{name}/translations/fet_fa.qm
%lang(el) %{_datadir}/%{name}/translations/fet_el.qm
%lang(es) %{_datadir}/%{name}/translations/fet_es.qm
%lang(fr) %{_datadir}/%{name}/translations/fet_fr.qm
%lang(hu) %{_datadir}/%{name}/translations/fet_hu.qm
%lang(id) %{_datadir}/%{name}/translations/fet_id.qm
%lang(it) %{_datadir}/%{name}/translations/fet_it.qm
%lang(lt) %{_datadir}/%{name}/translations/fet_lt.qm
%lang(mk) %{_datadir}/%{name}/translations/fet_mk.qm
%lang(ms) %{_datadir}/%{name}/translations/fet_ms.qm
%lang(nl) %{_datadir}/%{name}/translations/fet_nl.qm
%lang(pl) %{_datadir}/%{name}/translations/fet_pl.qm
%lang(ro) %{_datadir}/%{name}/translations/fet_ro.qm
%lang(ru) %{_datadir}/%{name}/translations/fet_ru.qm
%lang(tr) %{_datadir}/%{name}/translations/fet_tr.qm
%{_mandir}/man1/fet.1*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
