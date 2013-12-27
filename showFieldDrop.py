#!/usr/bin/python

import sys
import cgitb
import cgi
import os
import DBmodules 
import htmlPrint

'''form = cgi.FieldStorage()
db = form.getvalue("DATABASE_NAME")
table = form.getvalue("DATABASE_TABLE")
mainField = form.getvalue("MAIN_FIELD")
'''

db = "alunos2.db"
table = "cadastro"
mainField = "ID_Alunos"

if ( mainField == None ):
  htmlPrint.failure('Selecione o modo!')
  sys.exit(0)

(values) = DBmodules.listValues(db, table, mainField)

#passar para htmlPrint
print values
