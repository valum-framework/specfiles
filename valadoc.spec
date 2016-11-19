Name:    valadoc
Summary: A documentation tool for Vala
License: GPL
Version: 0.35.0
Release: 1
Source0: %{name}-%{version}.tar.xz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libgvc)
BuildRequires: vala
BuildRequires: vala-devel

%description

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING README
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*
