#!/usr/bin/python

import cgi
import os
import JSONmodules 
import htmlPrint
from dbToJson import dbToJson 

form = cgi.FieldStorage()
#db = form.getvalue("DATABASE_NAME")
db = 'teste.db'

if not os.path.isfile(db):
  htmlPrint.failure('O banco de dados indicado nao existe!')
  sys.exit(0)

try:
  db = dbToJson.convert(db)
except IOError as error:
  htmlPrint.failure('Nao foi possivel criar o correspondente .json')

tables = JSONmodules.listTables(db)

if not tables:
  htmlPrint.failure('Banco de dados vazio!')
  exit(0)

htmlPrint.tables(tables, db)
exit(0)

