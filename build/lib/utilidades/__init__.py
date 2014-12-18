#!/usr/bin/env python

try:
    import requests
except ImportError:
    print ("No tienes la biblioteca requests, necesitada por utilidades.")
    print ("Prueba a instalarla con (sudo) pip install requests")

UTILIDADES_OK           =0
UTILIDAD_TAM_BUFFER     =4096

def descargar_archivo(url, nombre_archivo_destino):
    peticion=requests.get(url)
    with open(nombre_archivo_destino, 'wb') as fd:
        for chunk in peticion.iter_content(UTILIDAD_TAM_BUFFER):
            fd.write(chunk)
    return UTILIDADES_OK


