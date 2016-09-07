#!/usr/bin/python
import re
import urllib2
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'database'
DB_NAME = 'web2'                        #Mi bd se llama web2

def run_query(query=''):                #La función que mostró el ingeniero para hacer la conexion
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

def Inserta(en, ti, des):   #En esta funcion recibo los parametros que se insertan en la bd
    query = "INSERT INTO Paginas(enlace,titulo,descripcion) VALUES ('%s','%s','%s')" % (en,ti,des) #Insert Into Paginas *Paginas* es mi tabla y enlace,tutulo y descripcion mis atributos, cada (%s) es la cantidad de valores que se van a ingresar, luego se pone %(con los valores que representan cada %s)
    run_query(query) #Mandamos la consulta

def datos(url2): #Funcion para buscar los titulos, y la descripcion del link encontrado en la funcion todos *Mas abajo está la funcion*
    count = 0   #contador inicializado en 0 para que se cumpla el while y solo se repita 2 veces la funcion
    pos1 = 1    #Posicion 1 inicializada en 1 para que se cumpla el while
    fin = 0
    while (count<1) and (pos1 > 0):     #Las codiciones del While
        try:
            response = urllib2.urlopen(url2)
            html = response.read()                  #Se lee la pagina recibida de la funcion todos
            if len(html)>0:                         #se verifica que la pagina tenga contenido o se pueda acceder
                pos1 = html.find('<title>',fin)     #Busca en html el tutulo desde la posicion 0
                if pos1>=0:                         #Si se encontro el titulo la posicion tiene que ser mayor a 0
                    pos1+7                          #Se le suman 7 espacions que son los que ocupa <title>
                    fin = html.find ('</title>',pos1) #buscamos el cierre de la etiqueta
                    t1 = html[pos1+7:fin]           #guardamos en una variable el titulo
                    fin=fin+9                       #se le suman 9 espacios a la posicion final
                else:
                    pos1=0                          #Si no se encuentra el titulo
                    t1="NULL"                       #el titulo va a ser igual a nulo
                pos1 = html.find('<meta name="description" content="',fin)  #Buscamos la descripcion de la pagina
                if pos1>=0:                         #El mismo proceso del titulo
                    pos1=pos1+34
                    fin = html.find ('" />',pos1)
                    d1 = html[pos1:fin]             #Guardamos la descripcion en las posiciones encontradas
                else:
                    contenido="NULL"
            print(url2)     #Imprimimos en la consola el url recibido de la funcion todos
            print(t1)       #imprimimos el titulo encontrado en esta Funcion
            print(d1)       #imprimimos la descripcion encontrada en esta funcion
            count = count+1 #Sumamos 1 al count
            Inserta(url2,t1,d1) #llamamos la funcion inserta y le enviamos los parametros encontrados
        except:
            pass            #Por cualquier error, simplemente salta


def todos(pagina):          #Esta funcion fue la de buscar el href, de la pagina python.org
    href = 1
    fin = 0
    miurl = []
    while href > 0:
        href = pagina.find('<a href=',fin)
        inicio = pagina.find('"',href)
        fin = pagina.find ('"',inicio + 1)
        patronhttps = re.compile ("http[s]*")
        if patronhttps.findall (pagina[inicio+1:fin]):
            miurl.append (pagina[inicio+1:fin])
    return miurl

response = urllib2.urlopen('http://python.org/')
html = response.read()
                        #Hasta aquí!!
for ur in todos(html):  #En la variable ur se guarda el zelda encontrado en la funcion todos
    if len(ur) > 0:     #Si la pagina tiene mas de 0 caracteres
        try:
            print datos(ur) #Imprime los datos encontrados en la funcion datos (la primera funcion, donde buscamos el titulo y la descripcion)
            print "---------------------------" #Linea separadora n.n
        except:
            pass            #si la url econtrada no contiene nada... solo pasa!
