{
use strict;
use warnings;

use esmith::ConfigDB;
use esmith::IpsecDB;
use Net::IPv4Addr qw(ipv4_in_network ipv4_parse);
use esmith::util::network qw(isValidIP);

my $configDB = esmith::ConfigDB->open_ro;
my $ipsecDB = esmith::IpsecDB->open_ro;

my @connections = $ipsecDB->connections;

foreach my $ipsec (@connections)

{
#first we verify if IPSec is enabled for the connection
my $ipsecstatus = $ipsec->prop("Status") || "disabled";


#Then we retrieve the name of the ebay
my $key = $ibay->key;

#start to count
# my $count = '0';


if (($nfsstatus eq 'enabled'))
{

# write the configuration
{
my @IP = split /[:]/, $nfsclient;
foreach my $IP (@IP)
{
#now we look about exports options
my $nfsrw = $ibay->prop("NfsRW") || 'ro';
my $nfssync = $ibay->prop("NfsSync") || 'sync';
my $wdelay = $ibay->prop("NfsWdelay") || 'wdelay';
my $nfssquash = $ibay->prop("NfsSquash") || 'root_squash';
my $anonuid = $ibay->prop("NfsAnonUid") || '';
my $anongid = $ibay->prop("NfsAnonGid") || '';
my $secure = $ibay->prop("NfsSecure") || 'secure';
my $hide = $ibay->prop("NfsHide") || 'nohide';
my $nfs_options = $hide . ',' . $nfssync . ',' . $wdelay;

if (isValidIP($IP) && (grep { ipv4_in_network($_, $IP) } @localAccess) )
{
$nfs_options = $nfs_options . ',' . "anonuid=$anonuid"
if (($anonuid =~ m/(\d+)/) && ($anonuid !~ m/(\D+)/));
$nfs_options = $nfs_options . ',' . "anongid=$anongid"
if (($anongid =~ m/(\d+)/) && ($anongid !~ m/(\D+)/));
$nfs_options = $nfs_options . ',' . $nfsrw;
$nfs_options = $nfs_options . ',' . $nfssquash;
$nfs_options = $nfs_options . ',' . $secure;
$OUT .= "\n/home/e-smith/files/ibays/$key/files " if ($count == '0');
$OUT .= " $IP($nfs_options)";
$count++
}
if ($IP eq 'local')
{
$nfsrw = 'ro';
$nfssquash = 'root_squash';
$secure = 'secure';
$nfs_options = $nfs_options . ',' . $nfsrw;
$nfs_options = $nfs_options . ',' . $nfssquash;
$nfs_options = $nfs_options . ',' . $secure;
foreach my $localAccess (@localAccess)
{
$OUT .= "\n/home/e-smith/files/ibays/$key/files " if ($count == '0');
$OUT .= " $localAccess($nfs_options)" if $localAccess !~ '127.0.0.1';
$count++
}
}
}
}
}
}
}
