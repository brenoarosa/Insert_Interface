#!/usr/bin/python

"""
BUGTRACK
try:
    blabablabla

except lite.Error:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    htmlPrint.failure(exceptionValue) ####
"""

import json
import sys
import cgi
import os
import JSONmodules
import traceback
from view.insert import insert as viewInsert
from view.failure import failure as viewFailure
from view.advancedXml import advancedXml as viewAdvancedXml
from lib.random_id import random_id


#form = cgi.FieldStorage()
#db = form.getvalue("DATABASE_NAME")
#table = form.getvalue("DATABASE_TABLE")
#mode = form.getvalue("OUTPUT_MODE")
db = "teste.json"
table = "cadastro"

fieldName = JSONmodules.fieldsList(db, table)

fieldOpt = {}

# getvalue de campo que nao for preenchido sera colocado como None na lista 

for name in fieldName:
  singularFieldOpt = {}

#  singularFieldOpt['IIName'] = form.getvalue(name+"_IINAME") 
#  singularFieldOpt['mandatoryField'] = form.getvalue(name+"_MANDATORY") 
#  singularFieldOpt['defaultValue'] = form.getvalue(name+"_DEFAULT") 
#  singularFieldOpt['disable'] = form.getvalue(name+"_DISABLE")

  singularFieldOpt['IIName'] = name+ "_IINAME" 
  singularFieldOpt['mandatoryField'] = "True" 
  singularFieldOpt['defaultValue'] = name+"_DEFAULT" 
  singularFieldOpt['disable'] = "True"
  fieldOpt[name] = singularFieldOpt

fieldOptJson = json.dumps(fieldOpt ,indent=4, separators=(',', ': ')  )

jsonId = random_id()
fileFullPath = os.path.abspath("./temp") + "/" + jsonId

try:
  jsonFile = open(fileFullPath, 'w')
  jsonFile.write(fieldOptJson)
  print ("Created file "+ fileFullPath)
  jsonFile.close()
except IOError as error:
  raise IOError("File cannot be created!")

exit(0)

