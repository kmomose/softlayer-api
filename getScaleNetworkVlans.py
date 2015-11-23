#!/usr/bin/env python3
#
# get autoscale group's network VLANs
#
# before execute, replace 'id' to your autoscale group id
#

import SoftLayer
import json

client = SoftLayer.Client()
vlans=client['Scale_Group'].getNetworkVlans(id=672761)

print vlans
