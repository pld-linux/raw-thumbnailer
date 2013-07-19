Summary:	Lightweight raw image thumbnailer
Summary(pl.UTF-8):	Lekki program do wykonywania miniaturek dla zdjęć w formacie raw
Name:		raw-thumbnailer
Version:	0.2.1
Release:	1
License:	LGPL v2.1+
Group:		Applications/Graphics
#Source0Download: http://code.google.com/p/raw-thumbnailer/downloads/list
Source0:	http://raw-thumbnailer.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	a39282120d8f754e9f6adb768d65b72a
URL:		http://code.google.com/p/raw-thumbnailer/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	libopenraw-gnome-devel >= 0.0.4
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
Requires:	libopenraw-gnome >= 0.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This simple program generates thumbnails of digital camera raw image
files using libopenraw and GDK. It supports the same file formats as
libopenraw.

This thumbnailer is designed to be small, lightweight and fast. It is
primarily intended to be used with file managers (although it could
easily be used by a photograph management program) and it used by
Thunar-thumbnailers.

%description -l pl.UTF-8
Ten prosty program generuje miniaturki cyfrowych zdjęć w formacie
raw przy użyciu bibliotek libopenraw i GDK. Obsługuje te same formaty
co libopenraw.

Ten generator miniaturek zaprojektowano by był mały, lekki i szybki.
Jest głównie przeznaczony do użytku z menadżerami plików
(aczkolwiek równie dobrze może być użyty przez program do
zarządzania fotografiami) i jest używany przez Thunar-thumbnailers.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/raw-thumbnailer
