#!/usr/bin/python

import cgi
import os
import JSONmodules 
from view.failure import failure as viewFailure
from view.tables import tables as viewTables
from dbToJson import dbToJson 

form = cgi.FieldStorage()
db = form.getvalue("DATABASE_NAME")
db = "teste.db"

if not os.path.isfile(db):
  viewFailure('O banco de dados indicado nao existe!')
  exit(0)

try:
  db = dbToJson.convert(db)
except IOError as error:
  viewFailure('Nao foi possivel criar o correspondente .json')
  exit(0)

tables = JSONmodules.listTables(db)

if not tables:
  viewFailure('Banco de dados vazio!')
  exit(0)

viewTables(tables, db)
exit(0)
