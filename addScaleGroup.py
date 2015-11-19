#!/usr/bin/env python3
#
# create an autoscale group
#
# tips:
# 1) networkVlanID can be found with Account.getSubnets() method
# 2) If networkVlanID is specified, the value for minimumMemberCount needs to be care.
#     The API can allow this setting to be 0, but softlayer portal does not.
#

import SoftLayer
import pprint
client = SoftLayer.Client()

try:

	scalegroup=client['Scale_Group'].createObject({
	   'accountId': XXXXXX,
	   'balancedTerminationFlag': False,
	   'cooldown': 60,
	   'networkVlanCount': 1,
	   'networkVlans':[{'networkVlanId': XXXXXXX}],
	   'maximumMemberCount': 1,
	   'minimumMemberCount': 0,
	   'name': 'ASG-CHN1',
	   'regionalGroupId': 743,
	   'status': {'id': 4, 'keyName': 'SUSPENDED', 'name': 'Suspended'},
	   'suspendedFlag': True,
	   'terminationPolicyId': 1,
	   'virtualGuestMemberTemplate': {'accountId': XXXXXX,
                                 'blockDevices': [{'bootableFlag': '',
                                                   'device': '0',
                                                   'diskImage': {'capacity': 25},}],
                                 'datacenter': {'name': 'che01'},
                                 'dedicatedAccountHostOnlyFlag': '',
                                 'domain': 'XXXXXXXX.softlayer.com',
                                 'hostname': 'as',
                                 'hourlyBillingFlag': True,
                                 'localDiskFlag': True,
                                 'maxCpu': '',
                                 'maxMemory': 1024,
                                 'operatingSystemReferenceCode': 'CENTOS_LATEST',
                                 'postInstallScriptUri': 'https://XXX.XXX.XXX.XXX/dummy.txt',
                                 'privateNetworkOnlyFlag': True,
                                 'startCpus': 1}
})
	
except SoftLayer.SoftLayerAPIError as e:
       pprint.pprint("Unable to execute faultCode=%s, faultString=%s"
                            % (e.faultCode, e.faultString))
       exit(1)

pprint.pprint(scalegroup)

