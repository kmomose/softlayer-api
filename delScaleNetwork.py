#!/usr/bin/env python3
#
# delete autoscale network VLAN
#
# before execute, replace 'id' to your target vlan id 
#   ( which can get via Scale_Group.getNetworkVlans method)
#

import SoftLayer
import pprint
client = SoftLayer.Client()

try:

	result=client['Scale_Network_Vlan'].deleteObject(id=86705)
	
except SoftLayer.SoftLayerAPIError as e:
       pprint.pprint("Unable to execute faultCode=%s, faultString=%s"
                            % (e.faultCode, e.faultString))
       exit(1)

pprint.pprint(result)

