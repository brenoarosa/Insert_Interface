#!/usr/bin/python

import sqlite3 as lite
import os
import sys

'''
  As funcoes aqui definidas retornam sempre listas,
  Eh necessario funcoes para mapear estas listas em objetos
'''

class DbNotFoundError(Exception):
  pass

def listTables(db):
# db (input) - Database name
# tables (output) - tables list

  if not os.path.isfile(db):
    raise DbNotFoundError("Could not found "+db)
    
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
    raise DbNotFoundError("Could not found "+db)

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
# fieldName (output) - Nome do campo
# fieldType (output) - Tipo do campo
# mandatoryField (out) - Retorna se o campo for obrigatorio
# defaultValue (out) - valor default do campo
# primaryKey (out) - retorna se o campo eh primary key

  if not os.path.isfile(db):
    raise DbNotFoundError("Could not found "+db)
  
  con = lite.connect(db)

  if con:    
    cur = con.cursor()

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
  
  
  return ( fieldName, fieldType, mandatoryField, defaultValue, primaryKey);

def listTableRelational(db, table):
# db (input) - Database name
# table (input) - table name
# tableRelational (output) - lista contendo as tabelas referenciadas
# fieldMain (output) - lista contendo os campos da tabela em questao que fazem referencia a outra tabela
# fieldRelational (output) - lista contendo os campos referenciados


  if not os.path.isfile(db):
    raise DbNotFoundError("Could not found "+db)

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

  return (tableRelational, fieldMain, fieldRelational)

def fullAttList(db, table):
#  O objetivo dessa funcao e mapear as listas relacionadas a foreign_keys com os atributor de um campo
#  Essa funcao tambem cria uma lista de lista de valores pra campos que sao foreign_key
  
  try:
    (fieldName, fieldType, mandatoryField, defaultValue, primaryKey) = listTableAttributes(db, table)
    (auxTableRelational, fieldMain, auxFieldRelational) = listTableRelational(db, table)
  except DbNotFoundError:
    raise DbNotFoundError("Could not found "+db)

  tableRelational = []
  fieldRelational = []
  relationalValues = []
  
  for name in fieldName:
    idx = fieldName.index(name)

    if name in fieldMain:
      tableRelational.append( auxTableRelational[ fieldMain.index(name) ] )
      fieldRelational.append( auxFieldRelational[ fieldMain.index(name) ] )
      relationalValues.append( listValues(db, tableRelational[idx], fieldRelational[idx]) )
    else:
      tableRelational.append(None)
      fieldRelational.append(None)
      relationalValues.append(None)


  return (fieldName, tableRelational, fieldRelational, relationalValues, fieldType, mandatoryField, defaultValue, primaryKey)
