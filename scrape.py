###################################################
# fccedits
#
# Scrape Wikipedia for edits made by FCC IP's
#
# Author: @bltjetpack, github.com/sa7mon
# Created: 12/14/17
#
####################################################

import requests
from netaddr import *


ipset = IPSet()

ipset.add('192.104.54.0/24') # s/o to @Viss for finding

for ip in ipset:
	print ip