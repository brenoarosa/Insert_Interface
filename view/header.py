#!/usr/bin/python

CGIPATH = "."

def header(func):

 def wrapper(*args):
  print ("Content-Type: text/html")     # HTML is following
  print ("")                              # blank line, end of headers
  print ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">")
  print ("<!--https://aliceglance.web.cern.ch/aliceglance/dev/membership/insertMember.php-->")
  print ("<html>")
  print ("<head>")
  print ("<meta http-equiv=\"Content-Type\" content=\"text/html charset=UTF-8\">")
  print ("<title>Membership Insert Interface</title>")
  print ("</head>")
  print ("<body>")
  print ("<div id=\"header\">")
  print ("<h1 class=\"theGlanceProject\"><span>Sistema Automatico de II</span></h1>")
  print ("</div>")
  func(*args)
  print ("</body>")
  print ("</html>")
 return wrapper
