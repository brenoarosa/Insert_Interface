#!/usr/bin/python

import sys
import DBmodules

CGIPATH = "."

def header():
# Fechar </body> e </html>

  print "Content-Type: text/html"     # HTML is following
  print                               # blank line, end of headers
  print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
  print "<!--https://aliceglance.web.cern.ch/aliceglance/dev/membership/insertMember.php-->"
  print "<html>"
  print "<head>"
  print "<meta http-equiv=\"Content-Type\" content=\"text/html charset=UTF-8\">"
  print "<title>Membership Insert Interface</title>"
  print "</head>"
  print "<body>"
  print "<div id=\"header\">"
  print "<h1 class=\"theGlanceProject\"><span>Sistema Automatico de II</span></h1>"
  print "</div>"

  return None



def insert (db, table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType, IIName=None, Mandatory=None, defaultValue=None, Disable=None):
# adicionar a verificacao por javascript

  header()

  print "<div><form target=\"submitButton\" action=\""+CGIPATH+"/insertIntoDB.py\" method=\"post\" name=\"mainForm\">"
  print "<div class=\"divData\">"
  print "<input type=\"hidden\" name=\"DATABASE_NAME\" value=\""+ db +"\" >"
  print "<input type=\"hidden\" name=\"DATABASE_TABLE\" value=\""+ table +"\" >"

  if ( IIName == None ):

    for name in fieldName:
      aux = getIndex(name, fieldMain)

      if (aux != None): #tem relacionamento, aux eh index do campo no fieldMain
        values = DBmodules.listValues(db,tableRelational[aux], fieldRelational[aux])
        print "<div> %s: <select name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\">" % (name, name, name)

        for value in values:
          print "<option value=\"" + value +"\">" + value +" </option> "
        print "</select>"

        auxStr = str(aux)
        print "<input id=\""+auxStr+"\" type=\"hidden\" name=\"DATABASE_TABLE_REL"+auxStr+"\" value=\""+tableRelational[aux]+"\" >"
        print "<class=\"submitButtonDiv\"><input type=\"button\" value=\"Add\" onclick = \"envia('"+ auxStr +"');\"></div>"


      if aux == None: #Nao tem relacionamento
        print "<div> %s: <input type=\"text\" name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\"></div>" % (name, name, name)


  if ( IIName != None ): # caso seja passado o parametro

    for name in fieldName:
      index = getIndex(name, fieldName)
      aux = getIndex(name, fieldMain)
      
      if (IIName[index] == None):
        IIName[index] = name
      if (defaultValue[index] == None):
        defaultValue[index] = ""

      if (Mandatory[index] == None):
        Mandatory[index] = ""
      if (Mandatory[index] == "True"):
        Mandatory[index] = "*"

      if (Disable[index] == None):
        Disable[index] = ""
      if (Disable[index] == "True"):
        Disable[index] = "disabled"


      if (aux != None): #tem relacionamento, aux eh index do campo no fieldMain
        values = DBmodules.listValues(db,tableRelational[aux], fieldRelational[aux])
        print "<div> %s: <select name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\">" % (name, name, name)

        for value in values:
          print "<option value=\"" + value +"\">" + value +" </option> "
        print "</select>"

        auxStr = str(aux)
        print "<input id=\""+auxStr+"\" type=\"hidden\" name=\"DATABASE_TABLE_REL"+auxStr+"\" value=\""+tableRelational[aux]+"\" >"
        print "<class=\"submitButtonDiv\"><input type=\"button\" value=\"Add\" onclick = \"envia('"+ auxStr +"');\"></div>"


      if (aux == None): #Nao tem relacionamento
        print "<div> %s%s: <input type=\"text\" name=\"FIELD_%s\" id=\"DATABASE_FIELD_%s\" value=\"%s\" %s></div>" % (IIName[index], Mandatory[index], name, name, defaultValue[index], Disable[index])

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
  print "function envia(auxStr){"
  print "   var tableName = 'DATABASE_TABLE_REL';"
  print "   tableName = tableName + auxStr;"
  print "   tableName = document.forms[\"mainForm\"][tableName].value;"
  print "   document.forms[\"addForm\"][\"DATABASE_TABLE\"].value = tableName;"
  print "   document.getElementById(\"form2ID\").submit();"
  print "}"
  print "</script>"


  print "</body>"
  print "</html>"

  return None 

