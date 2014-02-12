#!/usr/bin/python

from header import header
import sys
import JSONmodules
import json

CGIPATH = "."

@header
def validate (db, table, configFilePath):

  print "<div><form target=\"submitButton\" action=\""+CGIPATH+"/insertIntoDB.py\" method=\"post\" name=\"mainForm\">"
  print "<div class=\"divData\">"
  print "<input type=\"hidden\" name=\"DATABASE_NAME\" value=\""+ db +"\" >"
  print "<input type=\"hidden\" name=\"DATABASE_TABLE\" value=\""+ table +"\" >"
  print "<input type=\"hidden\" name=\"FIELD_UUID\" value=\""+ configFilePath +"\" >"

  print "<table boarder=\"1\">"
  print "<tr>"
  print "<th> Name (II)</th>"
  print "<th> Type </th>"
  print "<th> Mandatory </th>"
  print "<th> Validation </th>"
  print "</tr>"

  try:
    configFile = open(configFilePath, 'r')
    configFieldJson = configFile.read()
    configFile.close()
  except IOError as error:
    raise IOError
    exit(0)

  configField = json.loads( configFieldJson )

  for field in configField.keys():
    fieldOpt = configField[field]
    print fieldOpt

    print "<tr>"
    print "<td>" + fieldOpt["IIName"] + "</td>"
    print "<td>" + fieldOpt[""] + "</td>"

'''

  print "</div>" #div class
  print "<div class=\"submitButtonDiv\">"
  print "<input id=\"submitButton\" type=\"submit\" value=\"Submit\">"
  print "</div>" #div class
  print "</form></div>"


  return None
'''

