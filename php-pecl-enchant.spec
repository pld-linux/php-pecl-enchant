%define		_modname	enchant
%define		_status		beta

Summary:	%{_modname} - libenchant binder, support near all spelling tools
#Summary(pl):	%{_modname} - 
Name:		php-pecl-%{_modname}
Version:	0.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	3d4d57692803165e51eebe6cc8df175e
URL:		http://pecl.php.net/package/Modname/
BuildRequires:	enchant-devel
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
Enchant is a binder for libenchant. Libenchant provides a common
API for many spell libraries:
- aspell/pspell (intended to replace ispell)
- hspell (hebrew)
- ispell
- myspell (OpenOffice project, mozilla)
- uspell (primarily Yiddish, Hebrew, and Eastern European languages)
A plugin system allows to add custom spell support.

This extension has in PEAR status: %{_status}.

#%description -l pl
#
#To rozszerzenie ma w PEAR status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{docs,CREDITS}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
