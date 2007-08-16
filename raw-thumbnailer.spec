Summary:	Lightweight raw image thumbnailer
Summary(pl.UTF-8):	Lekki program do wykonywania miniaturek dla zdjęć w formacie raw
Name:		raw-thumbnailer
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://raw-thumbnailer.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	f6980ceb4cf80104cc3912a6711544f6
URL:		http://code.google.com/p/raw-thumbnailer/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libopenraw-devel
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
raw używając biblioteki libopenraw i GDK. Wspiera te same formaty co
libopenraw.

Ten generator miniaturek zaprojektowano by był mały, lekki i szybki.
Jest głównie przeznaczony do użytku z menadżerami plików
(aczkolwiek równie dobrze możę być użyty przez program
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/raw-thumbnailer
