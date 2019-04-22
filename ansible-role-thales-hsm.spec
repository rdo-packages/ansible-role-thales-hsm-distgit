# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%global srcname ansible_role_thales_hsm
%global rolename ansible-role-thales-hsm

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Ansible role for configuring Thales HSM Clients

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/openstack/ansible-role-thales-hsm
Source0:        https://github.com/openstack/%{rolename}/archive/v%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-d2to1
Requires:       ansible
%else
BuildRequires:  python%{pyver}-d2to1
Requires:       python3dist(ansible)
%endif

%description

Ansible role to configure Thales HSM clients

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{pyver_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_install}


%files
%doc README.rst
%license LICENSE
%{pyver_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
* Mon Apr 22 2019 RDO <dev@lists.rdoproject.org> 0.2.0-1
- Update to 0.2.0

