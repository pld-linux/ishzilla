Summary:	ishzilla - a Gecko-based web browser
Summary(pl):	ishzilla - przegl±darka WWW oparta na Gecko
Name:		ishzilla
Version:	0.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ishamael.tunkeymicket.com/tarballs/%{name}-%{version}.tar.gz
# Source0-md5:	02f96bfe82a9584b0dd0c72d9556cf62
Patch0:		%{name}-missing-gobject-init.patch
URL:		http://ishamael.tunkeymicket.com/
BuildRequires:	GConf2-devel >= 2.0.0
BuildRequires:	gob2 >= 2.0.5
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	libxml2-devel
BuildRequires:	mozilla-embedded-devel >= 1.4b
Requires(post):	GConf2
Obsoletes:	skipstone
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ishzilla is a web browser written in C using Gtk+-2 and Gecko, the
rendering engine from Mozilla.

%description -l pl
ishzilla to przegl±darka WWW napisana w C przy u¿yciu Gtk+-2 i Gecko,
silnika renderuj±cego Mozilli.

%prep
%setup -q
%patch -p1

%build
rm -f missing

CPPFLAGS="-I/usr/include/nspr"
CXXFLAGS="%{rpmcflags} -fno-rtti"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONFTOOL=true

rm -f $RPM_BUILD_ROOT%{_libdir}/ishzilla/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ishzilla
%attr(755,root,root) %{_libdir}/ishzilla/*.so
%{_sysconfdir}/gconf/schemas/*
