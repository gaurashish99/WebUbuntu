#!/usr/bin/python

import cgi
import  commands
import cgitb
cgitb.enable()



print("Content-type:text/html\r\n\r\n")
print  ("<html><head><title>Present Working Directory</title>")
print ("<body><h1>")

# gettting  html data 
mypage_data=cgi.FieldStorage()
cmd=mypage_data.getvalue('loc')

print "<pre>"
print   commands.getoutput("cd "+ cmd)
print "<pre>"
print "You're now in "+cmd+" Directory"
print ("</h1></body></html>")