Name:    valadoc
Summary: A documentation tool for Vala
License: GPL
Version: 0.30.0
Release: 1
Source0: %{name}-%{version}.tar.xz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libvala-0.30)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libgvc)
BuildRequires: vala

%description

%prep
%setup -q

%build
%configure
make

%install
%make_install

%files
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*
