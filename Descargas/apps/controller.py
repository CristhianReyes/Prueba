# -*- coding: utf-8 -*-

from sys import path
path.append('/home/gramz/sitiopy/apps')

from sitioweb import contacto, ejemplos


def application(environ, start_response):
    peticion = environ['REQUEST_URI']

    if peticion.startswith('/contacto'):
        output = contacto.saludo()
    elif peticion.startswith('/ejemplos'):
        output = ejemplos.variable()
    elif peticion.startswith('/tabla'):
        output = ejemplos.tabla()
    else:
        output = "No se a dónde acceder!!"


    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return output
