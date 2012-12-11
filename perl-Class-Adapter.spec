%define upstream_name    Class-Adapter
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Generate Class::Adapter classes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
The 'Class::Adapter' class is intended as an abstract base class for
creating any sort of class or object that follows the _Adapter_ pattern.

What is an Adapter?
    The term _Adapter_ refers to a _"Design Pattern"_ of the same name,
    from the famous _"Gang of Four"_ book _"Design Patterns"_. Although
    their original implementation was designed for Java and similar
    single-inheritance strictly-typed langauge, the situation for which it
    applies is still valid.

    An _Adapter_ in this Perl sense of the term is when a class is created
    to achieve by composition (objects containing other object) something
    that can't be achieved by inheritance (sub-classing).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.80.0-2mdv2011.0
+ Revision: 657396
- rebuild for updated spec-helper

* Sat Mar 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.80.0-1
+ Revision: 648566
- update to new version 1.08

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 536131
- update to 1.07

* Tue Nov 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.1
+ Revision: 469432
- update to 1.06

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 401707
- rebuild using %%perl_convert_version
- fixed license field

* Tue Nov 11 2008 Jérôme Quelin <jquelin@mandriva.org> 1.05-1mdv2009.1
+ Revision: 302309
- import perl-Class-Adapter


* Tue Nov 11 2008 cpan2dist 1.05-1mdv
- initial mdv release, generated with cpan2dist

