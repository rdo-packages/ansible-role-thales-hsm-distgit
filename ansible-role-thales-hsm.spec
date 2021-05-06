%global srcname ansible_role_thales_hsm
%global rolename ansible-role-thales-hsm

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Ansible role for configuring Thales HSM Clients

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ansible-role-thales-hsm
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3dist(ansible)

%description

Ansible role to configure Thales HSM clients

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
* Thu May 06 2021 RDO <dev@lists.rdoproject.org> 1.0.0-1
- Update to 1.0.0

