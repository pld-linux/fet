# TODO:
#	- fet doesn't respect locale settings
#
Summary:	FET is open source free software for automatically scheduling the timetable
Summary(hu.UTF-8):	FET egy nyílt forrású órarend-készítő program
Summary(pl.UTF-8):	Narzędzie do automatycznego układania planów dla szkół i uczelni
Name:		fet
Version:	5.17.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.lalescu.ro/liviu/fet/download/%{name}-%{version}.tar.bz2
# Source0-md5:	8e136dc5f764a27322f072804ff89aea
Source1:	http://www.lalescu.ro/liviu/fet/doc/en/faq.html
# Source1-md5:	7029338b802b65b42d7c2e2696bbbf27
Source2:	http://www.lalescu.ro/liviu/fet/doc/en/instructions.html
# Source2-md5:	68ffbb297e609ea26526b288c6e2369c
Source3:	http://www.lalescu.ro/liviu/fet/doc/en/tips.html
# Source3-md5:	d2a0a061f224d3c7ab96f7a3257a3b35
Source4:	%{name}.desktop
Source5:	%{name}.png
URL:		http://www.lalescu.ro/liviu/fet
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
Obsoletes:	fet-doc
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
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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

%package lang-ar
Summary:	ar translation to fet
Summary(hu.UTF-8):	ar fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-ar
ar translation to fet.

%package lang-ca
Summary:	Catalan translation to fet
Summary(hu.UTF-8):	Katalán fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-ca
Catalan translation to fet.

%package lang-da
Summary:	Danish translation to fet
Summary(hu.UTF-8):	Dán fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-da
Danish translation to fet.

%package lang-de
Summary:	German translation to fet
Summary(hu.UTF-8):	Német fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-de
German translation to fet.

%package lang-el
Summary:	Greek translation to fet
Summary(hu.UTF-8):	Görög fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-el
Greek translation to fet.

%package lang-es
Summary:	Spanish translation to fet
Summary(hu.UTF-8):	Spanyol fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-es
Spanish translation to fet.

%package lang-fa
Summary:	fa translation to fet
Summary(hu.UTF-8):	fa fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-fa
fa translation to fet.

%package lang-fr
Summary:	French translation to fet
Summary(hu.UTF-8):	Francia fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-fr
French translation to fet.

%package lang-he
Summary:	Hebrew translation to fet
Summary(hu.UTF-8):	Héber fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif
%description lang-he
Hebrew translation to fet.

%package lang-hu
Summary:	Hungarian translation to fet
Summary(hu.UTF-8):	Magyar fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-hu
Hungarian translation to fet.

%description lang-hu -l hu.UTF-8
Magyar fordítás fet-hez.

%package lang-id
Summary:	id translation to fet
Summary(hu.UTF-8):	id fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-id
id translation to fet.

%package lang-it
Summary:	Italian translation to fet
Summary(hu.UTF-8):	Olasz fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-it
Italian translation to fet.

%package lang-lt
Summary:	Lithuanian translation to fet
Summary(hu.UTF-8):	Litván fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-lt
Lithuanian translation to fet.

%package lang-mk
Summary:	mk translation to fet
Summary(hu.UTF-8):	mk fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-mk
mk translation to fet.

%package lang-ms
Summary:	ms translation to fet
Summary(hu.UTF-8):	ms fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-ms
ms translation to fet.

%package lang-nl
Summary:	nl translation to fet
Summary(hu.UTF-8):	nl fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-nl
nl translation to fet.

%package lang-pl
Summary:	Polish translation to fet
Summary(hu.UTF-8):	Lengyel fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-pl
Polish translation to fet.

%package lang-ro
Summary:	Romanian translation to fet
Summary(hu.UTF-8):	Román fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-ro
Romanian translation to fet.

%package lang-pt
Summary:	Portugese translation to fet
Summary(hu.UTF-8):	Portugal fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-pt
Portugese translation to fet.

%package lang-ru
Summary:	Russian translation to fet
Summary(hu.UTF-8):	Orosz fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-ru
Russian translation to fet.

%package lang-si
Summary:	Sinhala translation to fet
Summary(hu.UTF-8):	Sinhala fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-si
Sinhala translation to fet.

