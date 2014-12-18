#!/usr/bin/python3
# -*- coding: utf-8 -*-

UTILIDADES_OK           =0
UTILIDAD_TAM_BUFFER     =4096

import importlib
import os

from datetime import date, timedelta


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

def existe_fichero(nombre_fichero):
    if (os.path.isfile(nombre_fichero)):
        return True
    return False

"""Descarga un archivo desde una url y lo guarda en el nombre de archivo indicado"""
def descargar_archivo(url, nombre_archivo_destino):
    peticion=requests.get(url)
    with open(nombre_archivo_destino, 'wb') as fd:
        for chunk in peticion.iter_content(UTILIDAD_TAM_BUFFER):
            fd.write(chunk)
    return UTILIDADES_OK

"""Descarga un archivo desde una URL solo en el caso de que el archivo no existiera"""
def descargar_archivo_si_no_existe(url, nombre_archivo_destino):
    if (existe_fichero(nombre_archivo_destino)):
        return
    return descargar_archivo(url, nombre_archivo_destino)

"""Genera una lista de fechas empezando en cierto día del año y hasta el dia de hoy"""
def generar_lista_fechas(dia, mes, anio):
    #Formato:
    # %Y año con cuatro cifras
    # %m mes con dos cifras
    # %d dia con dos cifras
    # %a Dia de la semana en idioma local "Sun", "Mon"
    # %A Dia de la semana en idioma local "Sunday", "Monday"
    
    formato="%Y%m%d"
    lista_fechas=[]
    fecha=date(anio, mes, dia)
    hoy=date.today()
    incremento=timedelta(days=1)
    while (fecha<=hoy):
        lista_fechas.append(fecha.strftime(formato))
        fecha=fecha+incremento
    return lista_fechas

class LibroExcel(object):
    """Abrir un archivo Excel que se asume que está en formato Unicode (Excel 97 y posteriores)"""
    def __init__(self, nombre_archivo_excel):
        self.nombre_archivo=nombre_archivo_excel
        self.libro=xlrd.open_workbook(nombre_archivo_excel)
    """Indica de que hoja vamos a leer celdas, la primera es la 0"""
    def marcar_hoja_como_activa(self, num_hoja):
        self.hoja=self.libro.sheet_by_index(num_hoja)
        
    def leer_celda(self, fila, columna):
        if (self.hoja==None):
            raise IOError("No hay hojas activas (¿olvidó llamar a marcar_hoja_como_activa)")
        
        valor_celda=self.hoja.cell_value(fila, columna)
        return valor_celda
    


