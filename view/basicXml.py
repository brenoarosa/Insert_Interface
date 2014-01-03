#!/usr/bin/python

from header import header
import JSONmodules

CGIPATH = "."

@header
def basicXml(db, table):

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

    if (fieldRelational != None): #tem relacionamento
      print "<column>"
      print "<colName>"+ name  +"</colName>"
      print "<colType>"+ fieldType +"</colType>"
      print "<colReferenceTable>"+ tableRelational +"</colReferenceTable>"
      print "<colReferenceCol>"+ fieldRelational +"</colReferenceCol>"
      print "</column>"

    if ( fieldRelational == None): #Nao tem relacionamento
      print "<column>"
      print "<colName>"+ name +"</colName>"
      print "<colType>"+ fieldType +"</colType>"
      print "</column>"

  print "</table>"
  print "</InsertInterface>"
  #Aqui termina o print do XML
  print "</textarea>"
  print "</div>"

  return None

