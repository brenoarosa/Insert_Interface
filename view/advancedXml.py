#!/usr/bin/python

from header import header
import sys
import JSONmodules

CGIPATH = "."

#fieldOpt e um dict que contem as opcoes que o usuario 
#selecionou na pagina adv.
@header
def advancedXml(db, table, fieldOpt):

  print "<div class=\"title2\">"
  print "<h2>XML Editor</h2>"
  print "</div>" #header2
  print "<div>"
  print "<textarea name=\"xmlData\" cols=\"80\" rows=\"25\">"
  #Aqui comeca o print do XML

  print "<InsertInterface>"
  print "<name>Insert Interface for "+ db +"</name>"
  print "<database>"
  print "<connectString>"+ db +"</connectString>"
  print "</database>"
  print "<table>"
  print "<TableName>"+ table +"</TableName>"

  fieldsDict = JSONmodules.fieldsAttDict(db, table)
  fieldName = JSONmodules.fieldsList(db, table)

  for name in fieldName:

    fieldAtt = fieldsDict[name]
    fieldRelational = fieldAtt["fieldRelational"]
    fieldType = fieldAtt["fieldType"]
    tableRelational = fieldAtt["tableRelational"]
    primaryKey = fieldAtt["primaryKey"]

    IIName = fieldOpt[name].get("IIName")
    defaultValue = fieldOpt[name].get("defaultValue")
    mandatoryField = fieldOpt[name].get("mandatoryField")
    disable = fieldOpt[name].get("disable")

    if (fieldRelational != None): #tem relacionamento
      print "<column>"
      print "<colName>"+ name  +"</colName>"
      print "<colType>"+ fieldType +"</colType>"
      print "<colReferenceTable>"+ tableRelational +"</colReferenceTable>"
      print "<colReferenceCol>"+ fieldRelational +"</colReferenceCol>"
      if (IIName != None):
        print "<colDescr>"+ IIName +"</colDescr>"
      if (defaultValue != None):
        print "<colDefValue>"+ defaultValue +"</colDefValue>"
      if (mandatoryField != None):
        print "<colMandatory>"+ mandatoryField +"</colMandatory>"
      if (disable != None):
        print "<colDisable>"+ disable +"</colDisable>"
      print "</column>"

    if ( fieldRelational == None): #Nao tem relacionamento
      print "<column>"
      print "<colName>"+ name +"</colName>"
      print "<colType>"+ fieldType +"</colType>"
      if (IIName != None):
        print "<colDescr>"+ IIName +"</colDescr>"
      if (defaultValue != None):
        print "<colDefValue>"+ defaultValue +"</colDefValue>"
      if (mandatoryField != None):
        print "<colMandatory>"+ mandatoryField +"</colMandatory>"
      if (disable != None):
        print "<colDisable>"+ disable +"</colDisable>"
      print "</column>"

  print "</table>"
  print "</InsertInterface>"
  #Aqui termina o print do XML
  print "</textarea>"
  print "</div>"

  return None

