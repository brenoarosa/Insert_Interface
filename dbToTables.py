#!/usr/bin/python

import sys
import cgitb
import cgi
import os
import DBmodules 
import htmlPrint


form = cgi.FieldStorage()
db = form.getvalue("DATABASE_NAME")


if not os.path.isfile(db):
  htmlPrint.failure('O banco de dados indicado nao existe!')
  sys.exit(0)

tables = DBmodules.listTables(db)

if tables[0] == None:
  htmlPrint.failure('Banco de dados vazio!')
  sys.exit(0)

htmlPrint.tables(tables, db)
sys.exit(0)

