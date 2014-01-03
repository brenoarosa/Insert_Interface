#!/usr/bin/python

from header import header
import sys
import JSONmodules

CGIPATH = "."

@header
def failure(errorMessage):

  print "<div><b> ERRO! </b></div>"
  print "<div> %s </div>" % (errorMessage)
  print "<br clear=\"both\">"
  print "</div>"
 # print "<iframe style=\"display:none\" name=\"submitIframe\" id=\"submitIframe\" src=\"\"></iframe>"
  print "</div>"
  print "</div>"
  return None
