#!/usr/bin/python

import json
import sys
import cgi
import os
import JSONmodules
import traceback
from view.validate import validate as viewValidate
from view.failure import failure as viewFailure
from view.success import success as viewSuccess
from view.insertValidate import insertValidate as viewInsertValidate
from view.valTypes import *

form = cgi.FieldStorage()
db = form.getvalue("DATABASE_NAME")
table = form.getvalue("DATABASE_TABLE")
configFilePath = form.getvalue("FIELD_UUID")

try:
  configFile = open(configFilePath, 'r')
  configFieldJson = configFile.read()
  configFile.close()
except IOError, error:
  viewFailure(error)
  exit(0)

configField = json.loads( configFieldJson )
fieldsDict = JSONmodules.fieldsAttDict(db, table)


for field in configField.keys():
  fieldType = fieldsDict[field]["fieldType"]
  configField[field]["rules"] = {}
  
  if fieldType == "INTEGER":
    for val in INTEGER_VAL.keys():
      aux = form.getvalue(field+"_"+val)
      if aux != None:
        configField[field]["rules"][val] = []
        for i in range(INTEGER_VAL[val]):
          configField[field]["rules"][val].append(form.getvalue(field+"_"+val+"_ARG"+str(i)))

  if fieldType == "TEXT":
    for val in TEXT_VAL.keys():
      aux = form.getvalue(field+"_"+val)
      if aux != None:
        configField[field]["rules"][val] = []
        for i in range(TEXT_VAL[val]):
          configField[field]["rules"][val].append(form.getvalue(field+"_"+val+"_ARG"+str(i)))

  if fieldType == "REAL":
    for val in REAL_VAL.keys():
      aux = form.getvalue(field+"_"+val)
      if aux != None:
        configField[field]["rules"][val] = []
        for i in range(REAL_VAL[val]):
          configField[field]["rules"][val].append(form.getvalue(field+"_"+val+"_ARG"+str(i)))

  if fieldType == "NUMERIC":
    for val in NUMERIC_VAL.keys():
      aux = form.getvalue(field+"_"+val)
      if aux != None:
        configField[field]["rules"][val] = []
        for i in range(NUMERIC_VAL[val]):
          configField[field]["rules"][val].append(form.getvalue(field+"_"+val+"_ARG"+str(i)))



configFieldJson = json.dumps(configField ,indent=4, separators=(',', ': ')  )


try:
  jsonFile = open(configFilePath, 'w')
  jsonFile.write(configFieldJson)
  jsonFile.close()
#  viewInsertValidate(db, table, configFilePath)

except IOError, error:
  viewFailure("File cannot be created!")

viewSuccess("Configuracao da II: ", configFieldJson)
exit(0)
