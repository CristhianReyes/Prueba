#!/usr/bin/python
import re
import urllib2
import MySQLdb

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

def Inserta(en, ti, des):   
    query = "INSERT INTO Paginas(enlace,titulo,descripcion) VALUES ('%s','%s','%s')" % (en,ti,des) 
    run_query(query) 

def datos(url2): 
    count = 0   
    pos1 = 1    
    fin = 0
    while (count<1) and (pos1 > 0):     
        try:
            response = urllib2.urlopen(url2)
            html = response.read()                  
            if len(html)>0:                       
                pos1 = html.find('<title>',fin)     
                if pos1>=0:                        
                    pos1+7                         
                    fin = html.find ('</title>',pos1) 
                    t1 = html[pos1+7:fin]          
                    fin=fin+9                      
                else:
                    pos1=0                         
                    t1="NULL"                      
                pos1 = html.find('<meta name="description" content="',fin)  
                if pos1>=0:                         
                    pos1=pos1+34
                    fin = html.find ('" />',pos1)
                    d1 = html[pos1:fin]             
                else:
                    contenido="NULL"
            print(url2)     
            print(t1)       
            print(d1)       
            count = count+1 
            Inserta(url2,t1,d1) 
        except:
            pass           


def todos(pagina):          
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
                        
for ur in todos(html):  
    if len(ur) > 0:     
        try:
            print datos(ur) 
            print "---------------------------" 
        except:
            pass            
