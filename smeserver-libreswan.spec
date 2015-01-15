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
BuildRequires: e-smith-devtools
Requires:  e-smith-release >= 8.0
Requires:  libreswan >= 3.12
AutoReqProv: no

%description
Libreswan is a free software implementation of the most widely supported and standarized VPN protocol based on ("IPsec") and the Internet Key Exchange ("IKE")

%changelog

* Tue Jan 13 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-1
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

echo "
# Correct ICMP Redirect issues with LibreSwan\n
for each in /proc/sys/net/ipv4/conf/*; do\n
    echo 0 > $each/accept_redirects\n
    echo 0 > $each/send_redirects\n
    echo 0 > $each/rp_filter\n
    done\n
    echo 1 >  /proc/sys/net/core/xfrm_larval_drop
#  End ICMP redirect\n" >> rc.local

echo "see http://wiki.contribs.org/IPSEC"

%postun
sed --in-place=.bak '/# Correct ICMP/,/# End ICMP/d' rc.local
echo "rc.local backed up to rc.local.bak"
/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
/sbin/e-smith/expand-template /etc/inittab
/sbin/init q
