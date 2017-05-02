#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : seqdiag
Version  : 0.9.5
Release  : 7
URL      : https://pypi.python.org/packages/source/s/seqdiag/seqdiag-0.9.5.tar.gz
Source0  : https://pypi.python.org/packages/source/s/seqdiag/seqdiag-0.9.5.tar.gz
Summary  : seqdiag generates sequence-diagram image from text
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: seqdiag-bin
Requires: seqdiag-python
BuildRequires : blockdiag-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : reportlab-python
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
`seqdiag` generate sequence-diagram image file from spec-text file.
.. image:: https://drone.io/bitbucket.org/blockdiag/seqdiag/status.png
:target: https://drone.io/bitbucket.org/blockdiag/seqdiag
:alt: drone.io CI build status

%package bin
Summary: bin components for the seqdiag package.
Group: Binaries

%description bin
bin components for the seqdiag package.


%package python
Summary: python components for the seqdiag package.
Group: Default
Requires: blockdiag-python
Requires: nose-python
Requires: pep8
Requires: reportlab-python

%description python
python components for the seqdiag package.


%prep
%setup -q -n seqdiag-0.9.5

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/seqdiag

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
