Name:    bump
Version: 0.0.1
Release: 1%{?dist}
Summary: Concurrency management for GObject/GIO based projects, especially those written in Vala.

Group:   Development/Libraries
License: LGPL
URL:     https://github.com/nemequ/bump
Source0: bump-%{version}.tar.bz2

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: vala

%description
Bump is a small utility library providing high-level concurrency related
objects designed for asynchronous GObject programming, especially from Vala.

%package devel
Summary:  Build files for Bump
Requires: bump

%description devel
Provides build files including C headers and Vala bindings.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING README
%{_libdir}/*
%exclude %{_libdir}/pkgconfig/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/*
