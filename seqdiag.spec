#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : seqdiag
Version  : 2.0.0
Release  : 22
URL      : https://files.pythonhosted.org/packages/35/cf/1e1fa65111f90747e9c9f2438674b5c77dbb00a0b14a01ba280c7c34bad9/seqdiag-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/35/cf/1e1fa65111f90747e9c9f2438674b5c77dbb00a0b14a01ba280c7c34bad9/seqdiag-2.0.0.tar.gz
Summary  : seqdiag generates sequence-diagram image from text
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: seqdiag-bin = %{version}-%{release}
Requires: seqdiag-license = %{version}-%{release}
Requires: seqdiag-python = %{version}-%{release}
Requires: seqdiag-python3 = %{version}-%{release}
Requires: blockdiag
BuildRequires : blockdiag
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : olefile
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
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
Requires: seqdiag-license = %{version}-%{release}

%description bin
bin components for the seqdiag package.


%package license
Summary: license components for the seqdiag package.
Group: Default

%description license
license components for the seqdiag package.


%package python
Summary: python components for the seqdiag package.
Group: Default
Requires: seqdiag-python3 = %{version}-%{release}

%description python
python components for the seqdiag package.


%package python3
Summary: python3 components for the seqdiag package.
Group: Default
Requires: python3-core
Provides: pypi(seqdiag)
Requires: pypi(blockdiag)

%description python3
python3 components for the seqdiag package.


%prep
%setup -q -n seqdiag-2.0.0
cd %{_builddir}/seqdiag-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603404095
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/seqdiag
cp %{_builddir}/seqdiag-2.0.0/LICENSE %{buildroot}/usr/share/package-licenses/seqdiag/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/seqdiag-2.0.0/src/seqdiag/tests/VLGothic/LICENSE %{buildroot}/usr/share/package-licenses/seqdiag/af07a3a5218239724d3c4ad4f9e4746835129293
cp %{_builddir}/seqdiag-2.0.0/src/seqdiag/tests/VLGothic/LICENSE.en %{buildroot}/usr/share/package-licenses/seqdiag/25d28628ff8ea8da700469e7b9ce06e5faecfed0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/seqdiag

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/seqdiag/25d28628ff8ea8da700469e7b9ce06e5faecfed0
/usr/share/package-licenses/seqdiag/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/seqdiag/af07a3a5218239724d3c4ad4f9e4746835129293

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
