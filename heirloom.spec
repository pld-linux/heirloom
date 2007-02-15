%define snap	070115
Summary:	A collection of standard Unix utilities
Summary(pl.UTF-8):	Kolekcja standardowych narzędzi Uniksowych
Name:		heirloom
Version:	0.1
Release:	0.%{snap}.1
License:	Other
Group:		Applications
Source0:	http://dl.sourceforge.net/heirloom/%{name}-070115.tar.bz2
# Source0-md5:	0edcdfde085dbcf8882860e92230221b
Patch0:		%{name}-config.patch
Patch1:		%{name}-build.patch
URL:		http://heirloom.sourceforge.net/tools.html
BuildRequires:	bc
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	ed
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Heirloom Toolchest is a collection of standard Unix utilities.

- Derived from original Unix material released as Open Source by
  Caldera and Sun.
- Multiple versions of many utilities are provided to approach
  compatibility with various specifications and Unix flavors, namely
  SVID3/SVR4, SVID4/SVR4.2MP, POSIX.2-1992/SUSV2, POSIX.1-2001/SUSV3,
  and 4BSD (SVR4 /usr/ucb).
- Support for lines of arbitrary length and in many cases binary input
  data.
- Support for multibyte characters in UTF-8 and many East Asian
  encodings.
- More than 100 individual utilities including bc, cpio, diff, ed,
  file, find, grep, man, nawk, oawk, pax, ps, sed, sort, spell, and tar.
- The cpio utility can read and write zip files, GNU tar files, and
  the cpio formats of Cray UNICOS, SGI IRIX (-K), SCO UnixWare (-c) and
  Tru64 UNIX (-e). It is also available with the pax interface.
- Extensive documentation including a manual page for any utility.

%description -l pl.UTF-8
Heirloom Toolchest to zestaw standardowych narzędzi uniksowych.

- Wywodzi się z oryginalnego materiału uniksowego wydanego jako Open
  Source przez Calderę i Suna.
- Udostępniono wiele wersji wielu narzędzi w celu osiągnięcia
  zgodności z różnymi specyfikacjami i wersjami Uniksa, a konkretnie
  SVID3/SVR4, SVID4/SVR4.2MP, POSIX.2-1992/SUSV2, POSIX.1-2001/SUSV3
  oraz 4BSD (/usr/ucb w SVR4).
- Obsługa linii dowolnej długości i w wielu przypadkach binarnych
  danych wejściowych.
- Obsługa wielobajtowych znaków w UTF-8 i wielu kodowań
  wschodnioazjatyckich.
- Ponad 100 narzędzi, w tym bc, cpio, diff, ed, file, find, grep, man,
  nawk, oawk, pax, ps, sed, sort, spell i tar.
- Narzędzie cpio potrafi odczytywać i zapisywać pliki zip, pliki GNU
  tar oraz formaty cpio z systemów Cray UNICOS, SGI IRIX (-K), SCO
  UnixWare (-c) i Tru64 UNIX (-e). Jest dostępne także z interfejsem
  pax.
- Wyczerpująca dokumentacja wraz ze stronami manuala dla każdego
  narzędzia.

%prep
%setup -q -n %{name}-%{snap}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	DEFBIN=%{_bindir} \
	DEFSBIN=%{_bindir} \
	SV3BIN=%{_bindir} \
	S42BIN=%{_bindir} \
	SUSBIN=%{_bindir} \
	SU3BIN=%{_bindir} \
	UCBBIN=%{_bindir} \
	DEFSBIN=%{_bindir} \
	DEFLIB=%{_libdir} \
	MANDIR=%{_mandir} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	LNS="ln -s" \
	YACC="bison -y"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}}

%{__make} install \
	ROOT=$RPM_BUILD_ROOT \
	DEFBIN=%{_bindir} \
	DEFSBIN=%{_sbindir} \
	SV3BIN=%{_bindir} \
	S42BIN=%{_bindir} \
	SUSBIN=%{_bindir} \
	SU3BIN=%{_bindir} \
	UCBBIN=%{_bindir} \
	DEFLIB=%{_libdir} \
	MANDIR=%{_mandir} \
	TTYGRP="" \
	LNS="ln -s" \
	UCBINST="install"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc intro.txt CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%{_sysconfdir}/%{name}
