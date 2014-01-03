#!/usr/bin/python

import cgi
import os
import JSONmodules 
from view.failure import failure as viewFailure
from view.basicXml import basicXml as viewBasicXml
from view.advanced import advanced as viewAdvanced
from view.insert import insert as viewInsert

form = cgi.FieldStorage()
db = form.getvalue("DATABASE_NAME")
table = form.getvalue("DATABASE_TABLE")
action = form.getvalue("DATABASE_ACTION")

if ( action == None ):
  viewFailure('Selecione o modo!')
  exit(0)


if table == None:
  viewFailure('Tabela invalida!')
  exit(0)


if action == "XML":
  viewBasicXml(db, table) 
  exit(0)


if action == "ADVANCED":
  viewAdvanced(db, table)
  exit(0)


if action == "INSERT":
  viewInsert(db, table)
  exit(0)

if action == "SHOW":
  viewShow(db, table, fieldName)
  sys.exit(0)
