#!/usr/bin/env python3
#
#get subnet information and extract networkVlanId
#
#
import SoftLayer
import json
import pprint

client = SoftLayer.Client()

result=client['Account'].getSubnets()
#pprint.pprint(result)

enc=json.dumps(result,indent=4)
dec=json.loads(enc)
print enc
cnt=0
while cnt < len(dec):
	print dec[cnt]['addressSpace'],dec[cnt]['subnetType'],dec[cnt]['networkIdentifier'],dec[cnt]['networkVlanId']
	cnt=cnt+1

