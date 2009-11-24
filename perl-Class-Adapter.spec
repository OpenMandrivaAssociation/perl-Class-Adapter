%define upstream_name    Class-Adapter
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Generate Class::Adapter classes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*
