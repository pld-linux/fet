Summary:	FET is open source free software for automatically scheduling the timetable
Summary(hu.UTF-8):	FET egy nyílt forrású órarend-készítő program
Name:		fet
Version:	5.6.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.lalescu.ro/liviu/fet/download/%{name}-%{version}.tar.bz2
# Source0-md5:	00a416ed0d4b7613120c2737221d0ee5
URL:		http://www.lalescu.ro/liviu/fet/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	QtXml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FET is open source free software for automatically scheduling the
timetable of a school, high-school or university. It uses a fast and
efficient timetabling algorithm.

%description -l hu.UTF-8
FET egy nílt forrású szoftver, amely általános iskolák,
középiskolák, egyetemek órarendjét (időbeosztását) készíti
el. Egy gyors és hatékony algoritmust használ.

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
install translations/* $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
%{__cp} -a sample_inputs $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CONTRIBUTORS GUESTBOOK LINKS README REFERENCES SPONSORS THANKS TODO TRANSLATORS doc/*/*
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/fet*
%{_datadir}/%{name}
