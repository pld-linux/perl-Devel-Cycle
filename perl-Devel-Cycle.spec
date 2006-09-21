#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Cycle
Summary:	Devel::Cycle - Find memory cycles in objects
Name:		perl-Devel-Cycle
Version:	1.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/L/LD/LDS/Devel-Cycle-%{version}.tar.gz
# Source0-md5:	7d8a1e0ca88f8a66bb1344a217d21f1c
URL:		http://search.cpan.org/dist/Devel-Cycle/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple developer's tool for finding circular references in
objects and other types of references. Because of Perl's
reference-count based memory management, circular references will
cause memory leaks.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Devel/*.pm
%{_mandir}/man3/*
