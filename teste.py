#!/usr/bin/python

import sys
import DBmodules
import htmlPrint

#def xml (db, table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType):

db = "teste.db"
table = "cadastro"

(tableRelational, fieldMain, fieldRelational, fieldName, fieldType, mandatoryField, defaultValue, primaryKey) = DBmodules.listTableAttributes(db, table)

htmlPrint.advanced(db,table, tableRelational, fieldMain, fieldRelational, fieldName, fieldType, mandatoryField, defaultValue, primaryKey)

