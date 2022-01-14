Summary:	Tool for editing debug info in ELF binaries
Name:		debugedit
Version:	5.0
Release:	2
Source0:	https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz
Group:		Development/Other
License:	GPLv3+, parts GPLv2, LGPLv2.1
BuildRequires:	autoconf
BuildRequires:	make
BuildRequires:	pkgconfig(libelf)
BuildRequires:	pkgconfig(libdw)
BuildRequires:	help2man

%description
Tool for editing debug info in ELF binaries.

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

# For compatibility with older rpm builds
# This should be removed for OMV 5.0
ln -s find-debuginfo %{buildroot}%{_bindir}/find-debuginfo.sh

%files
%license COPYING COPYING3 COPYING.LIB
%{_bindir}/debugedit
%{_bindir}/find-debuginfo
%{_bindir}/find-debuginfo.sh
%{_bindir}/sepdebugcrcfix
%doc %{_mandir}/man1/debugedit.1*
%doc %{_mandir}/man1/find-debuginfo.1*
%doc %{_mandir}/man1/sepdebugcrcfix.1*
