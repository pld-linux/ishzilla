Summary:	ishzilla is a web browse
Summary(pl):	ishzilla to przegl±darka www
Name:		ishzilla
Version:	0.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ishamael.tunkeymicket.com/tarballs/%{name}-%{version}.tar.gz
URL:		http://ishamael.tunkeymicket.com/
BuildRequires:	GConf2-devel >= 2.0.0
BuildRequires:	GOB >= 2.0.5
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	libxml2
BuildRequires:	mozilla-embedded-devel >= 1.4b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ishzilla is a web browser written in C using Gtk+-2 and Gecko, the
rendering engine from Mozilla.

%description -l pl
ishzilla to przegldarka web napisana w C przy u¿yciu Gtk+-2 i Gecko,
silnika renderujacego Mozilli.

%prep
%setup -q

%build
rm -f missing

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
