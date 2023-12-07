Summary:	Tool for editing debug info in ELF binaries
Name:		debugedit
Version:	5.0
Release:	7
Group:		Development/Other
License:	GPLv3+, parts GPLv2, LGPLv2.1
Source0:	https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz
Patch1:		rpm-4.15.0-find-debuginfo__mga-cfg.diff
# (tpg) patches from upstream
Patch2:		0001-use-READELF-not-readelf.patch
Patch3:		0002-tests-Handle-zero-directory-entry-in-.debug_line-DWA.patch
Patch4:		0003-find-debuginfo.sh-Remove-bogus-shift-after-dwz-singl.patch
Patch5:		0004-debugedit-Use-original-shdr-sh_type-to-check-for-NOB.patch
Patch6:		0005-debugedit-Handle-hppa-EM_PARISC-and-R_PARISC_DIR32.patch
Patch7:		0006-Fix-u-option.patch
Patch8:		0007-debugedit-Guard-against-NULL-names-returned-by-by-st.patch
Patch9:		0008-debugedit-Use-standard-libelf-elf_strptr.patch
Patch10:	0009-debugedit-Skip-calling-edit_dwarf2-if-not-rewriting-.patch
Patch11:	0010-debugedit-Add-support-for-loongarch.patch
Patch12:	0011-find-debuginfo-Pass-j-down-to-dwz.patch
Patch13:	0012-configure.ac-Use-AC_LINK_IFELSE-for-gz-none-check.patch
Patch14:	0013-configure.ac-Use-AC_LANG_PROGRAM-for-AC_LINK_IFELSE-.patch
Patch15:	0014-scripts-find-debuginfo.in-Add-q-quiet.patch
Patch16:	0015-configure.ac-Update-AC_PROG_CC-for-autoconf-2.70.patch
Patch17:	0016-debugedit-Use-z-not-Z-as-conversion-specifier.patch
Patch18:	0017-debugedit-skip-.debug_types-tests-if-compiler-doesn-.patch
Patch19:	0018-debuginfo-check-whether-compiler-needs-fdebug-macro.patch
Patch20:	0019-debugedit-Simplify-and-extend-.debug_line-tests.patch
Patch21:	0020-find-debuginfo-remove-duplicate-filenames-when-creat.patch
Patch22:	0021-find-debuginfo-Prefix-install_dir-to-PATH.patch
Patch23:	0022-find-debuginfo-Add-v-verbose-for-per-file-messages.patch
Patch24:	0023-Always-run-cpio-with-quiet.patch
Patch25:	0024-sepdebugcrcfix-Do-not-use-LFS64-functions.patch
Patch26:	0025-debugedit-Fix-missing-space-in-help-output.patch
# Patches from upstream ML that haven't landed in git yet
# https://sourceware.org/bugzilla/show_bug.cgi?id=28728
Patch100:	https://inbox.sourceware.org/debugedit/20231204223100.3495057-1-mark@klomp.org/t.mbox.gz
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
%make_build \
%if %{cross_compiling}
	HELP2MAN=%{_bindir}/true
%endif

%install
%make_install \
%if %{cross_compiling}
	HELP2MAN=%{_bindir}/true
%endif

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
