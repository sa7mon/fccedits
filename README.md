# fccedits
Scrape Wikipedia for edits made by FCC IP's

## To use

1. (Optionally) Create virtualenv
2. `pip install -r requirements.txt`
3.  `python3 fccedits.py`

### Optional Arguments

1. `python3 fccedits.py --help or -h`
2. `python3 fccedits.py <IP Address/Range>`

## Scans
* [Thu Dec 14 20:49:52 2017 -0600](https://github.com/sa7mon/fccedits/blob/master/scans/12-14-17_20-49.txt)

## Notes
* This script was thrown together in about 30 minutes just to get some quick results. The code is messy and inefficient, probably but works.
* Please don't hammer Wikipedia's servers with lots of requests. This script was intentionally written in a non-threaded way to limit the load on their servers. 
* Issues are welcomed, but contributions are appreciated

## License
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International [(CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
