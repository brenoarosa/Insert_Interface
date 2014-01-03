#!/usr/bin/python

from header import header
import sys
import JSONmodules

CGIPATH = "."

@header
def success(message):

  print "<div><b> "+message+" </b></div>"
  print "<br clear=\"both\">"
  print "</div>"
  # print "<iframe style=\"display:none\" name=\"submitIframe\" id=\"submitIframe\" src=\"\"></iframe>"
  print "</div>"
  print "</div>"
  return None

