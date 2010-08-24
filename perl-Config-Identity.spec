%define upstream_name    Config-Identity
%define upstream_version 0.0016

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Load (and optionally decrypt via GnuPG) user/pass identity information
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Which)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Most)
BuildRequires: perl(Test::Warn)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Config::Identity is a tool for loadiing (and optionally decrypting via
GnuPG) user/pass identity information

For GitHub API access, an identity is a 'login'/'token' pair

For PAUSE access, an identity is a 'user'/'password' pair

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


