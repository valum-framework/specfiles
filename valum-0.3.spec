Name:       valum-0.3
Version:    0.3.0
Release:    3%{?dist}
Summary:    Valum is a Web micro-framework written in Vala

Group:      Development/Libraries
License:    LGPL
URL:        https://github.com/valum-framework/valum
Source0:    %{url}/archive/v%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: fcgi-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: python3-sphinx
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: valadoc

%description
Valum is a Web micro-framework able to create highly scalable expressive Web
applications or services by taking advantage of machine code execution and
asynchronous I/O.

%package devel
Summary:  Build files for Valum
Requires: valum-0.3

%description devel
Provides build files including C header, Vala bindings and GIR introspection
meta-data.

%package doc
Summary:   Documentaion for Valum
BuildArch: noarch

%description doc
Provides user and API documentation in HTML and Devhelp formats.

%prep
%autosetup -n valum-%{version}

%build
%meson
%meson_build
%meson_build docs/en docs/api docs/devhelp

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
%{_datadir}/vala

%files doc
%{_defaultdocdir}/*
%{_datadir}/devhelp/books
