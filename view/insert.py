#!/usr/bin/python

from header import header
import sys
import JSONmodules

CGIPATH = "."

@header
def insert (db, table, fieldOpt=None):

  print "<div><form target=\"submitButton\" onsubmit=\"SendEnable()\" action=\""+CGIPATH+"/insertIntoDB.py\" method=\"post\" name=\"mainForm\">"
  print "<div class=\"divData\">"
  print "<input type=\"hidden\" name=\"DATABASE_NAME\" value=\""+ db +"\" >"
  print "<input type=\"hidden\" name=\"DATABASE_TABLE\" value=\""+ table +"\" >"

  if ( fieldOpt == None ):

    fieldsDict = JSONmodules.fieldsAttDict(db, table)
    fieldName = JSONmodules.fieldsList(db, table)
    for name in fieldName:
      fieldAtt = fieldsDict[name]
      fieldRelational = fieldAtt["fieldRelational"]
      tableRelational = fieldAtt["tableRelational"] 
      relationalValues = fieldAtt["relationalValues"]

      if (fieldRelational != None): #tem relacionamento, aux eh index do campo no fieldMain
        print "<div> %s: <select name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\">" % (name, name, name)

        for value in relationalValues:
          print "<option value=\"" + value +"\">" + value +" </option> "
        print "</select>"

        print "<class=\"submitButtonDiv\"><input type=\"button\" value=\"Add\" onclick = \"envia('"+ tableRelational +"');\"></div>"


      if fieldRelational == None: #Nao tem relacionamento
        print "<div> %s: <input type=\"text\" name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\"></div>" % (name, name, name)


  if ( fieldOpt != None ): # caso seja passado o parametro

    fieldsDict = JSONmodules.fieldsAttDict(db, table)
    fieldName = JSONmodules.fieldsList(db, table)
    for name in fieldName:
      fieldAtt = fieldsDict[name]
      fieldRelational = fieldAtt["fieldRelational"]
      tableRelational = fieldAtt["tableRelational"]
      relationalValues = fieldAtt["relationalValues"]

      IIName = fieldOpt[name].get("IIName")
      defaultValue = fieldOpt[name].get("defaultValue")
      Mandatory = fieldOpt[name].get("mandatoryField")
      Disable = fieldOpt[name].get("disable")
      option = fieldOpt[name].get("opt_type")

      if (IIName == None):
        IIName = name

      if (defaultValue == None):
        defaultValue = ""

      if (Mandatory == None):
        Mandatory = ""
      if (Mandatory == "True"):
        Mandatory = "*"

      if (Disable == None):
        Disable = ""
      if (Disable == "True"):
        Disable = "disabled"


      if (fieldRelational != None): #tem relacionamento, aux eh index do campo no fieldMain

        if (option == "dropdown"):
          print "<div> %s%s: <select name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\" %s>" % (IIName, Mandatory, name, name, Disable)
          for value in relationalValues:
            if (value == defaultValue):
	          print "<option value=\"" + value +"\" selected >" + value +" </option> "
            else:
              print "<option value=\"" + value +"\">" + value +" </option> "
          print "</select>"

        if (option == "radio"):
          print "<div> %s%s:<br>" % (IIName, Mandatory)
          for value in relationalValues:
            if (value == defaultValue):
              print "<input type=\"radio\" name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\" value=\"%s\" checked %s>%s<br>" %(IIName,name,value,Disable,value)
            else:
              print "<input type=\"radio\" name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\" value=\"%s\" %s>%s<br>" %(IIName,name,value,Disable,value)

        print "<class=\"submitButtonDiv\"><input type=\"button\" value=\"Add\" onclick = \"envia('"+ tableRelational +"');\"></div>"


      if (fieldRelational == None): #Nao tem relacionamento
        print "<div> %s%s: <input type=\"text\" name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\" value=\"%s\" %s></div>" % (IIName, Mandatory, name, name, defaultValue, Disable)

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
  for name in fieldName:
    print "  document.getElementById(\"DATABASE_FIELD_%s\").disabled = false;" % (name)
  print "  document.getElementByName(\"mainForm\").submit();"
  print "}"
  print "</script>"


  return None

