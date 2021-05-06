Name:		debugedit
Version:	0.2
Release:	1
Summary:	Tool for editing debug info in ELF binaries
Source0:	https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz
Group:		Development/Other
License:	GPLv3+, parts GPLv2, LGPLv2.1
BuildRequires:	autoconf
BuildRequires:	make
BuildRequires:	pkgconfig(libelf)
BuildRequires:	pkgconfig(libdw)
BuildRequires:	help2man

%description
Tool for editing debug info in ELF binaries

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%files
%license COPYING COPYING3 COPYING.LIB
%{_bindir}/debugedit
%{_bindir}/find-debuginfo.sh
%{_bindir}/sepdebugcrcfix
%{_mandir}/man1/debugedit.1*
%{_mandir}/man1/find-debuginfo.sh.1*
%{_mandir}/man1/sepdebugcrcfix.1*
