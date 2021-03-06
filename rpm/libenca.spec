# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       libenca

# >> macros
# << macros

Summary:    Extremely Naive Charset Analyser
Version:    1.14
Release:    1
Group:      System/Libraries
License:    GPLv2
URL:        https://gitorious.org/enca
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  recode-devel

%description
Extremely Naive Charset Analyser.

%package libenca0
Summary:    Extremely Naive Charset Analyser
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libenca0
Extremely Naive Charset Analyser - shared library files
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings.


%package devel
Summary:    Extremely Naive Charset Analyser
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Extremely Naive Charset Analyser - development files
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings.


%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%configure --disable-static \
--with-html-dir=/usr/share/doc/enca/html \
--with-librecode \
--with-libiconv \
--disable-rpath

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post libenca0 -p /sbin/ldconfig

%postun libenca0 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libexecdir}/enca/*
%{_datadir}/man/man1/*

%files libenca0
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
#%doc %{_datadir}/doc/enca/html/libenca/*
