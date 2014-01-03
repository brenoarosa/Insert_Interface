#!/usr/bin/python

from header import header
import sys
import JSONmodules

CGIPATH = "."

@header
def tables (tables, db):

  print "<div><form target=\"submitButton\" action=\""+CGIPATH+"/tableToForm.py\" method=\"post\" >"
  print "<input type=\"hidden\" name=\"DATABASE_NAME\" value=\""+ db +"\" >"
  print "<div class=\"divData\">"
  print "<select name=\"DATABASE_TABLE\" id=\"DB_TABLE\">"
  for table in tables:
    print "<option value=\"" + table +"\">" + table +" </option>"

  print "</select>"
  print "</div>" #div class
  print "<br></br>"
  print "Selecione a opcao desejada com Banco de Dados"
  print "<div><input type=\"radio\" name=\"DATABASE_ACTION\" value=\"INSERT\" >Simple Insert Interface</div>"
  print "<div><input type=\"radio\" name=\"DATABASE_ACTION\" value=\"XML\">Simple XML</div>"
  print "<div><input type=\"radio\" name=\"DATABASE_ACTION\" value=\"ADVANCED\" checked >Advanced</div>"
  print "<div><input type=\"radio\" name=\"DATABASE_ACTION\" value=\"SHOW\" disabled>Exibir >>Nao implementada! </div>"
  print "<div class=\"submitButtonDiv\">"
  print "<input id=\"submitButton\" type=\"submit\" value=\"Submit\">"
  print "</div>" #div class
  print "</form></div>" #form
 # print "<iframe style=\"display:none\" name=\"submitIframe\" id=\"submitIframe\" src=\"\"></iframe>"
  return None

