#!/usr/bin/python

import sqlite3 as lite
import os
import sys

def insertTransaction(db, transaction):
# transaction (in) : script de insercao no DB
# sucess (out) : retorna se a operacao foi realizada com sucesso
# exceptionValue (out) : retorna a string de error

  exceptionValue = ""
  sucess = True

  if not os.path.isfile(db):
    sys.exit(0)

  con = lite.connect(db)
  
  if con:
    cur = con.cursor()
    
    try:
      cur.executescript(transaction)
    
    except lite.Error:
      exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
      sucess = False

  return (success, exceptionValue);


def listTables(db):
# db (input) - Database name
# tables (output) - tables list

  if not os.path.isfile(db):
    sys.exit(0)
    
  con = lite.connect(db)
  tables = []

  if con:
    cur = con.cursor()
    cur.execute("select name from sqlite_master where type = 'table'")
    tablesBD = cur.fetchall()

    for tableBD in tablesBD:
      tables.append (tableBD[0])

  return tables;
		

def listValues(db, table, field):
# db(input) - Database name
# table (input) - selected table
# field (input) - selected field
# values (output) - values to show
  if not os.path.isfile(db):
    sys.exit(0)

  con = lite.connect(db)

  if con:
    cur = con.cursor()
    cur.execute("select "+ field + " from " + table)
    listas = cur.fetchall()
    
    values = []
    for lista in listas:
      values.append (lista[0])

  return values


def listTableAttributes(db, table):
# db (input) - Database name
# table (input) - table name
# tableRelational (output) - lista contendo as tabelas referenciadas
# fieldMain (output) - lista contendo os campos da tabela em questao que fazem referencia a outra tabela
# fieldRelational (output) - lista contendo os campos referenciados
# fieldName (output) - Nome do campo
# fieldType (output) - Tipo do campo


  if not os.path.isfile(db):
    sys.exit(0)
  
  con = lite.connect(db)

  if con:    
    cur = con.cursor()

    cur.execute("PRAGMA foreign_key_list(" + table+ ")")
    allForeign = cur.fetchall()
    # comando acima lista todos campos relacionais da tabela indicada

    tableRelational = [] # lista contendo as tabelas referenciadas
    fieldMain = [] # lista contendo os campos da tabela em questao que fazem referencia a outra tabela
    fieldRelational = [] # lista contendo os campos referenciados

    for foreign in allForeign:
      tableRelational.append( foreign[2] )
      fieldMain.append( foreign[3] )
      fieldRelational.append( foreign[4] )

    fieldName = [] # Nome do campo
    fieldType = [] # Tipo do campo
    mandatoryField = [] # Verify if the field is mandatory
    defaultValue = [] # Return the default value of the field
    primaryKey = [] # Boolean that returns true when the field is a Primary Key
    
    cur.execute("PRAGMA table_info(" + table + ")")
    allAttributes = cur.fetchall()

    for attribute in allAttributes:
      fieldName.append( attribute[1] )
      fieldType.append( attribute[2] )
      mandatoryField.append( attribute[3] )
      defaultValue.append( attribute[4] )
      primaryKey.append( attribute[5] )
  
  
  return (tableRelational, fieldMain, fieldRelational, fieldName, fieldType, mandatoryField, defaultValue, primaryKey);
