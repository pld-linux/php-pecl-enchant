%define		_modname	enchant
%define		_status		stable
Summary:	%{_modname} - libenchant binder
Summary(pl):	%{_modname} - dowi±zania biblioteki libenchant
Name:		php-pecl-%{_modname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	916ea9f460d8196bd7088f5139cb32c2
URL:		http://pecl.php.net/package/enchant/
BuildRequires:	enchant-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enchant is a binder for libenchant. Libenchant provides a common API
for many spell libraries:
- aspell/pspell (intended to replace ispell)
- hspell (hebrew)
- ispell
- myspell (OpenOffice.org project, mozilla)
- uspell (primarily Yiddish, Hebrew, and Eastern European languages) A
  plugin system allows to add custom spell support.

In PECL status of this package is: %{_status}.

%description -l pl
Enchant jest dowi±zaniem do biblioteki libenchant, która udostêpnia
ujednolicone API dla wielu narzêdzi sprawdzaj±cych pisowniê:
- aspell/pspell (w zamierzeniu ma zast±piæ ispell)
- hspell (hebrajski)
- ispell
- myspell (projekt OpenOffice.org, mozilla)
- uspell (g³ównie Jidysz, Hebrajski oraz jêzyki wschodnioeuropejskie)
  System wtyczek pozwala na dodanie wsparcia dla kolejnych narzêdzi.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{docs,CREDITS}
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
