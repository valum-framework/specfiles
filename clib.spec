Name: clib
Version: 1.5.0
Release: 1
Summary: C package manager-ish
License: MIT
Source0: https://github.com/clibs/%{name}/archive/%{version}.tar.gz

BuildRequires: libcurl-devel

%description

%prep
%autosetup

%build
make

%install
make install PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/*
