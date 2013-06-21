%define		php_name	php%{?php_suffix}
%define		modname	enchant
%define		status		stable
Summary:	%{modname} - libenchant binder
Summary(pl.UTF-8):	%{modname} - dowiązania biblioteki libenchant
Name:		%{php_name}-pecl-%{modname}
Version:	1.1.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	88a9ebc2fed2f568181c55bd61e12e03
URL:		http://pecl.php.net/package/enchant/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	enchant-devel
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
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

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Enchant jest dowiązaniem do biblioteki libenchant, która udostępnia
ujednolicone API dla wielu narzędzi sprawdzających pisownię:
- aspell/pspell (w zamierzeniu ma zastąpić ispell)
- hspell (hebrajski)
- ispell
- myspell (projekt OpenOffice.org, mozilla)
- uspell (głównie Jidysz, Hebrajski oraz języki wschodnioeuropejskie)
  System wtyczek pozwala na dodanie wsparcia dla kolejnych narzędzi.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%doc CREDITS docs
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
