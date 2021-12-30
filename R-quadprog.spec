#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-quadprog
Version  : 1.5.8
Release  : 55
URL      : https://cran.r-project.org/src/contrib/quadprog_1.5-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/quadprog_1.5-8.tar.gz
Summary  : Functions to Solve Quadratic Programming Problems
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-quadprog-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
solving quadratic programming problems.

%package lib
Summary: lib components for the R-quadprog package.
Group: Libraries

%description lib
lib components for the R-quadprog package.


%prep
%setup -q -c -n quadprog
cd %{_builddir}/quadprog

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589512100

%install
export SOURCE_DATE_EPOCH=1589512100
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library quadprog
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library quadprog
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library quadprog
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc quadprog || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/quadprog/DESCRIPTION
/usr/lib64/R/library/quadprog/INDEX
/usr/lib64/R/library/quadprog/Meta/Rd.rds
/usr/lib64/R/library/quadprog/Meta/features.rds
/usr/lib64/R/library/quadprog/Meta/hsearch.rds
/usr/lib64/R/library/quadprog/Meta/links.rds
/usr/lib64/R/library/quadprog/Meta/nsInfo.rds
/usr/lib64/R/library/quadprog/Meta/package.rds
/usr/lib64/R/library/quadprog/NAMESPACE
/usr/lib64/R/library/quadprog/R/quadprog
/usr/lib64/R/library/quadprog/R/quadprog.rdb
/usr/lib64/R/library/quadprog/R/quadprog.rdx
/usr/lib64/R/library/quadprog/help/AnIndex
/usr/lib64/R/library/quadprog/help/aliases.rds
/usr/lib64/R/library/quadprog/help/paths.rds
/usr/lib64/R/library/quadprog/help/quadprog.rdb
/usr/lib64/R/library/quadprog/help/quadprog.rdx
/usr/lib64/R/library/quadprog/html/00Index.html
/usr/lib64/R/library/quadprog/html/R.css
/usr/lib64/R/library/quadprog/tests/Gwen.R
/usr/lib64/R/library/quadprog/tests/Gwen.Rout.save
/usr/lib64/R/library/quadprog/tests/TalbotKatz.R
/usr/lib64/R/library/quadprog/tests/TalbotKatz.Rout.save
/usr/lib64/R/library/quadprog/tests/bug.RData
/usr/lib64/R/library/quadprog/tests/test1.R
/usr/lib64/R/library/quadprog/tests/test1.Rout.save
/usr/lib64/R/library/quadprog/tests/test2.R
/usr/lib64/R/library/quadprog/tests/test2.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/quadprog/libs/quadprog.so
/usr/lib64/R/library/quadprog/libs/quadprog.so.avx2
/usr/lib64/R/library/quadprog/libs/quadprog.so.avx512
