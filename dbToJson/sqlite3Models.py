#!/usr/bin/python

import sqlite3Functions as sql
import json

class Field:
#  tableRelational = None
#  fieldRelational = None
#  relationalValues = []

#  fieldType = ''
#  mandatoryField = False
#  defaultValue = None
#  primaryKey = False

  def __init__(self, tableRelational, fieldRelational, relationalValues, fieldType, mandatoryField, defaultValue, primaryKey):
    self.tableRelational = tableRelational
    self.fieldRelational = fieldRelational
    self.relationalValues = relationalValues
    self.fieldType = fieldType
    self.mandatoryField = mandatoryField
    self.defaultValue = defaultValue
    self.primaryKey = primaryKey

class Table:
# name(in) = name of the table
# fields = list of field's objects

  def __init__(self, tableName):
    self.name = tableName
    self.fields = {}

  def fill (self, fieldNameList, tableRelationalList, fieldRelationalList, relationalValuesList, fieldTypeList, mandatoryFieldList, defaultValueList, primaryKeyList):
    for fieldName in fieldNameList:
      idx = fieldNameList.index(fieldName)
      tableRelational = tableRelationalList[idx]
      fieldRelational = fieldRelationalList[idx]
      relationalValues = relationalValuesList[idx]
      fieldType = fieldTypeList[idx]
      mandatoryField = mandatoryFieldList[idx]
      defaultValue = defaultValueList[idx]
      primaryKey = primaryKeyList[idx]

      obj = Field(tableRelational, fieldRelational, relationalValues, fieldType, mandatoryField, defaultValue, primaryKey)
      self.fields[fieldName] = obj.__dict__

def modelDb(db):
  try:
    tables = sql.listTables(db)
  except sql.DbNotFoundError as error:
    print(error.args[0])
    exit(1)

  tableListJson = {}

  for table in tables:
    tableListJson[table] = modelTable(db, table)

  return(tableListJson)


def modelTable(db, table):
  try:
    (fieldNameList, tableRelationalList, fieldRelationalList, relationalValuesList, fieldTypeList, mandatoryFieldList, defaultValueList, primaryKeyList) = sql.fullAttList(db, table)
  except sql.DbNotFoundError as error:
    print(error.args[0])
    exit(1)

  tab = Table(table)
  tab.fill(fieldNameList, tableRelationalList, fieldRelationalList, relationalValuesList, fieldTypeList, mandatoryFieldList, defaultValueList, primaryKeyList)
  return(tab.fields)

