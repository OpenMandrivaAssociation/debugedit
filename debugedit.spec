Summary:	Tool for editing debug info in ELF binaries
Name:		debugedit
Version:	5.0
Release:	5
Source0:	https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz
Patch0:		0001-find-debuginfo.sh-decompress-DWARF-compressed-ELF-se.patch
Patch1:		rpm-4.15.0-find-debuginfo__mga-cfg.diff
Patch2:		0001-tests-Handle-zero-directory-entry-in-.debug_line-DWA.patch
Group:		Development/Other
License:	GPLv3+, parts GPLv2, LGPLv2.1
BuildRequires:	autoconf
BuildRequires:	make
BuildRequires:	pkgconfig(libelf)
BuildRequires:	pkgconfig(libdw)
BuildRequires:	help2man

# The find-debuginfo.sh script has a couple of tools it needs at runtime.
# For strip_to_debug, eu-strip
Requires:	elfutils
# For add_minidebug, readelf, awk, nm, sort, comm, objcopy, xz
Requires:	binutils, gawk, coreutils, xz
# For find and xargs
Requires:	findutils
# For do_file, gdb_add_index
# We only need gdb-add-index, so suggest gdb-minimal (full gdb is also ok)
Requires:	/usr/bin/gdb-add-index
Suggests:	gdb-minimal
# For run_job, sed
Requires:	sed
# For dwz
Requires:	dwz
# For append_uniq, grep
Requires:	grep

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
