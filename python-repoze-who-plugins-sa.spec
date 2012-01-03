%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define _rcver rc1

Name:           python-repoze-who-plugins-sa
Version:        1.0
Release:        0.4.%{_rcver}%{?dist}
Summary:        The repoze.who SQLAlchemy plugin

Group:          Development/Languages
License:        BSD
URL:            http://code.gustavonarea.net/repoze.who.plugins.sa
Source0:        http://pypi.python.org/packages/source/r/repoze.who.plugins.sa/repoze.who.plugins.sa-%{version}%{_rcver}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel python-setuptools-devel python-repoze-who
BuildRequires:  python-elixir python-sqlalchemy python-coverage python-nose

Requires:       python-repoze-who
Requires:       python-sqlalchemy

%description
This plugin provides one repoze.who authenticator which works with SQLAlchemy
or Elixir-based models.


%prep
%setup -q -n repoze.who.plugins.sa-%{version}%{_rcver}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{__rm} -fr %{buildroot}%{python_sitelib}/tests

#%check
#PYTHONPATH=$(pwd) nosetests

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.3.rc1
- Remove the test suite, since it conflicts with other packages (#512759)

* Thu May 21 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.2.rc1
- Update to 1.0rc1
- Add python-elixir, python-sqlalchemy, python-coverage, python-nose,
  and python-repoze-who to the BuildRequires
- Remove the setuptools patch

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.1.b2.r2909
- Initial package for Fedora
