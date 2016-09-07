import urllib2
response = urllib2.urlopen('http://python.org/')
html = response.read ()
print html
print("Cantidad de digitos en la pagina web es de: ", len([x for x in html if x.word()]))
