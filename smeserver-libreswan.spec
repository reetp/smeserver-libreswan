%define name smeserver-libreswan
%define version 0.4
%define release 2
Summary: Plugin to enable IPSEC connections
Name: %{name}
Version: %{version}
Release: %{release}
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

* Fri Feb 27 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.4-2
- Update action script and allow for system not in gateway mode
- add ike and phase2alg db settings

* Tue Feb 24 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.4-1
- New ipsec-action script
- Numerous template changes

* Fri Jan 16 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.3-1
- remove debugging lines
- remove expand templates from spec file
- add status check for ipsec.conf
- add comment to masq template
- updated db defaults
- ipsec.conf not expanded on install
- missed auto=start

* Fri Jan 16 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.2-1
- remove rc.local modifications
- add /etc/sysctl.conf patches

* Thu Jan 15 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-1
- initial release

%prep
%setup

%build
perl createlinks

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

/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
/sbin/e-smith/expand-template /etc/sysctl.conf

echo "see http://wiki.contribs.org/IPSEC"

%postun
/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
/sbin/e-smith/expand-template /etc/inittab
/sbin/init q
