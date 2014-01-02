#!/usr/bin/python

import json

dbName = "Chinook_Sqlite.json"
table = "Customer"

dbFile = open(dbName, 'r').read()

db = json.loads( dbFile )
#print( db.keys() )
fields = db[table]
for fieldName in fields.keys():
  fieldAtt = fields[fieldName]
  fieldRelational = fieldAtt["fieldRelational"]
  mandatoryField = fieldAtt["mandatoryField"]
  fieldType = fieldAtt["fieldType"]
  relationalValues = fieldAtt["relationalValues"]
  tableRelational = fieldAtt["tableRelational"]
  primaryKey = fieldAtt["primaryKey"]
  defaultValue = fieldAtt["defaultValue"]
  print (fieldName +" : "+str(fieldRelational)+", "+str(mandatoryField)+", "+str(fieldType)+", "+str(relationalValues)+", "+str(tableRelational)+", "+str(primaryKey)+", "+str(defaultValue))
