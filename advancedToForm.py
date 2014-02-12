#!/usr/bin/python

# 
# Responsavel por pegar as entradas no advanced e escreve-las em listas, 
# passando para a funcao que escrevera o xml
# 

"""
BUGTRACK
try:
    blabablabla

except lite.Error:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    htmlPrint.failure(exceptionValue) ####
"""


import sys
import cgi
import os
import JSONmodules
import traceback
from view.insert import insert as viewInsert
from view.failure import failure as viewFailure
from view.advancedXml import advancedXml as viewAdvancedXml


form = cgi.FieldStorage()
db = form.getvalue("DATABASE_NAME")
table = form.getvalue("DATABASE_TABLE")
mode = form.getvalue("OUTPUT_MODE")

fieldName = JSONmodules.fieldsList(db, table)

fieldOpt = {}

# getvalue de campo que nao for preenchido sera colocado como None na lista 

for name in fieldName:
  singularFieldOpt = {}
  singularFieldOpt['IIName'] = form.getvalue(name+"_IINAME") 
  singularFieldOpt['mandatoryField'] = form.getvalue(name+"_MANDATORY") 
  singularFieldOpt['defaultValue'] = form.getvalue(name+"_DEFAULT") 
  singularFieldOpt['disable'] = form.getvalue(name+"_DISABLE")
  singularFieldOpt['opt_type'] = form.getvalue(name+"_OPT_TYPE")
  fieldOpt[name] = singularFieldOpt

if ( mode == "II"):
  try:
    viewInsert (db, table, fieldOpt)
  except:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    viewFailure(exceptionValue) ####  


if ( mode == "XML"):
  try:
    viewAdvancedXml (db, table, fieldOpt)
  except:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    viewFailure(exceptionValue) ####

exit(0)

