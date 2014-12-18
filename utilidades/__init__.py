#!/usr/bin/env python


UTILIDADES_OK           =0
UTILIDAD_TAM_BUFFER     =4096

import importlib


def importar_paquete(nombre):
    try:
        importlib.import_module(nombre)
    except ImportError:
        imprimir_error_importacion(nombre)
def imprimir_error_importacion(nombre_paquete):
    print ("No tienes la biblioteca {0}, necesitada por utilidades.".format(nombre_paquete))
    print ("Prueba a instalarla con (sudo) pip install {0}".format(nombre_paquete))
#Añade a esta lista cualquier nombre de paquete que necesites
paquetes_necesarios=["requests", "xlrd"]
for paquete in paquetes_necesarios:
    importar_paquete(paquete)



    
#########################################################################################
#
#                                 Código de la librería
#
#########################################################################################


"""Descarga un archivo desde una url y lo guarda en el nombre de archivo indicado"""
def descargar_archivo(url, nombre_archivo_destino):
    peticion=requests.get(url)
    with open(nombre_archivo_destino, 'wb') as fd:
        for chunk in peticion.iter_content(UTILIDAD_TAM_BUFFER):
            fd.write(chunk)
    return UTILIDADES_OK




class LibroExcel(object):
    """Abrir un archivo Excel que se asume que está en formato Unicode (Excel 97 y posteriores)"""
    def __init__(self, nombre_archivo_excel):
        self.nombre_archivo=nombre_archivo_excel
        self.libro=xlrd


