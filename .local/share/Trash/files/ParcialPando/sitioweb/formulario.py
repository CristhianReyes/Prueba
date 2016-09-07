# -*- coding: 850 -*-
import re
import urllib2
import MySQLdb
import cgi

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'database'
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
            <p>¿Qué deseas buscar?: <input type=\"text\" name=\"nombre\" value=\"\"/></p>\
            <p><input type=\"submit\" value=\"Buscar\"/></p>\
            </form>"
    return texto

def recibe(parametros):
    texto = parametros['QUERY_STRING']
    texto = texto[7:len(texto)]
    query="SELECT * FROM Paginas WHERE titulo LIKE '%"+texto+"%' OR descripcion LIKE '%"+texto+"%' OR enlace LIKE '%"+texto+"%'"
    resultado = run_query(query)
    tabla = "<table style=\"width:100%\"> "
    for fila in resultado:
        dato1 = str(fila[0])
        dato2 = str(fila[1])
        dato3 = str(fila[2])
        dato4 = str(fila[3])
        tabla += "<tr> \
                        <tr>\
                        <td>"+ dato3+ "</td>\
                        </tr>\
                        <tr>\
                        <td><a>"+ dato2 + "</a></td>\
                        </tr>\
                        <tr>\
                        <td>"+ dato4 + "</td>\
                        </tr>\
                        <tr>\
                        <td>""</td>\
                        </tr>\
                        <td>""</td>\
                        </tr>\
                    </tr>"
    tabla += " </table>"
    return tabla


#    for fila in resultado:
#        dato1 = str(fila[0])
#        dato2 = str(fila[1])
#        dato3 = str(fila[2])
#        dato4 = str(fila[3])
#        res ="<p>Valor: "+dato2+" , "+dato3+" , " +dato4+"</p>"
#        return res
#    print str(fila[0]), " - " , str(fila[1]).strip(), " (", str(fila[2]).strip(), ")", str(fila[3])
#print(resultado)
    #texto ="<p>Valor: " +resultado + "</p>"


#def recibe(parametros):
#    texto = parametros['QUERY_STRING']
#    texto = texto[7:len(texto)]
#    query="SELECT * FROM Paginas WHERE titulo LIKE '%"+texto+"%' OR descripcion LIKE '%"+texto+"%' OR enlace LIKE '%"+texto+"%'"
#    resultado=run_query(query);
#
#    tabla = " <table style=\"width:100%\">"
#
#    for x in range(0,len(resultado)):
#        tabla += "<tr> \
#                        <td>"+ str(resultado[x][0]) + "</td>\
#                        <td>"+ str(resultado[x][1]) + "</td>\
#                        <td>"+ str(resultado[x][2]) + "</td>\
#                        <td>"+ str(resultado[x][3]) + "</td>\
#                        <td>"+ str(resultado[x][4]) + "</td>\
#                    </tr>"
#
#    tabla += " </table>"
#    return tabla
