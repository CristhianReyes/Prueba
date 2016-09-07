#!/usr/bin/python
import re
import urllib2
response = urllib2.urlopen('http://python.org/')
html = response.read ()#
print (html)
palabras = re.compile("[a-z]+")
print(palabras.findall(html))
print "la cantidad de palabras que hay en el texto son: ", len(palabras.findall(html))
