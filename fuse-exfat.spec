Summary:	FUSE module to access exFAT filesystem
Summary(pl.UTF-8):	Moduł FUSE pozwalający na dostęp do systemu plików exFAT
Name:		fuse-exfat
Version:	0.9.3
Release:	1
License:	GPL v3+
Group:		Applications/System
#Source0Download: http://code.google.com/p/exfat/downloads/list
Source0:	http://exfat.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	42b5e36062cc3f89efd6c8d9b74c0c5d
URL:		http://code.google.com/p/exfat/
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	rpmbuild(macros) >= 1.385
BuildRequires:	scons
Requires:	libfuse >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to provide a full-featured exFAT file system
implementation for Linux and other Unix-like systems as a FUSE module.

Current status of the project is beta.

%description -l pl.UTF-8
Celem tego projektu jest umożliwienie pełnego dostępu do systemu
plików exFAT z poziomu Linuksa i innych systemów uniksowych poprzez
moduł FUSE.

Obecny status tego projektu to beta.

%prep
%setup -q

%build
%scons

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT/sbin \
%scons install

install fsck/exfatck $RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) /sbin/exfatck
%attr(755,root,root) /sbin/mount.exfat
%attr(755,root,root) /sbin/mount.exfat-fuse
