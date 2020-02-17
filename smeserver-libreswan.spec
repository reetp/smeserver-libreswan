%define name smeserver-libreswan
%define version 0.5
%define release 34
Summary: Plugin to enable IPSEC connections
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
URL: http://libreswan.org/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
Patch1: smeserver-libreswan-fix-masq-templates.patch
Patch2: smeserver-libreswan-move-logfile.patch
Patch3: smeserver-libreswan-add-debug-key.patch
Patch4: smeserver-libreswan-fix-rsa-id.patch
Patch5: smeserver-libreswan-fix-createlinks.patch
Patch6: smeserver-libreswan-ikev2-logrotate.patch
Patch7: smeserver-libreswan-add-certificates.patch
Patch8: smeserver-libreswan-modify-identifiers.patch
Patch9: smeserver-libreswan-modify-identifiers1.patch
Patch10: smeserver-libreswan-forceencaps-l2tpd.patch
Patch11: smeserver-libreswan-variable-network-interfaces.patch
Patch12: smeserver-libreswan-remove-obsoletes.patch
Patch13: smeserver-libreswan-add-reauth.patch
Patch14: smeserver-libreswan-check-l2tpd-status.patch
Patch15: smeserver-libreswan-include-l2tpd-rightsubnet.patch
Patch16: smeserver-libreswan-fix-xl2tpd-status-check.patch
Patch17: smeserver-libreswan-createlinks.patch
Patch18: smeserver-libreswan-modify-leftrightsubnet.patch

BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires:  e-smith-release >= 9.2
Requires:  libreswan >= 3.29
AutoReqProv: no

%description
Libreswan is a free software implementation of the most widely supported and standardised VPN protocol based on ("IPsec") and the Internet Key Exchange ("IKE")

%changelog
* Mon Feb 17 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-34.sme
- auto insert leftsourceip and subnet from internal interface
- Force right to have a value

* Tue Feb 14 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-33.sme
- update keyingtries
- update virtual-private

* Thu Jan 30 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-32.sme
- Fix xl2tpd status check

* Thu Oct 17 2019 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-31.sme
- Allow rightsubnet for xl2tpd in virtual_private
- Add check for empty virtual_private hosts

* Sun Oct 13 2019 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-30.sme
- Fix issue when there is no xl2tpd key

* Sat Aug 31 2019 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-29.sme
- Bump required Libreswan to 3.29
- add reauth option

* Thu Jun 21 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-28.sme
- Bump required Libreswan to 3.23
- Change forceencaps to encapsulation
- Remove obsolete nat_traversal
- Modify ipsec.conf for no rightsubnet in xl2tpd

* Tue Sep 19 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-27.sme
- Allow variable network interface names - Stefano Zamboni

* Thu Jun 15 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-26.sme
- add keep-alive option in main ipsec.conf
- add forceencaps option overall default and per connection
- small code tidy
- Add support for L2TPD

* Thu Jan 26 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-25.sme
 - Fix the ipsec.conf as well
 - remove automatic \@ in IDs - Fixes [SME: 9729]
 
* Thu Jan 26 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-24.sme
 - remove automatic \@ in IDs - Fixes [SME: 9729]
 - fix swapped left/right IDs in password file

* Wed Jan 25 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-23.sme
- Add the ability to use PEM/PKCS#12 certificates - fixes [SME: 9942]
- lots of code tidying

* Wed Dec 21 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-22.sme
- update logrotate completely now I realise it is symlinked
- remove UPDPort and add UPDPorts due to ipsec v2

* Wed Dec 21 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-21.sme
- add more variations for ike v1/2
- remove logrotate template
- add /etc/e-smith/events/logrotate/logfiles2timestamp/var/log/pluto.log
- Fix some log noise when first installed and still disabled

* Sat Apr 23 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-20.sme
- Fix typo in createlinks for sysctl.conf

* Mon Apr 04 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-19.sme
- Fix ID in ipsec.secrets if ID is set

* Thu Mar 24 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-18.sme
- Add debug db key to /etc/ipsec.conf
- Remove setting public/private keys as they won't affect unless templates are re-expanded
- Set xfrm_larval_drop drop correctly

* Tue Mar 22 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-17.sme
- Move pluto.log to /var/log/pluto
- bump libreswan requires version to 3.16
- regenerate masq template on ipsec-update
- change wiki location page
- add sysctl.conf template
- modify masq templates for ipsec status enabled/disabled
- only load ipsec.conf rather than *.conf to avoid loading v6neighbor-hole.conf

* Thu Mar 10 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-16.sme
- Fix masq templates for missing db entries on install

* Wed Mar 09 2016 JP Pialasse <tests@pialasse.com> 0.5-15.sme
- first import in SME buildsys

* Wed Feb 17 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-13
- Fix small typo in readme

* Fri Dec 04 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-12
- Add keyingtries
- Finally fix add issues using asynchronous

* Wed Dec 02 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-11
- Determine host IPtype - static or dynamic IP
- auto --up changed to exec
- Add checks for Left/Right ID in secrets file

* Tue Dec 01 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-10
- Allow dynamic addresses
- Add iptype
- disallow " in PSK passwords
- Revised logging messages

* Mon Nov 30 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-9
- Amended templates to allow for rsasig. Early cert settings removed

* Wed Nov 25 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-8
- Revised masq templates - disable on ipsec disable
- Template ipsec.secrets so Terry won't break it again
- Set requires e-smith >=9 and libreswan >=3.14

* Wed Nov 18 2015 John Crisp <jcrisp@safeandsoundit.co.uk> 0.5-7
- add 90adjustESP

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

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


echo "see https://wiki.contribs.org/Libreswan"

%postun
/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
/sbin/e-smith/expand-template /etc/inittab
/sbin/init q
