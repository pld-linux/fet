# TODO:
#	- optflags
#	- fet doesn't respect locale settings
#
Summary:	FET is open source free software for automatically scheduling the timetable
Summary(hu.UTF-8):	FET egy nyílt forrású órarend-készítő program
Summary(pl.UTF-8):	Narzędzie do automatycznego układania planów dla szkół i uczelni
Name:		fet
Version:	5.12.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.lalescu.ro/liviu/fet/download/%{name}-%{version}.tar.bz2
# Source0-md5:	3a203f86ed52b883899abce6abc1f6b0
Source1:	http://www.lalescu.ro/liviu/fet/doc/en/faq.html
# Source1-md5:	0bad32ba56fa0687956280d0bfb7d70a
Source2:	http://www.lalescu.ro/liviu/fet/doc/en/instructions.html
# Source2-md5:	68ffbb297e609ea26526b288c6e2369c
Source3:	http://www.lalescu.ro/liviu/fet/doc/en/tips.html
# Source3-md5:	d2a0a061f224d3c7ab96f7a3257a3b35
URL:		http://www.lalescu.ro/liviu/fet
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	unzip
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

%description lang-ar
ar translation to fet.

%package lang-ca
Summary:	Catalan translation to fet
Summary(hu.UTF-8):	Katalán fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-ca
Catalan translation to fet.

%package lang-de
Summary:	German translation to fet
Summary(hu.UTF-8):	Német fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-de
German translation to fet.

%package lang-el
Summary:	Greek translation to fet
Summary(hu.UTF-8):	Görög fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-el
Greek translation to fet.

%package lang-es
Summary:	Spanish translation to fet
Summary(hu.UTF-8):	Spanyol fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-es
Spanish translation to fet.

%package lang-fa
Summary:	fa translation to fet
Summary(hu.UTF-8):	fa fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-fa
fa translation to fet.

%package lang-fr
Summary:	French translation to fet
Summary(hu.UTF-8):	Francia fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-fr
French translation to fet.

%package lang-hu
Summary:	Hungarian translation to fet
Summary(hu.UTF-8):	Magyar fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-hu
Hungarian translation to fet.

%description lang-hu -l hu.UTF-8
Magyar fordítás fet-hez.

%package lang-id
Summary:	id translation to fet
Summary(hu.UTF-8):	id fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-id
id translation to fet.

%package lang-it
Summary:	Italian translation to fet
Summary(hu.UTF-8):	Olasz fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-it
Italian translation to fet.

%package lang-lt
Summary:	Lithuanian translation to fet
Summary(hu.UTF-8):	Litván fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-lt
Lithuanian translation to fet.

%package lang-mk
Summary:	mk translation to fet
Summary(hu.UTF-8):	mk fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-mk
mk translation to fet.

%package lang-ms
Summary:	ms translation to fet
Summary(hu.UTF-8):	ms fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-ms
ms translation to fet.

%package lang-nl
Summary:	nl translation to fet
Summary(hu.UTF-8):	nl fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-nl
nl translation to fet.

%package lang-pl
Summary:	Polish translation to fet
Summary(hu.UTF-8):	Lengyel fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-pl
Polish translation to fet.

%package lang-ro
Summary:	Romanian translation to fet
Summary(hu.UTF-8):	Román fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-ro
Romanian translation to fet.

%package lang-ru
Summary:	Russian translation to fet
Summary(hu.UTF-8):	Orosz fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-ru
Russian translation to fet.

%package lang-tr
Summary:	tr translation to fet
Summary(hu.UTF-8):	tr fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-tr
tr translation to fet.

%package lang-uk
Summary:	uk translation to fet
Summary(hu.UTF-8):	uk fordítás fet-hez
Group:		I18n
Requires:	%{name} = %{version}-%{release}

%description lang-uk
uk translation to fet.

%prep
%setup -q
install %{SOURCE1} %{SOURCE2} %{SOURCE3} .

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
%doc AUTHORS ChangeLog CONTRIBUTORS README REFERENCES THANKS TODO TRANSLATORS doc/*/* faq.html instructions.html tips.html
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
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

%files lang-ro
%defattr(644,root,root,755)
%lang(ro) %{_datadir}/%{name}/translations/fet_ro.qm

%files lang-ru
%defattr(644,root,root,755)
%lang(ru) %{_datadir}/%{name}/translations/fet_ru.qm

%files lang-tr
%defattr(644,root,root,755)
%lang(tr) %{_datadir}/%{name}/translations/fet_tr.qm

%files lang-uk
%defattr(644,root,root,755)
%lang(uk) %{_datadir}/%{name}/translations/fet_uk.qm
