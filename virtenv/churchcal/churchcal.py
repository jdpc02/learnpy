"""
 Church Calendar Main Script
"""
#!/usr/bin/python3
__author__ = 'dev'

import re
import sys
import datetime as dt
import pymongo as mydb

#  Global Vars
MYRE = re.compile(r'([1-9]|1[012])/([1-9]|[12][0-9]|3[01])/\d{4}$')
LOCMDB = "192.168.0.21"

def ccopen():
    """ Open a connection """
    dbdelay = 10
    dbclient = mydb.MongoClient('mongodb://'+ LOCMDB, serverSelectionTimeoutMS=dbdelay)
    try:
        dbclient.server_info()
    except mydb.errors.ServerSelectionTimeoutError as err:
        print(err)
        return None
    return dbclient

def ccclose(closedb):
    """ Close a connection """
    closedb.close()

def initenv(envset):
    """
     Initialize environment
      Days of Mass
       0 - Monday
       1 - Tuesday
       2 - Wednesday
       3 - Thursday
       4 - Friday
       5 - Saturday
       6 - Sunday
      Mass hours
       24-hour notation
    """
    dbs = envset.list_database_names()
    if "churchcal" in dbs:
        print('Configured')
    else:
        cfgpost = [
            {
                "weekday": "6",
                "hours": {
                    "1030": {
                        "Name1": ""
                    },
                    "0830": {
                        "Name1": ""
                    }
                }
            },
            {
                "weekday": "1",
                "hours": {
                    "1900": {
                        "Name1": "",
                        "Name2": "",
                        "Name3": "",
                        "Name4": "",
                        "Name5": ""
                    }
                }
            },
            {
                "weekday": "4",
                "hours": {
                    "1900": {
                        "Name1": "",
                        "Name2": "",
                        "Name3": "",
                        "Name4": "",
                        "Name5": ""
                    }
                }
            },
            {
                "weekday": "5",
                "hours": {
                    "1700": {
                        "Name1": "",
                        "Name2": "",
                        "Name3": "",
                        "Name4": "",
                        "Name5": ""
                    }
                }
            }
        ]
        thedb = envset.churchcal
        thecfg = thedb.cfgdb
        thecfg.insert_many(cfgpost)

def getcfg(cfgfdb, cfgdate):
    """ Get the configuration """
    theres = None
    dbs = cfgfdb.churchcal
    colls = dbs.list_collection_names()
    if "cfgdb" in colls:
        thecoll = dbs.cfgdb
        thewkday = dt.datetime(cfgdate).weekday()
        theres = thecoll.find_one({"weekday": thewkday}, {"hours": 1, "_id": 0})
    return theres

def runquery(querydate, querydb):
    """ Run the query on the DB"""
    dbs = querydb.churchcal
    colls = dbs.list_collection_names()
    tmpdate = dt.datetime.strptime(querydate, "%m/%d/Y")
    theres = None
    if "dcoll" in colls:
        thecoll = dbs.dcoll
        thequery = {'datestamp': tmpdate}
        theres = thecoll.find(thequery)
    return theres

def readrec(readdate, readdb):
    """ Read a record (date) """
    return runquery(readdate, readdb)

def postfnd(fnddate, fnddb):
    """ Validate post """
    postfndres = runquery(fnddate, fnddb)
    return bool(postfndres.count != 0)

def writerec(writedate, writename, writedb):
    """ Write a record (date) """
    dbs = writedb.churchcal
    colls = dbs.list_collection_names()
    thecfg = getcfg(writedb, writedate)
    if "dcoll" in colls:
        if postfnd(writedate, writedb):
            print('Appending {0} for {1}'.format(writename, writedate))
        else:
            print('Writing record {1} for {0}'.format(writedate, writename))
    else:
        if thecfg is not None:
            print('Writing initial record {0} for collection dcoll'.format(writedate))
            thecfg['datestamp'] = dt.datetime.strptime(writedate, "%m/%d/Y")
            for myhour in thecfg['hours'].keys():
                # if myhour == writehour:
                for mynames in thecfg['hours'][myhour].keys():
                    if thecfg['hours'][myhour][mynames] == "":
                        print('Writing {0} at {1}'.format(writename, myhour))
                        break
            postcoll = dbs.dcoll
            postcoll.insert_one(thecfg)
        else:
            print("Unable to write record {0}\n".format(writedate))
            print("Is {0} a valid date?".format(writedate))

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
    if len(sys.argv) <= 1:
        print("Defaulting to {0}".format(LOCMDB))
        print("python {0} <mongoDB IP>".format(sys.argv[0]))
    else:
        LOCMDB = str(sys.argv[1])
    bck = ccopen()
    initenv(bck)
    ccdate = inpdate()
    ccname = input("Name: ")
    if postfnd(ccdate, bck):
        print("Record found for {1}".format(ccdate))
    # else:
    #     writerec(ccdate, ccname, bck)
    ccclose(bck)
