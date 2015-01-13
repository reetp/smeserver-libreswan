%define name smeserver-libreswan
%define version 0.1
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
BuildRequires: e-smith-devtools >= 2.0
Requires:  e-smith-release >= 8.0
Requires:  libreswan >= 3.12
AutoReqProv: no

%description
Libreswan is a free software implementation of the most widely supported and standarized VPN protocol based on ("IPsec") and the Internet Key Exchange ("IKE")

%changelog

* Tue Jan 13 2015 John Crsip <jcrisp@safeandsoundit.co.uk> 0.1-1
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
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
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
/sbin/e-smith/expand-template /etc/ipsec.conf
/sbin/e-smith/expand-template /etc/rc.d/init.d/masq

/bin/rm -f /etc/cron.daily/hylafax
/bin/touch /var/spool/hylafax/etc/xferfaxlog
echo "see http://wiki.contribs.org/IPSEC"

%postun
/sbin/e-smith/expand-template /etc/inittab
/sbin/init q

