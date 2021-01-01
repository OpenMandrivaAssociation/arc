%define debug_package %{nil}

Name:		arc
Version:	5.21q
Release:	1
URL:		https://github.com/ani6al/arc
Source:		https://github.com/ani6al/arc/archive/%{version}/arc-%{version}.tar.gz
Patch0:		arc-5.21q-compile.patch
Summary:	Archive compression utility
License:	GPL
Group:		Archiving/Compression 

%description
ARC is used to create and maintain file archives. Many other new archive
formats exist, but it can stil be useful if you have old .arc files.

%prep
%autosetup -p1

%build
%make_build OPT="%{optflags}"

%install
%{__install} -Dp -m0755 arc %{buildroot}%{_bindir}/arc
%{__install} -Dp -m0755 marc %{buildroot}%{_bindir}/marc
%{__install} -Dp -m0644 arc.1 %{buildroot}%{_mandir}/man1/arc.1

%files
%doc Changelog COPYING LICENSE Readme PATCHLEVEL Arcinfo Arc521.doc
%{_bindir}/%{name}
%{_bindir}/marc
%{_mandir}/man1/%{name}.1*
