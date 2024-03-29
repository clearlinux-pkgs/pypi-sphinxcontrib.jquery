#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-sphinxcontrib.jquery
Version  : 4.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/de/f3/aa67467e051df70a6330fe7770894b3e4f09436dea6881ae0b4f3d87cad8/sphinxcontrib-jquery-4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/f3/aa67467e051df70a6330fe7770894b3e4f09436dea6881ae0b4f3d87cad8/sphinxcontrib-jquery-4.1.tar.gz
Summary  : Extension to include jQuery on newer Sphinx releases
Group    : Development/Tools
License  : 0BSD
Requires: pypi-sphinxcontrib.jquery-python = %{version}-%{release}
Requires: pypi-sphinxcontrib.jquery-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
======================
sphinxcontrib-jquery
======================
.. image:: https://img.shields.io/pypi/v/sphinxcontrib-jquery.svg
:target: https://pypi.org/project/sphinxcontrib-jquery/
:alt: Package on PyPI

%package python
Summary: python components for the pypi-sphinxcontrib.jquery package.
Group: Default
Requires: pypi-sphinxcontrib.jquery-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib.jquery package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib.jquery package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_jquery)
Requires: pypi(sphinx)
Provides: pypi(sphinxcontrib_jquery)

%description python3
python3 components for the pypi-sphinxcontrib.jquery package.


%prep
%setup -q -n sphinxcontrib-jquery-4.1
cd %{_builddir}/sphinxcontrib-jquery-4.1
pushd ..
cp -a sphinxcontrib-jquery-4.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695234242
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
