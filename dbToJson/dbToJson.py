#!/usr/bin/python

#import sqlite3Functions as sql
import sqlite3Models as models
import json

db = 'Chinook_Sqlite.sqlite'

def parser(func):
  return(json.dumps(func ,indent=4, separators=(',', ': ')  ))


dbList = db.split(".")
dbList = dbList[:-1]
dbJson = ".".join(dbList) + ".json"

try:
  jsonFile = open(dbJson, 'w')
  jsonFile.write(parser(models.modelDb(db)))
except IOError as error:
  print ("File cannot be created!")

