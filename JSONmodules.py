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

