import urllib2
response = urllib2.urlopen('http://www.maestrosdelweb.com/guia-python-cadenas-de-texto/')
html = response.read()
arreglo = []

segc = 0
ultima = 0

while segc <= 0:
	href = html.find('a href', ultima)
	pric = html.find('"', href)
	segc = html.find('"', pric+2)
	enlace = html[pric+1:segc]
	print enlace
	arreglo.append(enlace)
	segc = 0  
