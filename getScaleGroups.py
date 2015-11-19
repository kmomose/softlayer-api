#!/usr/bin/env python3
#
# get autoscale groups and extract the name and id
#
import SoftLayer
import json

client = SoftLayer.Client()
scalegroups=client['Account'].getScaleGroups()

enc = json.dumps(scalegroups,indent=4)
print enc

dec = json.loads(enc)

try:
	cnt=0
	while True: 
		print dec[cnt]['name'],dec[cnt]['id']
		cnt = cnt+1
except IndexError:
	print 'end of the list'

