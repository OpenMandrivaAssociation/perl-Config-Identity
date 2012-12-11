%define upstream_name    Config-Identity
%define upstream_version 0.0016

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Load (and optionally decrypt via GnuPG) user/pass identity information
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Which)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)

BuildArch:	noarch

%description
Config::Identity is a tool for loadiing (and optionally decrypting via
GnuPG) user/pass identity information

For GitHub API access, an identity is a 'login'/'token' pair

For PAUSE access, an identity is a 'user'/'password' pair

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.1.600-2mdv2011.0
+ Revision: 653558
- rebuild for updated spec-helper

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.1.600-1mdv2011.0
+ Revision: 572933
- fixing buildrequires:
- adding missing buildrequires:
- adding missing buildrequires:
- import perl-Config-Identity

