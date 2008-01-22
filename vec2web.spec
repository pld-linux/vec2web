Summary:	Vector to web graphics converter
Summary(pl.UTF-8):	Konwerter grafiki wektorowej do bitmapowej
Name:		vec2web
Version:	2.0.4.7
Release:	1
License:	GPL v2
Group:		Applications/Graphics
#Source0-download: http://www.ribbonsoft.com/vec2web_downloads.html
Source0:	http://www.ribbonsoft.com/archives/vec2web/%{name}-%{version}-1.src.tar.gz
# Source0-md5:	7823c32dc991adfc80b6801b59e7dc8d
URL:		http://www.ribbonsoft.com/vec2web.html
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vec2web is a small tool to convert vector drawings (currently DXF)
to graphics which can be used on the web (currently PNG). However,
vec2web can also convert DXF drawings to PS (PostScript) and WBMP
(wireless bitmap) or display them in an X11 or Windows window.

%description -l pl.UTF-8
vec2web to małe narzędzie do konwersji rysunków wektorowych (obecnie
DXF) do grafiki nadającej się do użycia na stronach WWW (obecnie PNG).
vec2web potrafi także konwersjować rysunki DXF do formatu PS
(PostScript) i WBMP (wireless bitmap) oraz wyświetlać je w oknie X11
lub Windows.

%prep
%setup -q -n %{name}-%{version}-1.src

sed -i -e 's/ debug / release /' vec2web/src/vec2web.pro

%build
cd dxflib
%configure
%{__make} \
	CXX="%{__cc}"
cd ../qcadlib
%{__make} prepare
cd src
qmake qcadlib.pro \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}"
%{__make} \
	QTDIR=/usr
cd ../../vec2web/src
qmake vec2web.pro \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}" \
	QMAKE_RPATH=
%{__make} \
	QTDIR=/usr

%install
rm -rf $RPM_BUILD_ROOT

install -D vec2web/vec2web $RPM_BUILD_ROOT%{_bindir}/vec2web

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc vec2web/{AUTHORS,CHANGES,FAQ,README}
%attr(755,root,root) %{_bindir}/vec2web
