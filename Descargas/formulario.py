def envia():
    texto = "<form action=\"http://python-web/recibe\" method=\"get\">\
            <p>Tu nombre: <input type=\"text\" name=\"nombre\" value=\"\"/></p>\
            <p><input type=\"submit\" value=\"Enviar\"/></p>\
            </form>"
    return texto


def recibe(parametros):
    texto ="<p>Valor:" +parametros['QUERY_STRING'] + "</p>"
    return texto
