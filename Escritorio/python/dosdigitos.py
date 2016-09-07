#!/usr/bin/python
import re
import urllib2
response = urllib2.urlopen('http://python.org/')
html = response.read()
print (html)
patrondigito = re.compile("\d{2}")
print (patrondigito.findall(html))
print "La cantidad de digitos en la pagina son: ", len(patrondigito.findall(html))
