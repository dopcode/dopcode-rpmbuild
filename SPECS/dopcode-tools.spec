%define alias tools

%define debug_package %{nil}

Name:           dopcode-tools
Version:        1.0.0
Release:        1%{?dist}
Summary:        Tools for dopcode

 
Group:          dopcode
License:        dopcode License
URL:            http://www.dopcode.org
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  /bin/rm, /bin/mkdir, /bin/cp, /bin/tar
Requires:       /bin/bash

%description
Tools for dopcode
 
%prep
%setup -q
 
%build

%install
cp -a $RPM_BUILD_DIR/%{name}-%{version}/dopcode $RPM_BUILD_ROOT

%clean

%files
%defattr(-,dopcode,dopcode,-)
%config /dopcode/%{alias}
%config %dir /dopcode/%{name}-%{version}/
%attr(0755,dopcode,dopcode)
%config /dopcode/%{name}-%{version}/*.sh
%config /dopcode/%{name}-%{version}/logs

%pre

%post
chmod a+x /dopcode/%{alias}/*.sh

%preun

%postun

%changelog
* Sat Jun 27 2020 dospluto<dospluto@gmail.com> - 1.0.0-1
- Initial RPM
