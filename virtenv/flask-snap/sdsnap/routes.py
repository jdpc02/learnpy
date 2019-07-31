import pathlib
from flask import render_template
from sdsnap import app
import urllib.request as ur
import datetime as dt
import bs4 as beau
import textile as newhtml
import os

def gensdidx():
    strlist = ''
    chkurl = True
    sdfeed = 'http://rss.slashdot.org/Slashdot/slashdotMain'
    try:
        openurl = ur.urlopen(sdfeed)
    except:
        chkurl = False
    if chkurl:
        mysoup = beau.BeautifulSoup(openurl, 'lxml')
        dtmvar = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        strlist = '[' + dtmvar + '] From "' + mysoup.title.string + '":' + openurl.geturl() + '\n\n'
        for sentry in mysoup.find_all("title"):
            if sentry.text not in ('Slashdot', 'Search Slashdot'):
                strlist = strlist + '* ' + sentry.text + '\n'
    else:
        strlist = 'Unable to reach ' + sdfeed + '\n'

    outhtml = newhtml.textile(strlist)
    thepath = pathlib.Path(__file__).parent.resolve()
    path = os.path.join(thepath, 'templates\\index.html')
    with open(path, 'w') as outfile:
        print(outhtml, file=outfile)
    outfile.close()
    return

gensdidx()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', response=gensdidx())
 