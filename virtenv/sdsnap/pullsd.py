"""
 Pull slashdot feed
"""
#!/usr/bin/python
__author__ = 'dev'

import urllib.request as ur
import datetime as dt
import bs4 as beau
import textile as newhtml

STRLIST = ''
SDFEED = 'http://rss.slashdot.org/Slashdot/slashdotMain'
OPENURL = ur.urlopen(SDFEED)

#print("Status: {0}\nURL: {1}\n{2}".format(OPENURL.getcode(), OPENURL.geturl(), OPENURL.info()))
MYSOUP = beau.BeautifulSoup(OPENURL, 'lxml')
#print(MYSOUP.title.string)
#print("Total length is {0}\n".format(len(MYSOUP.text)))
DTMVAR = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

STRLIST = '[' + DTMVAR + ']From "' + MYSOUP.title.string + '":' + OPENURL.geturl() + '\n\n'
for SENTRY in MYSOUP.find_all("title"):
    if SENTRY.text not in ('Slashdot', 'Search Slashdot'):
        STRLIST = STRLIST + '* ' + SENTRY.text + '\n'

OUTHTML = newhtml.textile(STRLIST)
print(OUTHTML)
