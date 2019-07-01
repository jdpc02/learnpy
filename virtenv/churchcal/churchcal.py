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

def getfromcfg(cfgdate, cfgfdb):
    """ Get the entry from the config collection """
    theres = None
    dbs = cfgfdb.churchcal
    colls = dbs.list_collection_names()
    if "cfgdb" in colls:
        thecoll = dbs.cfgdb
        thewkday = dt.datetime.strftime(cfgdate, "%w")
        theres = thecoll.find_one({"weekday": thewkday}, {"hours": 1, "_id": 0})
    return theres

def getfromdcoll(fddate, fddb):
    """ Get the entry from the dcoll collection """
    return runquery(fddate, fddb)

def runquery(querydate, querydb):
    """ Run the query on the DB"""
    dbs = querydb.churchcal
    colls = dbs.list_collection_names()
    theres = None
    if "dcoll" in colls:
        thecoll = dbs.dcoll
        thequery = {'datestamp': querydate}
        theres = thecoll.find_one(thequery)
    return theres

def fnddcoll(fnddate, fnddb):
    """ Validate post """
    theres = runquery(fnddate, fnddb)
    try:
        thebool = bool(theres.count() == 1)
    except AttributeError:
        thebool = False
    return thebool

def listhours(listdict):
    """ Specify available hours """
    return listdict['hours'].keys()

def getslots(availdict, availhour):
    """ Number of available slots """
    thenum = 0
    for thename in availdict['hours'][availhour].keys():
        if availdict['hours'][availhour][thename] == "":
            thenum += 1
    return thenum

def getrec(grdate, grdb):
    """ Grab record from config or DB """
    thecfg = None
    if not fnddcoll(grdate, grdb):
        thecfg = getfromcfg(grdate, grdb)
    else:
        thecfg = getfromdcoll(grdate, grdb)
    return thecfg

def gethours(specdate, specdb):
    """ List Available Hours """
    thei = 1
    thenumslots = 0
    thechoice = 0
    thedict = {}
    thecfg = None
    thehours = None

    thecfg = getrec(specdate, specdb)
    if thecfg is not None:
        thehours = listhours(thecfg)
    if thehours is not None:
        for thehour in thehours:
            thenumslots = getslots(thecfg, thehour)
            if thenumslots == 0:
                continue
            print(thei + ") " + thehour + " (" + thenumslots + ")")
            thedict[thei] = thehour
            thei += 1
        if thei > 1:
            while True:
                try:
                    thechoice = int(input("Which Mass? "))
                except ValueError:
                    print("Please enter the number corresponding to the hour")
                else:
                    break
            if thei > thechoice >= 1:
                return thedict[thechoice]
    return None

def setspot(ssdict, sshour, ssname):
    """ Add name to record """
    for thename in ssdict['hours'][sshour].keys():
        if ssdict['hours'][sshour][thename] == "":
            ssdict['hours'][sshour][thename] = ssname
    return ssdict

def writerec(writedate, writename, writedb):
    """ Write the record """
    dbs = writedb.churchcal
    postcoll = dbs.dcoll

    thecfg = getrec(writedate, writedb)
    if thecfg is not None:
        thehour = gethours(writedate, writedb)
        if thehour is not None:
            print('Configuring record {1} for {0}'.format(writename, writedate))
            thecfg = setspot(thecfg, thehour, writename)
    else:
        return False

    if fnddcoll(writedate, writedb):
        print('Updating {1} with {0} at {2}'.format(writename, writedate, thehour))
        theqry = {'datestamp': writedate}
        postcoll.replace_one(theqry, thecfg)
        # theslot = 'Name' + getslots(thecfg, thehour)
        # thekey = 'hours.' + thehour + '.' + theslot
        # thevar = {"$set": {thekey: writename}
        # postcoll.update_one(theqry, thevar)
    else:
        print('Writing record {0}'.format(writedate))
        thecfg['datestamp'] = writedate
        postcoll.insert_one(thecfg)

    return False

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
            thedate = dt.datetime.strptime(thedate, "%m/%d/%Y")
            return thedate

def outputrec():
    """ Print the contents of a dcoll record """

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
    if fnddcoll(ccdate, bck):
        print("Record found for {1}".format(ccdate))
    # else:
    #     writerec(ccdate, ccname, bck)
    ccclose(bck)
