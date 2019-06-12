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
    theres = None
    if "dcoll" in colls:
        thecoll = dbs.dcoll
        thequery = {querydate: {"$regex": "\\S*"}}
        theres = thecoll.find(thequery)
    return theres

# >>> i = "5"
# >>> mycoll.find_one({"weekday": i}, {"hours":1, "_id": 0})
# {'hours': {'1700': {'Name1': '', 'Name2': '', 'Name3': '', 'Name4': '', 'Name5': ''}}}
# >>> type(mycoll.find_one({"weekday": i}, {"hours":1, "_id": 0}))
# <class 'dict'>
# >>> query = mycoll.find_one({"weekday": i}, {"hours":1, "_id": 0})
# >>> print(query)
# {'hours': {'1700': {'Name1': '', 'Name2': '', 'Name3': '', 'Name4': '', 'Name5': ''}}}
# >>> query['hours']['1700']['Name3'] = "MY New Name"
# >>> query['hours']
# {'1700': {'Name1': '', 'Name2': '', 'Name3': 'MY New Name', 'Name4': '', 'Name5': ''}}
# >>> thisdate = "7/4/2019"
# >>> query['date'] = thisdate
# >>> print(query)
# {'hours': {'1700': {'Name1': '', 'Name2': '', 'Name3': 'MY New Name', 'Name4': '', 'Name5': ''}}, 'date': '7/4/2019'}
# >>> mycoll.insert_one(query)
# <pymongo.results.InsertOneResult object at 0x0000020EE89AF2C8>
# >>> for i in mycoll.find():
# ...     print(i)
# ...
# {'_id': ObjectId('5ce947f44d1d89ad098b703d'), 'weekday': '6', 'hours': {'1030': {'Name1': ''}, '0830': {'Name1': ''}}}
# {'_id': ObjectId('5ce947f44d1d89ad098b703e'), 'weekday': '1', 'hours': {'1900': {'Name1': '', 'Name2': '', 'Name3': '', 'Name4': '', 'Name5': ''}}}
# {'_id': ObjectId('5ce947f44d1d89ad098b703f'), 'weekday': '4', 'hours': {'1900': {'Name1': '', 'Name2': '', 'Name3': '', 'Name4': '', 'Name5': ''}}}
# {'_id': ObjectId('5ce947f44d1d89ad098b7040'), 'weekday': '5', 'hours': {'1700': {'Name1': '', 'Name2': '', 'Name3': '', 'Name4': '', 'Name5': ''}}}
# {'_id': ObjectId('5ce94da54d1d89ad098b7041'), 'hours': {'1700': {'Name1': '', 'Name2': '', 'Name3': 'MY New Name', 'Name4': '', 'Name5': ''}}, 'date': '7/4/2019'}
# >>> mycoll.find_one({"date": thisdate}, {"_id":0})
# {'hours': {'1700': {'Name1': '', 'Name2': '', 'Name3': 'MY New Name', 'Name4': '', 'Name5': ''}}, 'date': '7/4/2019'}

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
    dbs = writedb.churchcal
    colls = dbs.list_collection_names()
    thewkday = dt.datetime(writedate).weekday()
    thecfg = getcfg(writedb, writedate)
    if "dcoll" in colls:
        if postfnd(writedate, writedb):
            print('Appending {0} for {1}'.format(writename, writedate))
        else:
            print('Writing record {1} for {0}'.format(writedate, writename))
    else:
        print('Writing initial record {0} for collection dcoll'.format(writedate))
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
