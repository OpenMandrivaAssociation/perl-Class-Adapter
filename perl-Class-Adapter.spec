
%define realname   Class-Adapter
%define version    1.05
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Generate Class::Adapter classes
Source:     http://www.cpan.org/modules/by-module/Class/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

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


