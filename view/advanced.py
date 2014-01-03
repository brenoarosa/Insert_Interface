#!/usr/bin/python

from header import header
import sys
import JSONmodules

CGIPATH = "."

@header
def advanced(db,table):
#

  print "<div class=\"title2\">"
  print "<h2>Advanced Options</h2>"
  print "</div>" #header2

  print "<div><form target=\"submitButton\" action=\""+CGIPATH+"/advancedToForm.py\" method=\"post\" >"
  print "<input type=\"hidden\" name=\"DATABASE_NAME\" value=\""+ db +"\" >"
  print "<input type=\"hidden\" name=\"DATABASE_TABLE\" value=\""+ table +"\" >"
  print "<table boarder=\"1\">"
  print "<tr>"
  print "<th> Name (DB)</th>"
  print "<th> Name (II)</th>"
  print "<th> Type </th>"
  print "<th> Mandatory </th>"
  print "<th> Default Value </th>"
  print "<th> Primary Key </th>"
  print "<th> Disable </th>"

  print "</tr>"

  fieldsDict = JSONmodules.fieldsAttDict(db, table)
  fieldName = JSONmodules.fieldsList(db, table)

  for field in fieldName:
    fieldAtt = fieldsDict[field]
    fieldRelational = fieldAtt["fieldRelational"]
    fieldType = fieldAtt["fieldType"]
    tableRelational = fieldAtt["tableRelational"]
    mandatoryField = fieldAtt["mandatoryField"]
    defaultValue = fieldAtt["defaultValue"]
    primaryKey = fieldAtt["primaryKey"]

    print "<tr>"
    print "<td>" + field + "</td>"
    print "<td> <input type=\"text\" name=\"" +field+"_IINAME\" </td>"

    print "<td>" + fieldType + "</td>"

    if (mandatoryField == 1 ):
      print "<td> <input type=\"checkbox\" name=\""+ field +"_MANDATORY\" value = \"True\" checked disabled </td>"
    if (mandatoryField == 0):
      print "<td> <input type=\"checkbox\" name=\""+ field +"_MANDATORY\" value = \"True\" </td>"

    if (defaultValue == None):
      print "<td> <input type=\"text\" name=\""+field+"_DEFAULT\" </td>"
    if (defaultValue != None):
      print "<td> <input type=\"text\" name=\""+ field +"_DEFAULT\" value = \""+ defaultValue +" </td>"

    if (primaryKey == 1 ):
      print "<td> <input type=\"checkbox\" name=\""+ field +"_PRIMARY\" value = \"True\" checked disabled </td>"
    if (primaryKey == 0 ):
      print "<td> <input type=\"checkbox\" name=\""+ field +"_PRIMARY\" value = \"True\" disabled </td>"

    print "<td> <input type=\"checkbox\" name=\""+ field +"_DISABLE\" value = \"True\" </td>"
    print "</tr>"

  print "</table>"
  print "<br>"
  print "<div> Select the output mode: </div>"
  print "<div>"
  print "<input type=\"radio\" name=\"OUTPUT_MODE\" value = \"II\" checked >Insert Interface "
  print "<input type=\"radio\" name=\"OUTPUT_MODE\" value = \"XML\" >XML"
  print "</div>"

  print "<div class=\"submitButtonDiv\">"
  print "<input id=\"submitButton\" type=\"submit\" value=\"Submit\">"
  print "</div>" #div class
  print "</form></div>" #form

  return None

