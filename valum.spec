Name:       valum
Version:    0.3.0
Release:    1%{?dist}
Summary:    Valum is a Web micro-framework written in Vala

Group:      Development/Libraries
License:    LGPL
URL:        https://github.com/valum-framework/valum
Source0:    %{url}/releases/download/v%{version}/valum-%{version}.tar.bz2

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: fcgi-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: vala
BuildRequires: vala-tools

%description
Valum is a Web micro-framework able to create highly scalable expressive Web
applications or services by taking advantage of machine code execution and
asynchronous I/O.

%package devel
Summary:  Build files for Valum
Requires: valum

%description devel
Provides build files including C header, Vala bindings and GIR introspection
meta-data.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md COPYING
%{_libdir}/*
%exclude %{_libdir}/pkgconfig

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/*
