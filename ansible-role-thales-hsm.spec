%global srcname ansible_role_thales_hsm
%global rolename ansible-role-thales-hsm

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        0.2.0
Release:        1
Summary:        Ansible role for configuring Thales HSM Clients

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/dmend/ansible-role-thales-hsm
Source0:        https://github.com/dmend/ansible-role-thales-hsm/archive/v0.2.0.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python2-pbr

Requires: ansible

%description

Ansible role to configure Thales HSM clients

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%py2_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py2_install


%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
