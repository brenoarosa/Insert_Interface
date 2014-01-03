#!/usr/bin/python

import cgi
import os
import JSONmodules 
import htmlPrint

form = cgi.FieldStorage()
db = form.getvalue("DATABASE_NAME")
table = form.getvalue("DATABASE_TABLE")
action = form.getvalue("DATABASE_ACTION")

if ( action == None ):
  htmlPrint.failure('Selecione o modo!')
  exit(0)


if table == None:
  htmlPrint.failure('Tabela invalida!')
  exit(0)


if action == "XML":
  htmlPrint.basicXml(db, table) 
  exit(0)


if action == "ADVANCED":
  htmlPrint.advanced(db, table)
  exit(0)


if action == "INSERT":
  htmlPrint.insert(db, table)
  exit(0)

if action == "SHOW":
  htmlPrint.show(db, table, fieldName)
  sys.exit(0)
