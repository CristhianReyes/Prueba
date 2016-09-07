def variable():
    texto = 'Texto desde una variable'
    salida =  "<p>Este es el <b>" + texto + " </b>!!!</p>"
    return salida


def tabla ():

    tabla = "<table style=\"width:100%\"> "

    for x in range(1,20):
        tabla += "<tr> \
                        <td>"+ str(x) + "</td>\
                        <td>"+ str(x*50) + "</td>\
                    </tr>"
    tabla += " </table>"
    return tabla
