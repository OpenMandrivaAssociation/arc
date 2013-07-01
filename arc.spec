Name:		arc
Version:	5.21o
Release:	%mkrel 5
URL:		http://sourceforge.net/projects/arc/
Source:		%{name}-%{version}.tgz
Summary:	Archive compression utility
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 5.21o-5mdv2011.0
+ Revision: 616602
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 5.21o-4mdv2010.0
+ Revision: 424013
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 5.21o-3mdv2009.0
+ Revision: 240430
- rebuild
- fix no-buildroot-tag

* Wed Aug 08 2007 Nicolas Vigier <nvigier@mandriva.com> 5.21o-1mdv2008.0
+ Revision: 60124
- Import arc

