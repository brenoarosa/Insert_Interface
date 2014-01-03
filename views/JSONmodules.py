#!/usr/bin/python
'''
Aqui consideremos o db ja mapeado no json.
tentarei reescrever as funcoes necessarias para refazer
todo o sistema.

'''

import json

def jsonContent(dbName):
  dbFile = open(dbName, 'r')
  jsonStr = dbFile.read()
  dbFile.close()
  dbContent = json.loads( jsonStr )
  return dbContent

def listTables(dbName):
  db = jsonContent(dbName)
  tables = db.keys()
  return tables

def fieldsAttDict(dbName, table):
  db = jsonContent(dbName)
  fieldsDict = db[table]
  return fieldsDict
  
def fieldsList(dbName, table):
  fieldsDict = fieldsAttDict(dbName, table)
  return fieldsDict.keys()

'''
dbName = "Chinook_Sqlite.json"
table = "Customer"


fields = fieldsList(dbName, table)
print (fields)
'''

'''
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

'''
