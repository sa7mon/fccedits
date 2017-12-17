#!/usr/bin/env python

#############
#
# fccedits - Scrape Wikipedia for edits made by FCC IP's
#
# Author: @bltjetpack, github.com/sa7mon
# Additions? : @Suprn8, github.com/Caprico1
# Created: 12/14/17
# License: Creative Commons (CC BY-NC-SA 4.0))
#
#############

from netaddr import *
import requests
from bs4 import BeautifulSoup
from sys import argv, exit

address = '192.104.54.0/24'     # default to FCC's IP range. Shout out to @Viss for finding

'''------------------Check for user input --------------------------------------'''

if len(argv) == 2:

    if argv[1] == '-h' or argv[1] == '--help':
        print()
        print('Search for wikipedia edits from a specific IP or range of IP\'s.')
        print()
        print('Defaults to IP range: 192.104.54.0/24    # FCC registered IP\'s. Thanks @Viss')
        print()
        print('------------------------------------------------------------')
        print('Usage: python scape.py <IP address/IP address with subnet>')
        print('Example: python scape.py 192.104.54.0/24')
        print('------------------------------------------------------------')
        exit()
    else:
        address = argv[1]


ipset = IPSet()

ipset.add(address)

for ip in ipset:
    print("Checking ip: " + str(ip) + "...", end='', flush=True)

    editsPage = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/Special:Contributions/' + str(ip)).text,
                              "html.parser")

    editList = editsPage.find("ul", class_="mw-contributions-list")
    if editList is None:
        print("No edits found from this IP")
        continue

    edits = editList.find_all("li")

    print("Found " + str(len(edits)) + " edits from this IP:\n")

    for edit in edits:
        diff = ""
        posDiff = edit.find(
            class_="mw-plusminus-pos")  # Diff elements can be either span's or strong's. Just look for class.
        negDiff = edit.find(class_="mw-plusminus-neg")
        neuDiff = edit.find(class_="mw-plusminus-null")
        if posDiff is not None:
            diff = posDiff.text
        elif negDiff is not None:
            diff = negDiff.text
        elif neuDiff is not None:
            diff = neuDiff.text
        articleTitle = edit.find("a", class_="mw-contributions-title").text
        diffLink = edit.find("a", class_="mw-changeslist-diff").get("href")

        print("   " + diff + "   " + articleTitle + "   " + "https://en.wikipedia.org" + diffLink)