%package lang-sk
Summary:	Slovak translation to fet
Summary(hu.UTF-8):	Szlovák fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-sk
Slovak translation to fet.

%package lang-tr
Summary:	tr translation to fet
Summary(hu.UTF-8):	tr fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-tr
tr translation to fet.

%package lang-uk
Summary:	uk translation to fet
Summary(hu.UTF-8):	uk fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-uk
uk translation to fet.

%prep
%setup -q
install %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
qmake-qt4 fet.pro \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_CXX="%{__cxx}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}/translations}

install -p fet $RPM_BUILD_ROOT%{_bindir}

# install manual
cp -p doc/fet.1 $RPM_BUILD_ROOT%{_mandir}/man1

# install translations
cp -p translations/fet_*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/translations

# install examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__cp} -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# install fet.desktop
install -d $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}

# install fet.png
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps
cp -p %{SOURCE5} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps

%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/translations/fet_untranslated.qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README REFERENCES THANKS TODO TRANSLATORS doc/*/* faq.html instructions.html tips.html
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_mandir}/man1/fet.1*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files lang-ar
%defattr(644,root,root,755)
%lang(ar) %{_datadir}/%{name}/translations/fet_ar.qm

%files lang-ca
%defattr(644,root,root,755)
%lang(ca) %{_datadir}/%{name}/translations/fet_ca.qm

%files lang-da
%defattr(644,root,root,755)
%lang(de) %{_datadir}/%{name}/translations/fet_da.qm

%files lang-de
%defattr(644,root,root,755)
%lang(de) %{_datadir}/%{name}/translations/fet_de.qm

%files lang-el
%defattr(644,root,root,755)
%lang(el) %{_datadir}/%{name}/translations/fet_el.qm

%files lang-es
%defattr(644,root,root,755)
%lang(es) %{_datadir}/%{name}/translations/fet_es.qm

%files lang-fa
%defattr(644,root,root,755)
%lang(fa) %{_datadir}/%{name}/translations/fet_fa.qm

%files lang-fr
%defattr(644,root,root,755)
%lang(fr) %{_datadir}/%{name}/translations/fet_fr.qm

%files lang-he
%defattr(644,root,root,755)
%lang(he) %{_datadir}/%{name}/translations/fet_he.qm

%files lang-hu
%defattr(644,root,root,755)
%lang(hu) %{_datadir}/%{name}/translations/fet_hu.qm

%files lang-id
%defattr(644,root,root,755)
%lang(id) %{_datadir}/%{name}/translations/fet_id.qm

%files lang-it
%defattr(644,root,root,755)
%lang(it) %{_datadir}/%{name}/translations/fet_it.qm

%files lang-lt
%defattr(644,root,root,755)
%lang(lt) %{_datadir}/%{name}/translations/fet_lt.qm

%files lang-mk
%defattr(644,root,root,755)
%lang(mk) %{_datadir}/%{name}/translations/fet_mk.qm

%files lang-ms
%defattr(644,root,root,755)
%lang(ms) %{_datadir}/%{name}/translations/fet_ms.qm

%files lang-nl
%defattr(644,root,root,755)
%lang(nl) %{_datadir}/%{name}/translations/fet_nl.qm

%files lang-pl
%defattr(644,root,root,755)
%lang(pl) %{_datadir}/%{name}/translations/fet_pl.qm

%files lang-pt
%defattr(644,root,root,755)
%lang(pl) %{_datadir}/%{name}/translations/fet_pt_BR.qm

%files lang-ro
%defattr(644,root,root,755)
%lang(ro) %{_datadir}/%{name}/translations/fet_ro.qm

%files lang-ru
%defattr(644,root,root,755)
%lang(ru) %{_datadir}/%{name}/translations/fet_ru.qm

%files lang-sk
%defattr(644,root,root,755)
%lang(sk) %{_datadir}/%{name}/translations/fet_sk.qm

%files lang-si
%defattr(644,root,root,755)
%lang(si) %{_datadir}/%{name}/translations/fet_si.qm

%files lang-tr
%defattr(644,root,root,755)
%lang(tr) %{_datadir}/%{name}/translations/fet_tr.qm

%files lang-uk
%defattr(644,root,root,755)
%lang(uk) %{_datadir}/%{name}/translations/fet_uk.qm
