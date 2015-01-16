%define name smeserver-libreswan
%define version 0.2
%define release 1
Summary: Plugin to enable IPSEC connections
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
URL: http://libreswan.org/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires:  e-smith-release >= 8.0
Requires:  libreswan >= 3.12
AutoReqProv: no

%description
Libreswan is a free software implementation of the most widely supported and standarized VPN protocol based on ("IPsec") and the Internet Key Exchange ("IKE")

%changelog

* Fri Jan 16 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.2-1
- remove rc.local modifications
- add /etc/sysctl.conf patches

* Thu Jan 15 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-1
- initial release

%prep
%setup

%build
perl createlinks

mkdir -p          root/etc/e-smith/db/configuration/defaults/ipsec
echo "service"  > root/etc/e-smith/db/configuration/defaults/ipsec/type
echo "disabled"  > root/etc/e-smith/db/configuration/defaults/ipsec/status


%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist


%clean
cd ..
rm -rf %{name}-%{version}

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre
%preun
%post
/sbin/e-smith/expand-template /etc/ipsec.conf
/sbin/e-smith/expand-template /etc/ipsec.d/ipsec.conf
/sbin/e-smith/expand-template /etc/ipsec.d/ipsecrets.conf
/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
/sbin/e-smith/expand-template /etc/sysctl.conf

echo "see http://wiki.contribs.org/IPSEC"

%postun
/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
/sbin/e-smith/expand-template /etc/inittab
/sbin/init q
