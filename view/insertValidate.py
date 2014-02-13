#!/usr/bin/python

from header import header

CGIPATH = "."

@header
def insertValidate(db, table, configFilePath):

  print "<div><form target=\"submitButton\" onsubmit=\"SendEnable()\" action=\""+CGIPATH+"/insertIntoDB.py\" method=\"post\" name=\"mainForm\">"
  print "<div class=\"divData\">"
  print "<input type=\"hidden\" name=\"DATABASE_NAME\" value=\""+ db +"\" >"
  print "<input type=\"hidden\" name=\"DATABASE_TABLE\" value=\""+ table +"\" >"

