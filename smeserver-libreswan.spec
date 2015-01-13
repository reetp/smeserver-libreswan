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

#all below need to be create in the src.rpm with folder&file
#see https://github.com/stephdl/smeserver-sogo/tree/sme9/root/etc/e-smith/db/configuration/defaults/sogod
#mkdir -p          root/etc/e-smith/db/configuration/defaults/ipsec
#echo "service"  > root/etc/e-smith/db/configuration/defaults/ipsec/type
#echo "disabled"  > root/etc/e-smith/db/configuration/defaults/ipsec/status


%install
#here you are doing a 'cd root', so all rpm files have to be in a root folder
#see https://github.com/stephdl/smeserver-nfs, it is a good pratice
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
echo "%doc COPYING" >> %{name}-%{version}-filelist
#here you can define permissions and ownership if needed (if you want a script can be executable)
#see http://wiki.contribs.org/.spec_file_notes
#and specially http://wiki.contribs.org/.spec_file_notes#.25install

%clean
cd ..
rm -rf %{name}-%{version}

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre
%preun
%post
#here you have to create an event in the createlink, nothing in %post & postun
#see http://wiki.contribs.org/Createlinks_example_script & http://wiki.contribs.org/Esmith::Build::CreateLinks
#all expand, creation of service has to be done with the createlinks
#/sbin/e-smith/expand-template /etc/ipsec.conf
#/sbin/e-smith/expand-template /etc/ipsec.d/ipsec.conf
#/sbin/e-smith/expand-template /etc/ipsec.d/ipsecrets.conf
#/sbin/e-smith/expand-template /etc/ipsec.conf
#/sbin/e-smith/expand-template /etc/rc.d/init.d/masq

#/bin/rm -f /etc/cron.daily/hylafax
#/bin/touch /var/spool/hylafax/etc/xferfaxlog

#well that it is ok, you can give instructions
echo "see http://wiki.contribs.org/IPSEC"

%postun
#/sbin/e-smith/expand-template /etc/inittab
#/sbin/init q

