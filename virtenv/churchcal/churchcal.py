"""
 Church Calendar Main Script
"""
#!/usr/bin/python3
__author__ = 'dev'

import re
import datetime as dt
import pymongo as mydb

#  Global Vars
MYRE = re.compile(r'([1-9]|1[012])/([1-9]|[12][0-9]|3[01])/\d{4}$')
LOCMDB = "192.168.0.21"

def ccopen():
    """ Open a connection """
    dbclient = mydb.MongoClient('mongodb://'+ LOCMDB)
    return dbclient

def ccclose(closedb):
    """ Close a connection """
    closedb.close()

def initenv(envset):
    """
     Initialize environment
      Days of Mass
      Mass hours
    """
    dbs = envset.list_database_names()
    if "churchcal" in dbs:
        print('Configured')
    else:
        cfgpost = [{"6": ["0830", "1030"]},
                   {"1": ["1900"]},
                   {"4": ["1900"]},
                   {"5": ["1700"]}]
        thedb = envset.churchcal
        thecfg = thedb.cfgdb
        thecfg.insert_many(cfgpost)

def getcfg(cfgfdb):
    """ Get the configuration """
    theres = None
    dbs = cfgfdb.churchcal
    colls = dbs.list_collection_names()
    if "cfgdb" in colls:
        thecoll = dbs.cfgdb
        theres = thecoll.find()
    return theres

def runquery(querydate, querydb):
    """ Run the query on the DB"""
    dbs = querydb.churchcal
    colls = dbs.list_collection_names()
    theres = None
    if "dcoll" in colls:
        thecoll = dbs.dcoll
        thequery = {querydate: {"$regex": "\\S*"}}
        theres = thecoll.find(thequery)
    return theres

def readrec(readdate, readdb):
    """ Read a record (date) """
    return runquery(readdate, readdb)

def postfnd(fnddate, fnddb):
    """ Validate post """
    postfndres = runquery(fnddate, fnddb)
    if postfndres.count != 0:
        return True
    else:
        return False

def writerec(writedate, writename, writedb):
    """ Write a record (date) """
    thewkday = dt.datetime(writedate).weekday()
    dbs = writedb.churchcal
    colls = dbs.list_collection_names()
    if "dcoll" in colls:
        if postfnd(writedate, writedb):
            print('Appending {0} for {1}'.format(writename, writedate))
        else:
            print('Writing record {1} for {0}'.format(writedate, writename))
    else:
        print('Writing initial record {0} for collection'.format(writedate))
        post = {writedate: writename}
        postcoll = dbs.dcoll
        postcoll.insert_one(post)

def datevalid(inpvar):
    """ Validate input """
    if MYRE.match(inpvar):
        return True
    return False

def inpdate():
    """ Get date """
    while True:
        thedate = input("Date [m/d/yyyy]: ")
        if datevalid(thedate):
            return thedate

if __name__ == '__main__':
    print('Run main function')
    bck = ccopen()
    initenv(bck)
    ccdate = inpdate()
    ccname = input("Name: ")
    if postfnd(ccdate, bck):
        print("Record found for {1}".format(ccdate))
    # else:
    #     writerec(ccdate, ccname, bck)
    ccclose(bck)
