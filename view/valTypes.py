#!/usr/bin/python


# jquery validations at: http://jqueryvalidation.org/documentation/

# DATATYPE = {VALIDATION: ARGUMENTS NEEDED, ...}
#def sqlite3():

INTEGER_VAL = {"min" : 1 , "max" : 1 , "range" : 2, "digits" : 0 }
TEXT_VAL = {"minlenght" : 1, "maxlenght" : 1, "rangelenght" : 2, "email" : 0, "url" : 0, "date" : 0, "dateISO" : 0}
REAL_VAL = {"min" : 1, "max" : 1, "range": 2, "number" : 0}
NUMERIC_VAL = {"min" : 1, "max" : 1, "range" : 2, "number" : 0, "digits" : 0, "date" : 0, "dateISO" : 0, "creditcard" : 0}
