# -*- coding: 850 -*-
import re
import urllib2
import MySQLdb
import cgi

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'futbol'
DB_NAME = 'web2'

def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos)
    cursor = conn.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()
    else:
        conn.commit()
        data = None

    cursor.close()
    conn.close()

    return data

def envia():
    texto = "<form action=\"http://python-web/recibe\" method=\"get\">\
            <p> Escriba palabra a Buscar: <input type=\"text\" name=\"nombre\" value=\"\"/></p>\
            <p><input type=\"submit\" value=\"Buscar\"/></p>\
            </form>"
    return texto

def recibe(parametros):
    texto = parametros['QUERY_STRING']
    texto = texto[7:len(texto)]
    query="SELECT enlace, titulo, descripcion FROM Paginas WHERE titulo LIKE '%"+texto+"%' OR descripcion LIKE '%"+texto+"%' OR enlace LIKE '%"+texto+"%'"
    resultado = run_query(query)
    tabla = "<table style=\"width:100%\"> "
    for fila in resultado:
        dato1 = str(fila[0])
        dato2 = str(fila[1])
       tabla += "<tr> \
                        <tr>\
                        <td>"+ dato1+ "</td>\
                        </tr>\
                        <tr>\
                        <td><a>"+ dato2 + "</a></td>\
                        </tr>\
                        <tr>\
                        <td>"+ "Resultados" + "</td>\
                        </tr>\
                        <tr>\
                        <td>" "</td>\
                        </tr>\
                        <td>""</td>\
                        </tr>\
                    </tr>"
    tabla += " </table>"
    return tabla
