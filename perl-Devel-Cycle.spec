#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Devel
%define	pnam	Cycle
Summary:	Devel::Cycle - Find memory cycles in objects
Summary(pl.UTF-8):	Devel::Cycle - znajdowanie cykli pamięci w obiektach
Name:		perl-Devel-Cycle
Version:	1.12
Release:	1
# same as perl 5 >= 5.8.2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/Devel-Cycle-%{version}.tar.gz
# Source0-md5:	3d9a963da87b17398fab9acbef63f277
URL:		http://search.cpan.org/dist/Devel-Cycle/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Suggests:	perl-PadWalker
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple developer's tool for finding circular references in
objects and other types of references. Because of Perl's
reference-count based memory management, circular references will
cause memory leaks.

Suggested packages:
 - perl-PadWalker - If the PadWalker module is installed, Devel::Cycle
   will also report cycles in code closures.

%description -l pl.UTF-8
Ten pakiet zawiera proste narzędzie dla programisty do znajdowania
zapętlonych odniesień w obiektach i innych rodzajach referencji. W
wyniku perlowego zarządzania pamięcią opartego o zliczanie odniesień
zapętlone odniesienia powodują wycieki pamięci.

Sugerowane pakiety:
 - perl-PadWalker - Po zainstalowaniu modułu PadWalker, Devel::Cycle
   będzie w stanie zgłaszać pętle w zagnieżdżonym kodzie.

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
%{perl_vendorlib}/Devel/Cycle.pm
%{_mandir}/man3/Devel::Cycle.3pm*
