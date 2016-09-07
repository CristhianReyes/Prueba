#!/usr/bin/python
import re
import urllib2
response = urllib2.urlopen('http://python.org/')
html = response.read ()#
print (html)
menorcien = re.compile("[0-9]?[0-9]")
print (menorcien.findall(html))
print "La cantidad de de numeros menores a cien son: ",len(menorcien.findall(html))

