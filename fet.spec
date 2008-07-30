# TODO:
#	- fet doesn't respect locale settings
#	- mv sample_inputs files to proper place (maybe /usr/src/examples
#	  or _docdir)
#
Summary:	FET is open source free software for automatically scheduling the timetable
Summary(hu.UTF-8):	FET egy nyílt forrású órarend-készítő program
Name:		fet
Version:	5.6.0
Release:	0.2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.lalescu.ro/liviu/fet/download/%{name}-%{version}.tar.bz2
# Source0-md5:	00a416ed0d4b7613120c2737221d0ee5
URL:		http://www.lalescu.ro/liviu/fet/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FET is open source free software for automatically scheduling the
timetable of a school, high-school or university. It uses a fast and
efficient timetabling algorithm.

%description -l hu.UTF-8
FET egy nílt forrású szoftver, amely általános iskolák, középiskolák,
egyetemek órarendjét (időbeosztását) készíti el. Egy gyors és hatékony
algoritmust használ.

%prep
%setup -q

%build
qmake-qt4 fet.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}/translations}

install fet $RPM_BUILD_ROOT%{_bindir}
install doc/fet.1 $RPM_BUILD_ROOT%{_mandir}/man1
install translations/fet_*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
%{__cp} -a sample_inputs $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/%{name}/translations/fet_untranslated.qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CONTRIBUTORS GUESTBOOK LINKS README REFERENCES SPONSORS THANKS TODO TRANSLATORS doc/*/*
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/fet.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sample_inputs
%dir %{_datadir}/%{name}/translations
%lang(ar) %{_datadir}/%{name}/translations/fet_ar.qm
%lang(ca) %{_datadir}/%{name}/translations/fet_ca.qm
%lang(de) %{_datadir}/%{name}/translations/fet_de.qm
%lang(el) %{_datadir}/%{name}/translations/fet_el.qm
%lang(es) %{_datadir}/%{name}/translations/fet_es.qm
%lang(fr) %{_datadir}/%{name}/translations/fet_fr.qm
%lang(hu) %{_datadir}/%{name}/translations/fet_hu.qm
%lang(id) %{_datadir}/%{name}/translations/fet_id.qm
%lang(it) %{_datadir}/%{name}/translations/fet_it.qm
%lang(mk) %{_datadir}/%{name}/translations/fet_mk.qm
%lang(ms) %{_datadir}/%{name}/translations/fet_ms.qm
%lang(nl) %{_datadir}/%{name}/translations/fet_nl.qm
%lang(pl) %{_datadir}/%{name}/translations/fet_pl.qm
%lang(ro) %{_datadir}/%{name}/translations/fet_ro.qm
%lang(tr) %{_datadir}/%{name}/translations/fet_tr.qm
