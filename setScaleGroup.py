#!/usr/bin/env python3
#
import SoftLayer
import pprint
client = SoftLayer.Client()

try:

	result=client['Scale_Group'].editObject({'maximumMemberCount': 2,'minimumMemberCount': 0,'cooldown':60},id=656259)


except SoftLayer.SoftLayerAPIError as e:
       pprint.pprint("Unable to execute faultCode=%s, faultString=%s"
                            % (e.faultCode, e.faultString))
       exit(1)

pprint.pprint(result)

