Summary:	Tool for editing debug info in ELF binaries
Name:		debugedit
Version:	5.0
Release:	8
Group:		Development/Other
License:	GPLv3+, parts GPLv2, LGPLv2.1
Source0:	https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz
Patch0:		rpm-4.15.0-find-debuginfo__mga-cfg.diff
# Look at *.so* files regardless of their permissions - some projects
# follow Debian-ish policies of not making libraries executable, and
# the debuginfo generator runs before the permission fixup
# (it has to, because the same set of scripts that invokes permission
# fixup also invokes further stripping).
Patch1:		debugedit-5.0-look-at-so-files.patch
# (tpg) patches from upstream
Patch101:	0001-use-READELF-not-readelf.patch
Patch102:	0002-tests-Handle-zero-directory-entry-in-.debug_line-DWA.patch
Patch103:	0003-find-debuginfo.sh-Remove-bogus-shift-after-dwz-singl.patch
Patch104:	0004-debugedit-Use-original-shdr-sh_type-to-check-for-NOB.patch
Patch105:	0005-debugedit-Handle-hppa-EM_PARISC-and-R_PARISC_DIR32.patch
Patch106:	0006-Fix-u-option.patch
Patch107:	0007-debugedit-Guard-against-NULL-names-returned-by-by-st.patch
Patch108:	0008-debugedit-Use-standard-libelf-elf_strptr.patch
Patch109:	0009-debugedit-Skip-calling-edit_dwarf2-if-not-rewriting-.patch
Patch110:	0010-debugedit-Add-support-for-loongarch.patch
Patch111:	0011-find-debuginfo-Pass-j-down-to-dwz.patch
Patch112:	0012-configure.ac-Use-AC_LINK_IFELSE-for-gz-none-check.patch
Patch113:	0013-configure.ac-Use-AC_LANG_PROGRAM-for-AC_LINK_IFELSE-.patch
Patch114:	0014-scripts-find-debuginfo.in-Add-q-quiet.patch
Patch115:	0015-configure.ac-Update-AC_PROG_CC-for-autoconf-2.70.patch
Patch116:	0016-debugedit-Use-z-not-Z-as-conversion-specifier.patch
Patch117:	0017-debugedit-skip-.debug_types-tests-if-compiler-doesn-.patch
Patch118:	0018-debuginfo-check-whether-compiler-needs-fdebug-macro.patch
Patch119:	0019-debugedit-Simplify-and-extend-.debug_line-tests.patch
Patch120:	0020-find-debuginfo-remove-duplicate-filenames-when-creat.patch
Patch121:	0021-find-debuginfo-Prefix-install_dir-to-PATH.patch
Patch122:	0022-find-debuginfo-Add-v-verbose-for-per-file-messages.patch
Patch123:	0023-Always-run-cpio-with-quiet.patch
Patch124:	0024-sepdebugcrcfix-Do-not-use-LFS64-functions.patch
Patch125:	0025-debugedit-Fix-missing-space-in-help-output.patch
Patch126:	0026-debugedit-Add-support-for-.debug_str_offsets-DW_FORM.patch
Patch127:	0027-debugedit-Only-write-the-ELF-file-when-updating-stri.patch
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

%files
%license COPYING COPYING3 COPYING.LIB
%{_bindir}/debugedit
%{_bindir}/find-debuginfo
%{_bindir}/sepdebugcrcfix
%doc %{_mandir}/man1/debugedit.1*
%doc %{_mandir}/man1/find-debuginfo.1*
%doc %{_mandir}/man1/sepdebugcrcfix.1*
