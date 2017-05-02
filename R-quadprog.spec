#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-quadprog
Version  : 1.5.5
Release  : 7
URL      : https://cran.r-project.org/src/contrib/quadprog_1.5-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/quadprog_1.5-5.tar.gz
Summary  : Functions to solve Quadratic Programming Problems.
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0
Requires: R-quadprog-lib
BuildRequires : clr-R-helpers

%description
This is an R port of the quadprog package version 1.2 of
Berwin A. Turlach <berwin.turlach@anu.edu.au> which can be found
at http://wilton.anu.edu.au/%7Eberwin/software/quadprog.html. An older
version can also be found in the statlib archive.

%package lib
Summary: lib components for the R-quadprog package.
Group: Libraries

%description lib
lib components for the R-quadprog package.


%prep
%setup -q -c -n quadprog

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492802643

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492802643
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library quadprog
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library quadprog


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
/usr/lib64/R/library/quadprog/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/quadprog/libs/quadprog.so
