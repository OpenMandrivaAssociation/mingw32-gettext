%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

Name:      mingw32-gettext
Version:   0.17
Release:   %mkrel 3
Summary:   GNU libraries and utilities for producing multi-lingual messages

License:   GPLv2+ and LGPLv2+
Group:     Development/Other
URL:       https://www.gnu.org/software/gettext/
Source0:   http://ftp.gnu.org/pub/gnu/gettext/gettext-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Patch0:    mingw32-gettext-0.17-gnulib-optarg-symbols.patch

BuildArch: noarch

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-runtime
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-iconv
BuildRequires: mingw32-termcap

# Possible extra BRs.  These are used if available, but
# not required just for building.
#BuildRequires: mingw32-dlfcn
#BuildRequires: mingw32-libxml2
#BuildRequires: mingw32-expat
#BuildRequires: mingw32-glib2


%description
MinGW Windows Gettext library


%prep
%setup -q -n gettext-%{version}

%patch0 -p1


%build
%{_mingw32_configure} \
  --disable-java \
  --disable-native-java \
  --disable-csharp \
  --disable-static \
  --enable-threads=win32 \
  --without-emacs
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_mingw32_datadir}/locale/locale.alias
rm -f $RPM_BUILD_ROOT%{_mingw32_libdir}/charset.alias
rm -f $RPM_BUILD_ROOT%{_mingw32_datadir}/info/dir

# Remove man pages, these are available in base gettext-devel.
rm -rf $RPM_BUILD_ROOT%{_mingw32_mandir}/man1/
rm -rf $RPM_BUILD_ROOT%{_mingw32_mandir}/man3/

%find_lang %{name} --all-name


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%{_mingw32_bindir}/autopoint
%{_mingw32_bindir}/envsubst.exe
%{_mingw32_bindir}/gettext.exe
%{_mingw32_bindir}/gettext.sh
%{_mingw32_bindir}/gettextize
%{_mingw32_bindir}/libasprintf-0.dll
%{_mingw32_bindir}/libgettextlib-0-17.dll
%{_mingw32_bindir}/libgettextpo-0.dll
%{_mingw32_bindir}/libgettextsrc-0-17.dll
%{_mingw32_bindir}/libintl-8.dll
%{_mingw32_bindir}/msg*.exe
%{_mingw32_bindir}/ngettext.exe
%{_mingw32_bindir}/recode-sr-latin.exe
%{_mingw32_bindir}/xgettext.exe

%{_mingw32_includedir}/autosprintf.h
%{_mingw32_includedir}/gettext-po.h
%{_mingw32_includedir}/libintl.h

%{_mingw32_libdir}/gettext

%{_mingw32_libdir}/libasprintf.dll.a
%{_mingw32_libdir}/libasprintf.la

%{_mingw32_libdir}/libgettextlib.dll.a
%{_mingw32_libdir}/libgettextlib.la

%{_mingw32_libdir}/libgettextpo.dll.a
%{_mingw32_libdir}/libgettextpo.la

%{_mingw32_libdir}/libgettextsrc.dll.a
%{_mingw32_libdir}/libgettextsrc.la

%{_mingw32_libdir}/libintl.dll.a
%{_mingw32_libdir}/libintl.la

%{_mingw32_docdir}/gettext
%{_mingw32_docdir}/libasprintf/autosprintf_all.html

%{_mingw32_datadir}/gettext/

%{_mingw32_datadir}/aclocal/*m4
%{_mingw32_datadir}/info/autosprintf.info
%{_mingw32_datadir}/info/gettext.info
