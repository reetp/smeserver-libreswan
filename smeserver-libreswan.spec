%define name smeserver-libreswan
%define version 0.5
%define release 6
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
* Tue Nov 17 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-6
- more update to masq firewalls - change -p 50 to -p ESP

* Tue Nov 17 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-5
- update masq firewall rules
- document clean up

* Wed May 27 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-4
- set dpd actions off if ipsec is 'add'
- add salifetime key and rename ikelifetime and keylife
- change defaults for salifetime and ikelifetime
- add in rsasig support

* Wed Apr 22 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-3
- change default ike from aes-sha to aes-sha1

* Tue Mar 24 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-2
- More minor fixes - should work OK with xl2tpd

* Thu Mar 19 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-1
- Remove templates2expand and added to createlinks
- modified ipsec.secret template
- various other fixes

* Fri Mar 13 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.4-5
- Big changes again - now have PreviousState to detect changes
- Createlinks to S10 to run after expand-templates

* Thu Mar 5 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.4-4
- Changed lots. Removed sysctl.conf template
- Changed firewall template

* Tue Mar 3 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.4-3
- Load of code tidying and prep from xl2tpd

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
/sbin/e-smith/expand-template /etc/inittab
/sbin/init q


echo "see http://wiki.contribs.org/IPSEC"

%postun
/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
/sbin/e-smith/expand-template /etc/inittab
/sbin/init q
