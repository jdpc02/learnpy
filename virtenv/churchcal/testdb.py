"""
 Test python script to read and write from a mongoDB instance
"""
#!/usr/bin/python3
__author__ = 'dev'
import sys
#from mongoengine import connect
import pymongo as mydb

# defaults
LOCMDB = "192.168.0.21"

if len(sys.argv) <= 1:
    print("Defaulting to {0}".format(LOCMDB))
    print("python {0} <mongoDB IP>".format(sys.argv[0]))
else:
    LOCMDB = str(sys.argv[1])

CLIENT = mydb.MongoClient('mongodb://'+ LOCMDB)
try:
    CLIENT.admin.command('ismaster')
except mydb.errors.ConnectionFailure:
    print("Server not available")

print(CLIENT.list_database_names())

# connect(host='mongodb://' + LOCMDB)
