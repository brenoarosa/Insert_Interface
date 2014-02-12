#!/usr/bin/python

from header import header
import sys
import JSONmodules
import json
from dbTypes import *
from valTypes import *

CGIPATH = "."

@header
def validate (db, table, configFilePath):

  print "<div><form target=\"submitButton\" action=\""+CGIPATH+"/****************.py\" method=\"post\" name=\"mainForm\">"
  print "<div class=\"divData\">"
  print "<input type=\"hidden\" name=\"DATABASE_NAME\" value=\""+ db +"\" >"
  print "<input type=\"hidden\" name=\"DATABASE_TABLE\" value=\""+ table +"\" >"
  print "<input type=\"hidden\" name=\"FIELD_UUID\" value=\""+ configFilePath +"\" >"

  print "<table boarder=\"1\">"
  print "<tr>"
  print "<th> Name (II)</th>"
  print "<th> Type </th>"
  print "<th> Validations</th>"
  print "</tr>"

  try:
    configFile = open(configFilePath, 'r')
    configFieldJson = configFile.read()
    configFile.close()
  except IOError as error:
    raise IOError
    exit(0)

  configField = json.loads( configFieldJson )
  fieldsDict = JSONmodules.fieldsAttDict(db, table)
  
  for field in configField.keys():
    fieldOpt = configField[field]
    fieldType = fieldsDict[field]["fieldType"]

    print "<tr>"
    print "<td>" + fieldOpt["IIName"] + "</td>"
    print "<td>" + fieldType + "</td>"
    print "</tr>"

    if fieldType in INTEGER:
      for val in INTEGER_VAL.keys():
        print("<tr><td></td><td></td>")
	print ("<td> <input type=\"checkbox\" name=\""+ val +"\" value = \"True\">" + val)
	for i in range(INTEGER_VAL[val]):
	  print ("<input type=\"text\" name= \""+field+"_"+val+"_ARG"+str(i)+"\">")
        print("</td></tr>")


    if fieldType in TEXT:
      for val in TEXT_VAL.keys():
        print("<tr><td></td><td></td>")
        print ("<td> <input type=\"checkbox\" name=\""+ val +"\" value = \"True\">" + val)
        for i in range(TEXT_VAL[val]):
          print ("<input type=\"text\" name= \""+field+"_"+val+"_ARG"+str(i)+"\">")
        print("</td></tr>")


    if fieldType in REAL:
      for val in REAL_VAL.keys():
        print("<tr><td></td><td></td>")
        print ("<td> <input type=\"checkbox\" name=\""+ val +"\" value = \"True\">" + val)
        for i in range(REAL_VAL[val]):
          print ("<input type=\"text\" name= \""+field+"_"+val+"_ARG"+str(i)+"\">")
        print("</td></tr>")


    if fieldType in NUMERIC:
      for val in NUMERIC_VAL.keys():
        print("<tr><td></td><td></td>")
        print ("<td> <input type=\"checkbox\" name=\""+ val +"\" value = \"True\">" + val)
        for i in range(NUMERIC_VAL[val]):
          print ("<input type=\"text\" name= \""+field+"_"+val+"_ARG"+str(i)+"\">")
	print("</td></tr>")

  
  print "</table>"
  print "</div>" #div class
  print "<div class=\"submitButtonDiv\">"
  print "<input id=\"submitButton\" type=\"submit\" value=\"Submit\">"
  print "</div>" #div class
  print "</form></div>"


  return None
