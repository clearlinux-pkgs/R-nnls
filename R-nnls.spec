#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-nnls
Version  : 1.4
Release  : 9
URL      : https://cran.r-project.org/src/contrib/nnls_1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/nnls_1.4.tar.gz
Summary  : The Lawson-Hanson algorithm for non-negative least squares
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-nnls-lib = %{version}-%{release}
BuildRequires : R-quadprog
BuildRequires : buildreq-R

%description
algorithm for non-negative least squares (NNLS).  Also allows
        the combination of non-negative and non-positive constraints.

%package lib
Summary: lib components for the R-nnls package.
Group: Libraries

%description lib
lib components for the R-nnls package.


%prep
%setup -q -c -n nnls

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552757604

%install
export SOURCE_DATE_EPOCH=1552757604
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nnls
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nnls
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nnls
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  nnls || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/nnls/COPYRIGHTS
/usr/lib64/R/library/nnls/DESCRIPTION
/usr/lib64/R/library/nnls/INDEX
/usr/lib64/R/library/nnls/Meta/Rd.rds
/usr/lib64/R/library/nnls/Meta/features.rds
/usr/lib64/R/library/nnls/Meta/hsearch.rds
/usr/lib64/R/library/nnls/Meta/links.rds
/usr/lib64/R/library/nnls/Meta/nsInfo.rds
/usr/lib64/R/library/nnls/Meta/package.rds
/usr/lib64/R/library/nnls/NAMESPACE
/usr/lib64/R/library/nnls/R/nnls
/usr/lib64/R/library/nnls/R/nnls.rdb
/usr/lib64/R/library/nnls/R/nnls.rdx
/usr/lib64/R/library/nnls/help/AnIndex
/usr/lib64/R/library/nnls/help/aliases.rds
/usr/lib64/R/library/nnls/help/nnls.rdb
/usr/lib64/R/library/nnls/help/nnls.rdx
/usr/lib64/R/library/nnls/help/paths.rds
/usr/lib64/R/library/nnls/html/00Index.html
/usr/lib64/R/library/nnls/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/nnls/libs/nnls.so
/usr/lib64/R/library/nnls/libs/nnls.so.avx2
/usr/lib64/R/library/nnls/libs/nnls.so.avx512
