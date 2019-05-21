"""
 Church Calendar Main Script
"""
#!/usr/bin/python3
__author__ = 'dev'

import re
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
        thedb = envset['churchcal']
        thecfg = thedb['cfgdb']
        thecfg.insert_many(cfgpost)

def readrec(readdate, readname, readdb):
    """ Read a record (date) """
    dbs = readdb.list_database_names()
    if "dcoll" in dbs:
        thedb = readdb['churchcal']
        thedb.dcoll.find({readdate})
        while True:
            thedb.dcoll.next()
        return True
    else:
        return False

def postvalid():
    """ Validate post """
    return True

def writerec(writedate, writename, writedb):
    """ Write a record (date) """
    print("{0} {1}".format(writedate, writename))
    dbs = writedb.list_database_names()
    if "dcoll" in dbs:
        print('something')
    else:
        post = {writedate: writename}
        thedb = writedb['churchcal']
        postcoll = thedb['dcoll']
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
    if readrec(ccdate, ccname, bck):
        print("Record {0} already exists on {1}".format(ccname, ccdate))
    # else:
    #     writerec(ccdate, ccname, bck)
    ccclose(bck)
