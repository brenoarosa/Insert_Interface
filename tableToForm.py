#!/usr/bin/python

import sys
import cgitb
import cgi
import os
import DBmodules 
import htmlPrint

form = cgi.FieldStorage()
db = form.getvalue("DATABASE_NAME")
table = form.getvalue("DATABASE_TABLE")
action = form.getvalue("DATABASE_ACTION")

if ( action == None ):
  htmlPrint.failure('Selecione o modo!')
  sys.exit(0)

if table == None:
  htmlPrint.failure('Tabela invalida!')
  sys.exit(0)

(tableRelational, fieldMain, fieldRelational, fieldName, fieldType, mandatoryField, defaultValue, primaryKey) = DBmodules.listTableAttributes(db, table)

if action == "XML":
  htmlPrint.basicXml(db, table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType) 
  sys.exit(0)


if action == "ADVANCED":
  htmlPrint.advanced(db, table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType, mandatoryField, defaultValue, primaryKey)
  sys.exit(0)


if action == "INSERT":
  htmlPrint.insert(db, table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType)
  sys.exit(0)

if action == "SHOW":
  htmlPrint.show(db, table, fieldName)
  sys.exit(0)
