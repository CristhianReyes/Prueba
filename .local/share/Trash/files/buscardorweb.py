#!/usr/bin/python
import re
import urllib2
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'futbol'
DB_NAME = 'webs'

def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conexion = MySQLdb.connect(*datos)
    cursor = conexion.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()
    else:
        conexion.commit()
        data = None

    cursor.close()
    conexion.close()

    return data

def insertar(en, ti, de):
  query = "insert into pages(enlace, titulo, descripcion) values ('%s', '%s', '%s')" % (en, ti, de)
  run_query(query)

def datos(paginas):
  count = 0
  posicion = 1
  fin = 0
  while (count<1) and (posicion > 0):
    try:
      response = urllib2.urlopen(paginas)
      html = response.read()
      if len(html)>0:
        posicion = html.find('<title>', fin)
        if posicion>=0:
            posicion+7
            fin = html.find('</title', posicion)
            p = html[posicion + 7 :fin]
            fin = fin+9
        else:
            posicion=0
            p ="NULL"
        posicion = html.find('<meta name="description" content="',fin)
        if posicion>= 0:
            posicion=posicion+34
            fin = html.find ('" />', posicion)
            po = html[posicion:fin]
        else:
	    insertar(paginas, p, po)
            con="NULL"
      
      print(paginas)
      print(p)
      print(po)
      count = count+1
      
    except:
      pass

def todos(pag):
    href = 1
    fin = 0
    urlls = []
    while href > 0:
        href = pag.find('<a href=', fin)
        inicio = pag.find('"', href)
        fin = pag.find ('"', inicio + 1)
        http = re.compile ("http[s]*")
        if http.findall (pag[inicio+1:fin]):
            urlls.append (pag[inicio+1:fin])
    return urlls

response = urllib2.urlopen('http://python.org/')
html = response.read()

for x in todos(html):
    if len(x) > 0:
        try:
            print datos(x)
            print "-----------------------------------------"
        except:
            pass
