#!/usr/bin/env python3
#
# modify the network vlan associated with paticuler autoscale group
#
# Tips:
# 1) networkVlanID can be found with Account.getSubnets() method
# 2) scaleGroupID can be found wiht Account.getScaleGroups() method
#

import SoftLayer
import pprint
client = SoftLayer.Client()

try:

	result=client['Scale_Network_Vlan'].createObject({
                                 'networkVlanId': XXXXXX,
		 'scaleGroupId': XXXXXX
})
	
except SoftLayer.SoftLayerAPIError as e:
       pprint.pprint("Unable to execute faultCode=%s, faultString=%s"
                            % (e.faultCode, e.faultString))
       exit(1)

pprint.pprint(result)

