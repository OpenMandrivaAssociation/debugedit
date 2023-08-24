Summary:	Tool for editing debug info in ELF binaries
Name:		debugedit
Version:	5.0
Release:	6
Group:		Development/Other
License:	GPLv3+, parts GPLv2, LGPLv2.1
Source0:	https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz
Patch1:		rpm-4.15.0-find-debuginfo__mga-cfg.diff
# (tpg) patches from upstream
Patch2:		0001-use-READELF-not-readelf.patch
Patch3:		0001-tests-Handle-zero-directory-entry-in-.debug_line-DWA.patch
Patch4:		0001-find-debuginfo-Pass-j-down-to-dwz.patch
Patch5:		0002-configure.ac-Use-AC_LINK_IFELSE-for-gz-none-check.patch
Patch6:		0003-configure.ac-Use-AC_LANG_PROGRAM-for-AC_LINK_IFELSE-.patch
Patch7:		0004-scripts-find-debuginfo.in-Add-q-quiet.patch
Patch8:		0005-configure.ac-Update-AC_PROG_CC-for-autoconf-2.70.patch
Patch9:		0006-debugedit-Use-z-not-Z-as-conversion-specifier.patch
Patch10:	0010-find-debuginfo-remove-duplicate-filenames-when-creat.patch
Patch11:	0011-find-debuginfo-Prefix-install_dir-to-PATH.patch
Patch12:	0012-find-debuginfo-Add-v-verbose-for-per-file-messages.patch
Patch13:	0013-Always-run-cpio-with-quiet.patch
Patch14:	0014-sepdebugcrcfix-Do-not-use-LFS64-functions.patch
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
autoreconf -f -v -i

%build
%configure
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
