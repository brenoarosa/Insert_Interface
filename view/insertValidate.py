#!/usr/bin/python

from header import header
from failure import failure as viewFailure
import json
import JSONmodules
import traceback

CGIPATH = "."

#
# APLICAR VALIDACAO
#

@header
def insertValidate(db, table, configFilePath):

  print "<div><form target=\"submitButton\" onsubmit=\"SendEnable()\" action=\""+CGIPATH+"/insertIntoDB.py\" method=\"post\" id=\"mainForm\" name=\"mainForm\">"
  print "<div class=\"divData\">"
  print "<input type=\"hidden\" name=\"DATABASE_NAME\" value=\""+ db +"\" >"
  print "<input type=\"hidden\" name=\"DATABASE_TABLE\" value=\""+ table +"\" >"

  try:
    configFile = open(configFilePath, 'r')
    configFieldJson = configFile.read()
    configFile.close()
  except IOError, error:
    viewFailure(error)
    exit(0)

  configField = json.loads( configFieldJson )
  fieldsDict = JSONmodules.fieldsAttDict(db, table)
  
  for field in configField.keys():
    fieldAtt = fieldsDict[field]

    fieldRelational = fieldAtt["fieldRelational"]
    tableRelational = fieldAtt["tableRelational"]
    relationalValues = fieldAtt["relationalValues"]
    
    IIName = configField[field]["IIName"]
    defaultValue = configField[field]["defaultValue"]
    Mandatory = configField[field]["mandatoryField"]
    Disable = configField[field]["disable"]
    option = configField[field]["opt_type"]

    if (defaultValue == None):
      defaultValue = ""

    if (Mandatory == None):
      Mandatory = ""
    if (Mandatory == "True"):
      Mandatory = "*"
      configField[field]["rules"]["required"] = []

    if (Disable == None):
      Disable = ""
    if (Disable == "True"):
      Disable = "disabled"

    if (fieldRelational == None): #Nao tem relacionamento
        print "<div> %s%s: <input type=\"text\" name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\" value=\"%s\" %s></div>" % (IIName, Mandatory, field, field, defaultValue, Disable)

    if (fieldRelational != None): #tem relacionamento, aux eh index do campo no fieldMain

        if (option == "dropdown"):
          print "<div> %s%s: <select name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\" %s>" % (IIName, Mandatory, field, field, Disable)
          for value in relationalValues:
            if (value == defaultValue):
              print "<option value=\"" + str(value) +"\" selected >" + str(value) +" </option> "
            else:
              print "<option value=\"" + str(value) +"\">" + str(value) +" </option> "
          print "</select>"

        if (option == "radio"):
          print "<div> %s%s:<br>" % (IIName, Mandatory)
          for value in relationalValues:
            if (value == defaultValue):
              print "<input type=\"radio\" name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\" value=\"%s\" checked %s>%s<br>" %(IIName,field,value,Disable,value)
            else:
              print "<input type=\"radio\" name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\" value=\"%s\" %s>%s<br>" %(IIName,field,value,Disable,value)

        print "<class=\"submitButtonDiv\"><input type=\"button\" value=\"Add\" onclick = \"envia('"+ tableRelational +"');\"></div>"


  print "</div>" #div class
  print "<div class=\"submitButtonDiv\">"
  print "<input id=\"submitButton\" type=\"submit\" value=\"Submit\">"
  print "</div>" #div class
  print "</form></div>"

# segundo formulario, envia uma requisicao pra outra tabela
  print "<div><form action=\""+CGIPATH+"/tableToForm.py\" method=\"post\" id=\"form2ID\" name=\"addForm\">"
  print "<div class=\"divData\">"
  print "<input type=\"hidden\" name=\"DATABASE_NAME\" value=\""+ db +"\" >"
  print "<input type=\"hidden\" name=\"DATABASE_TABLE\" value=\"\" >"
  print "<input type=\"hidden\" name=\"DATABASE_ACTION\" value=\"INSERT\" >"
  print "</div>"
  print "</form></div>"


# script
  print "<script>"
  print "function envia(tableName){"
  print "   document.forms[\"addForm\"][\"DATABASE_TABLE\"].value = tableName;"
  print "   document.getElementById(\"form2ID\").submit();"
  print "}"
  print "</script>"

#script Disable
  print "<script>"
  print "function SendEnable(){"
  for field in configField.keys():
    print "  document.getElementById(\"DATABASE_FIELD_%s\").disabled = false;" % (field)
  print "  document.getElementByName(\"mainForm\").submit();"
  print "}"
  print "</script>"

  regra = {"rules": {}}
  for field in configField.keys():
    regra["rules"][field] = configField[field]["rules"]

  regraJson = json.dumps(regra)

#script Validacao
  print "<script>"
  print "$().ready(function() {"
  print "  $(\"#mainForm\").validate("
  print regraJson 
  print "  );"
  print "});"
  print "</script>"
    
  return None