def advancedXml(db, table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType, IIName, Mandatory, defaultValue, Disable):

  header()
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

  for name in fieldName:
    foreignIndex = getIndex(name, fieldMain)
    index = getIndex(name, fieldName) # posicao em fieldName equivalente a posicao em fieldType

    if (foreignIndex != None): #tem relacionamento, aux eh index do campo no fieldMain
      print "<column>"
      print "<colName>"+ name  +"</colName>"
      print "<colType>"+ fieldType[index] +"</colType>"
      print "<colReferenceTable>"+ tableRelational[foreignIndex] +"</colReferenceTable>"
      print "<colReferenceCol>"+ fieldRelational[foreignIndex] +"</colReferenceCol>"
      if (IIName[index] != None):
        print "<colDescr>"+ IIName[index] +"</colDescr>"
      if (defaultValue[index] != None):
        print "<colDefValue>"+ defaultValue[index] +"</colDefValue>"
      if (Mandatory[index] != None):
        print "<colMandatory>"+ Mandatory[index] +"</colMandatory>"
      if (Disable[index] != None):
        print "<colDisable>"+ Disable[index] +"</colDisable>"
      print "</column>"

    if ( foreignIndex == None): #Nao tem relacionamento
      print "<column>"
      print "<colName>"+ name +"</colName>"
      print "<colType>"+ fieldType[index] +"</colType>"
      if (IIName[index] != None):
        print "<colDescr>"+ IIName[index] +"</colDescr>"
      if (defaultValue[index] != None):
        print "<colDefValue>"+ defaultValue[index] +"</colDefValue>"
      if (Mandatory[index] != None):
        print "<colMandatory>"+ Mandatory[index] +"</colMandatory>"
      if (Disable[index] != None):
        print "<colDisable>"+ Disable[index] +"</colDisable>"
      print "</column>"


  print "</table>"
  print "</InsertInterface>"
  #Aqui termina o print do XML
  print "</textarea>"
  print "</div>"

  return None


def basicXml(db, table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType):

  header()
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

  for name in fieldName:
    foreignIndex = getIndex(name, fieldMain)
    indexType = getIndex(name, fieldName) # posicao em fieldName equivalente a posicao em fieldType

    if (foreignIndex != None): #tem relacionamento, aux eh index do campo no fieldMain
      print "<column>"
      print "<colName>"+ name  +"</colName>"
      print "<colType>"+ fieldType[indexType] +"</colType>"
      print "<colReferenceTable>"+ tableRelational[foreignIndex] +"</colReferenceTable>"
      print "<colReferenceCol>"+ fieldRelational[foreignIndex] +"</colReferenceCol>"
      print "</column>"

    if ( foreignIndex == None): #Nao tem relacionamento
      print "<column>"
      print "<colName>"+ name +"</colName>"
      print "<colType>"+ fieldType[indexType] +"</colType>"
      print "</column>"

  print "</table>"
  print "</InsertInterface>"
  #Aqui termina o print do XML
  print "</textarea>"
  print "</div>"
  
  return None


def advanced(db,table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType, mandatoryField, defaultValue, primaryKey):
#

  header()
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

  for field in fieldName:
    index = getIndex(field, fieldName) # posicao na lista
    print "<tr>"
    print "<td>" + fieldName[index] + "</td>"
    print "<td> <input type=\"text\" name=\"" +field+"_IINAME\" </td>"
    
    print "<td>" + fieldType[index] + "</td>"

    if (mandatoryField[index] == 1 ):
      print "<td> <input type=\"checkbox\" name=\""+ field +"_MANDATORY\" value = \"True\" checked disabled </td>"    
    if (mandatoryField[index] == 0):
      print "<td> <input type=\"checkbox\" name=\""+ field +"_MANDATORY\" value = \"True\" </td>"
    
    if (defaultValue[index] == None):
      print "<td> <input type=\"text\" name=\""+field+"_DEFAULT\" </td>"
    if (defaultValue[index] != None):
      print "<td> <input type=\"text\" name=\""+ field +"_DEFAULT\" value = \""+ defaultValue[index] +" </td>"

    if (primaryKey[index] == 1 ):
      print "<td> <input type=\"checkbox\" name=\""+ field +"_PRIMARY\" value = \"True\" checked disabled </td>"
    if (primaryKey[index] == 0 ):
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
  print "</body>"
  print "</html>"

  return None



def getIndex(string, lista):
  try:
    aux = lista.index(string)

  except ValueError:
    return None
  
  return aux


def tables (tables, db):

  header()
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
  print "</body>"
  print "</html>"
  return None

def failure(errorMessage):
  
  header()
  print "<div><b> ERRO! </b></div>"
  print "<div> %s </div>" % (errorMessage)
  print "<br clear=\"both\">"
  print "</div>"
 # print "<iframe style=\"display:none\" name=\"submitIframe\" id=\"submitIframe\" src=\"\"></iframe>"
  print "</div>"
  print "</div>"
  print "</body>"
  print "</html>"
  return None

def success(message):
  
  header()
  print "<div><b> "+message+" </b></div>"
  print "<br clear=\"both\">"
  print "</div>"
  # print "<iframe style=\"display:none\" name=\"submitIframe\" id=\"submitIframe\" src=\"\"></iframe>"
  print "</div>"
  print "</div>"
  print "</body>"
  print "</html>"
  return None

