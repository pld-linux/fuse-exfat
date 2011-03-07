Summary:	FUSE module to access exFAT filesystem
Summary(pl.UTF-8):	Moduł FUSE pozwalający na dostęp do systemu plików exFAT
Name:		fuse-exfat
Version:	0.9.4
Release:	1
License:	GPL v3+
Group:		Applications/System
#Source0Download: http://code.google.com/p/exfat/downloads/list
Source0:	http://exfat.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	f9d66d9a8358c9151e38a97721f6101a
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
%scons \

%install
rm -rf $RPM_BUILD_ROOT

%scons install \
	DESTDIR=$RPM_BUILD_ROOT/sbin

install -d $RPM_BUILD_ROOT%{_mandir}/man8
install fuse/mount.exfat-fuse.8 $RPM_BUILD_ROOT%{_mandir}/man8
echo '.so mount.exfat-fuse.8' >$RPM_BUILD_ROOT%{_mandir}/man8/mount.exfat.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) /sbin/mount.exfat
%attr(755,root,root) /sbin/mount.exfat-fuse
%{_mandir}/man8/mount.exfat.8*
%{_mandir}/man8/mount.exfat-fuse.8*
