###################################################
# fccedits
#
# Scrape Wikipedia for edits made by FCC IP's
#
# Author: @bltjetpack, github.com/sa7mon
# Created: 12/14/17
#
####################################################

from netaddr import *
import requests
from bs4 import BeautifulSoup

ipset = IPSet()

ipset.add('192.104.54.0/24') # s/o to @Viss for finding

for ip in ipset:
	# https://en.wikipedia.org/wiki/Special:Contributions/119.18.13.17
	print("Checking ip: " + str(ip) + "...", end='', flush=True)

	editsPage = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/Special:Contributions/' + str(ip)).text, "html.parser")

	editList = editsPage.find("ul", class_="mw-contributions-list")
	if editList is None:
		print("No edits found from this IP")
		continue

	edits = editList.find_all("li")
	
	print("Found " + str(len(edits)) + " edits from this IP:")

	for edit in edits:
		articleTitle = edit.find("a", class_="mw-contributions-title").text
		diffLink = edit.find("a", class_="mw-changeslist-diff").get("href")

		print("   " + articleTitle + " - " + "https://en.wikipedia.org" + diffLink)







