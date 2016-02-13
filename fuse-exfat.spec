Summary:	FUSE module to access exFAT filesystem
Summary(pl.UTF-8):	Moduł FUSE pozwalający na dostęp do systemu plików exFAT
Name:		fuse-exfat
Version:	1.2.3
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/relan/exfat/releases
Source0:	https://github.com/relan/exfat/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fca71e6598f79d037a3c7c969cb5710c
Patch0:		%{name}-man.patch
URL:		https://github.com/relan/exfat
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11.2
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	pkgconfig
Requires:	libfuse >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This project aims to provide a full-featured exFAT file system
implementation for Linux and other Unix-like systems as a FUSE module.

%description -l pl.UTF-8
Celem tego projektu jest umożliwienie pełnego dostępu do systemu
plików exFAT z poziomu Linuksa i innych systemów uniksowych poprzez
moduł FUSE.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so mount.exfat-fuse.8' >$RPM_BUILD_ROOT%{_mandir}/man8/mount.exfat.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) /sbin/mount.exfat
%attr(755,root,root) /sbin/mount.exfat-fuse
%{_mandir}/man8/mount.exfat.8*
%{_mandir}/man8/mount.exfat-fuse.8*
