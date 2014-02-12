#!/usr/bin/python

import dbToJson.sqlite3Functions as sql
import cgi
import JSONmodules
from dbToJson import dbToJson
from view.failure import failure as viewFailure
from view.success import success as viewSuccess


form = cgi.FieldStorage()
db = form.getvalue("DATABASE_NAME")
table = form.getvalue("DATABASE_TABLE") 

fieldName = JSONmodules.fieldsList(db, table)

values = []
# Aqui serao armazenados os valores dos campos, na mesma sequencia que os campos estao estruturados no db

stringFields = ""
stringValues = ""
# aqui estarao os valores dos campos, em sequencia, separados por virgula

for field in fieldName:
  values.append( form.getvalue("FIELD_" + field) )


for i in xrange(len(fieldName)): #Varre todos campos

#  viewFailure(str(i) + " : "+ str(values[i])) DEBBUGER
  if values[i] != None: #Se a pessoa nao deixar o campo em branco
    field = "\'" + fieldName[i] + "\'"
    stringFields = stringFields + ", " + field
    value = "\'" + values[i] + "\'"
    stringValues = stringValues + ", " + value


stringValues = stringValues[2:] # retira a virgula inicial
stringFields = stringFields[2:]

transaction = "INSERT INTO \""+ table +"\"("+ stringFields +") VALUES(" + stringValues +")"

try:
  db = dbToJson.searchOriginalName(db) #tenta achar o nome original do arquivo
  sql.insertTransaction(db, transaction)

except Exception, e:
  viewFailure(e)
  exit(0)

viewSuccess("Entrada adicionada ao Banco de Dados com sucesso!")  
exit(0)

