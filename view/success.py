#!/usr/bin/python

from header import header
import sys
import JSONmodules

CGIPATH = "."

@header
def success(message, submessage=None):

  print "<div><b> "+message+" </b></div>"
  if submessage !=None:
    print "<div>"+ submessage +"</div>"
  return None

