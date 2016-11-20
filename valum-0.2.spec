Name:       valum-0.2
Version:    0.2.16
Release:    5%{?dist}
Summary:    Valum is a web micro-framework written in Vala

Group:      Development/Libraries
License:    LGPL
URL:        https://github.com/valum-framework/valum
Source0:    %{url}/archive/v%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: fcgi-devel
BuildRequires: python3-sphinx
BuildRequires: vala
BuildRequires: vala-tools

%description
Valum is a web micro-framework able to create highly scalable expressive web
applications or services by taking advantage of machine code execution and
asynchronous I/O.

%package devel
Summary:    Build files for Valum
Requires:   valum-0.2

%description devel
Provides build files including C header, Vala bindings and GIR introspection
meta-data.

%package doc
Summary:    Documentation for Valum
BuildArch:  noarch

%description doc
Provides user documentation in HTML format.

%prep
%autosetup -n valum-%{version}

%build
./waf configure --prefix=%{_prefix} CFLAGS="%{optflags}" VALAFLAGS='--debug'
./waf build

%install
./waf install --destdir=%{buildroot}
mkdir -p %{buildroot}%{_defaultdocdir}/valum-0.2/user
cp -R build/docs %{buildroot}%{_defaultdocdir}/valum-0.2/user/en

%check
./build/tests/tests

%files
%doc README.md COPYING
%{_libdir}/*
%exclude %{_libdir}/pkgconfig/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/*
%{_datadir}/vala/*

%files doc
%{_defaultdocdir}/valum-0.2/*
