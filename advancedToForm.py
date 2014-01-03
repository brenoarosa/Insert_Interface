#!/usr/bin/python

# 
# Responsavel por pegar as entradas no advanced e escreve-las em listas, 
# passando para a funcao que escrevera o xml
# 


import sys
import cgi
import os
import DBmodules
import htmlPrint
import traceback

"""
try:
    blabablabla

except lite.Error:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    htmlPrint.failure(exceptionValue) ####
"""

form = cgi.FieldStorage()
db = form.getvalue("DATABASE_NAME")
table = form.getvalue("DATABASE_TABLE")
mode = form.getvalue("OUTPUT_MODE")

(tableRelational, fieldMain, fieldRelational, fieldName, fieldType, mandatoryField, defaultValue, primaryKey) = DBmodules.listTableAttributes(db, table)

IIName = []
Mandatory = []
Padrao = []
Disable = []

# getvalue de campo que nao for preenchido sera colocado como None na lista 

for name in fieldName:
  aux = htmlPrint.getIndex(name, fieldName)
  IIName.append (form.getvalue(name+"_IINAME") )
  Mandatory.append (form.getvalue(name+"_MANDATORY") )
  Padrao.append (form.getvalue(name+"_DEFAULT") )
  Disable.append (form.getvalue(name+"_DISABLE"))

if ( mode == "II"):
  try:
    htmlPrint.insert (db, table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType, IIName, Mandatory, Padrao, Disable)
  except:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    htmlPrint.failure(exceptionValue) ####  


if ( mode == "XML"):
  try:
    htmlPrint.advancedXml (db, table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType, IIName, Mandatory, Padrao, Disable)
  except:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    htmlPrint.failure(exceptionValue) ####

sys.exit(0)

