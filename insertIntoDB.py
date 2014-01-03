#!/usr/bin/python

import sys
import cgitb
import sqlite3 as lite
import cgi
import DBmodules
import os
import htmlPrint
import traceback

form = cgi.FieldStorage()


db = form.getvalue("DATABASE_NAME")
con = lite.connect(db) #Conectando com bando de dados.

if con:
  table = form.getvalue("DATABASE_TABLE") 
  (tUSELESS, fiUSELESS, fdUSELESS, fieldName, fieldType, dUSELESS, aUSELESS, iUSELESS) = DBmodules.listTableAttributes(db, table)
  actionDB = con.cursor() #Instanciamento para realizar comandos no BD.

  values = []
  # Aqui serao armazenados os valores dos campos, na mesma sequencia que os campos estao estruturados no db

  stringValues = ""
  # aqui estarao os valores dos campos, em sequencia, separados por virgula

  for field in fieldName:
    values.append( form.getvalue("FIELD_" + field) )

  for value in values:
    if value == None:
      aux = htmlPrint.getIndex(value, values)
      htmlPrint.failure("Campo "+ fieldName[aux] +" em branco!")
      sys.exit(0)

    value = "\'" + value + "\'"
    stringValues = stringValues + ", " + value


  stringValues = stringValues[2:] # retira a virgula inicial

#  htmlPrint.failure("INSERT INTO \""+ table +"\" VALUES(" + stringValues +");") ####DEBBUGER STRING
  try:
    actionDB.execute("INSERT INTO \""+ table +"\" VALUES(" + stringValues +");") 
    con.commit() # envia o comando ao sql

  except lite.Error:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    htmlPrint.failure(exceptionValue) ####
    con.close()
    sys.exit(0)
  
  actionDB.close()

con.close()
htmlPrint.success("Entrada adicionada ao Banco de Dados com sucesso!")  
sys.exit(0)


