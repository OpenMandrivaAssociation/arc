Name:		arc
Version:	5.21o
Release:	%mkrel 3
URL:		http://sourceforge.net/projects/arc/
Source:		%{name}-%{version}.tgz
Summary:	ARC archive compression utility
License:	GPL
Group:		Archiving/Compression 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
ARC is used to create and maintain file archives. Many other new archive
formats exist, but it can stil be useful if you have old .arc files.

%prep
%setup -q

%build
%make
%{__lzma} arc.1

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 arc %{buildroot}%{_bindir}/arc
%{__install} -Dp -m0755 marc %{buildroot}%{_bindir}/marc
%{__install} -Dp -m0644 arc.1.lzma %{buildroot}%{_mandir}/man1/arc.1.lzma

%files
%doc Changelog COPYING LICENSE Readme PATCHLEVEL Arcinfo Arc521.doc
%{_bindir}/%{name}
%{_bindir}/marc
%{_mandir}/man1/%{name}.1*

