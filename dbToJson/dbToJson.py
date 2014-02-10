#!/usr/bin/python

#import sqlite3Functions as sql
import sqlite3Models as models
import json
import os

def parser(obj):
  return(json.dumps(obj ,indent=4, separators=(',', ': ')  ))

def jsonExt(db):
  dbList = db.split(".")
  dbList = dbList[:-1]
  dbJson = ".".join(dbList) + ".json"
  return dbJson

def convert(db):
  dbJson = jsonExt(db)

  try:
    jsonFile = open(dbJson, 'w')
    jsonFile.write(parser(models.modelDb(db)))
    jsonFile.close()
  except IOError as error:
    raise IOError("File cannot be created!")
  return dbJson

def searchOriginalName(db):
  db = db.split(".")
  db = db[:-1]
  db = ".".join(db)

  for filename in os.listdir( "." ):
    if db in filename:
      if ".json" in filename:
        pass
      else:
        return filename
