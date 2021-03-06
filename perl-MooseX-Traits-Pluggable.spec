#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	MooseX
%define	pnam	Traits-Pluggable
Summary:	MooseX::Traits::Pluggable - an extension to MooseX::Traits
Summary(pl.UTF-8):	MooseX::Traits::Pluggable - rozszerzenie dla MooseX::Traits
Name:		perl-MooseX-Traits-Pluggable
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d7af140b575c7b1e32044e2876f6401
URL:		http://search.cpan.org/dist/MooseX-Traits-Pluggable/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-MOP >= 0.84
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Moose
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-namespace-autoclean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
See MooseX::Traits for usage information.

Adds support for class precedence search for traits and some extra
attributes, described below.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/MooseX/Traits
%{perl_vendorlib}/MooseX/Traits/*.pm
%{_mandir}/man3/*
