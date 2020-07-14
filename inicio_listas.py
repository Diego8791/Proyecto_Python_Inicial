#!/usr/bin/env python

'''
Proyecto [Python]
Consulta de accidentes -Accidentología Vial-
---------------------------
Autor: Diego Farias
Version: 1.1

Descripcion:
Programa creado para generar una lista de fechas para consulta de archivo .csv de 
registro de accidentes viales.
'''

__author__ = "Diego Farias"
__email__ = "dfarias8791@gmail.com"
__version__ = "1.1"


import datetime                             # se importa modulo datetime para realizar la diferencia entre fechas
from datetime import date, timedelta  
import consultas
import csv


def lista_numeros(numero_inicial, numero_final):
    '''
    Funcion para crear una lista de accidentes a evaluar comenzando con el primer numero ingresado
    y terminando con el segundo numero ingresado por el usuario, generando una lista
    de n elementos entre numero inicial y numero final, incrementando de 1 en 1 y retornando la lista
    list_accidentes con elementos tipo string. 
    '''
       
    # bucle para hacer una lista de strings con numero de accidentes para comparacion con archivo .csv
    list_accidentes = []

    for i in range((numero_final - numero_inicial) + 1): 
        numero = numero_inicial + i             # elemento 
        numero = str(numero)                    # conversion de elemento a string (se hace porque los valores de la clave 
                                                #'Nº de Accidente' son strings)
        list_accidentes.append(numero)           # se agrega el elemento a la lista list_accidentes
    
    return list_accidentes     # retorno de la lista list_accidentes con numeros de accidentes a evaluar


def test_numeros(list_accidentes, data):
    '''
    Función para chequear que el rango desde el numero inicial al numero final ingresados 
    por el usuario se encuentra completo en el archivo csv y de no ser asi, reporte los numeros
    que faltan cargarse. El programa seguirá solo si no falta ningun accidente que cargar en el
    rango especificado.
    ''' 
    
    fo = open('reporte.txt', 'w')
    fo.write('------------Reporte de faltante de accidentes------------------------\n')
    test = True           
    for numero in list_accidentes:      # para cada elemento de list_accidentes se verificara si se encuentra en 
                                        # el archivo Listado_de_accidentes.csv
        marca = False
        for i in range(len(data)):
            if data[i].get('Nº de Accidente') == numero:
                marca = True                   # si se encuentra el numero de accidente la variable marca tomara el valor True
        if marca == False:                      # si no se encuentra el elemento, marca no cambiara de valor y el programa
                                                # informara al usuario  el faltante del registro 
            cadena = 'Falta accidente ' + str(numero) + '\n'  # cadena para archivo reporte.txt
            fo.write(cadena)
            print(cadena)
            test = False    # la variable test toma el valor False siempre que falte al menos un accidente en archivo csv, por lo que
                            # el programa solo informara los registros faltantes, no permitiendo realizar otra accion
    if marca == False:
        print("Cargue los accidentes detallados, el programa finalizará")
        cadena = "Cargue los accidentes detallados, el programa finalizará"
        fo.write(cadena)
        
    return test      # retorno del valor de la variable test


def lista_fecha(fecha_inicial, fecha_final):
    '''
    Funcion para construir una lista de elementos tipo strings con las fechas iniciando en la fecha inicial ingresada por el
    usuario y terminando con la fecha final tambien ingresada por el usuario. El formato de fecha_inicial y fecha_final es 
    un elemento tipo string con el formato 'dd-mm-aa', y la funcion debe devolver una lista (list_accidentes) con elementos tipo
    strings con el formato 'dd-Mmm-aa' donde el mes son las tres primeras letras del mes correspondiente, la primera de ellas
    en mayuscula, por ejemplo 01-Ene-20, siendo este formato el que contiene los valores de la clave 'Fecha' en archivo 
    Listado_de_accidentes.csv
    '''
    
    # dar formato para determinar la diferencia en dias entre las fechas
    lista = []                                 # lista local 
    # para fecha inicial
    fecha_1 = fecha_inicial                    
    fecha_1 = fecha_1.split('-')               # se crea una lista con el metodo split()
    for i in range(len(fecha_1)):              # se convierte a los elementos en enteros
        fecha_1[i] = int(fecha_1[i])
    f1 = date(fecha_1[2], fecha_1[1], fecha_1[0])   # se utiliza la funcion date para dar formato de fecha para, a posterior
                                                    # realizar resta de fechas
    lista.append(f1)                                # se agrega el elemento a lista
    
    # para fecha final (idem anterior, con la salvedad que no se agrega a lista)
    fecha_2 = fecha_final               
    fecha_2 = fecha_2.split('-')
    for i in range(len(fecha_2)):
        fecha_2[i] = int(fecha_2[i])
    f2 = date(fecha_2[2], fecha_2[1], fecha_2[0])

    diferencia = f2 - f1                # resta de fechas para obtener la cantidad de dias de diferencia entre la fecha 
                                        # inicial y la fecha final

    diferencia = int(diferencia.days)   # la diferencia de dias entre fecha inicial y fecha final se conviente en entero para 
                                        # usarse en el range posterior
    
    fecha = f1
    # formar lista entre dos fechas
    for i in range(diferencia):
        fecha = fecha + timedelta(days=1)      # incremento de 1 dia entre cada iteracion 
        lista.append(fecha)                    # agregar el elemento a lista

    # Diccionario para cambiar el formato numerico al formato alfabetico del mes
    mes = {'01':'Ene','02':'Feb','03':'Mar','04':'Abr','05':'May','06':'Jun','07':'Jul',
    '08':'Ago','09':'Sep','10':'Oct','11':'Nov','12':'Dic'}

    # dar formato de salida
    list_accidentes = []    
    for fecha in lista:               # para cada elemento de lista
        fecha = str(fecha)            # dar formato string a la fecha
        fecha = fecha[2:]             # solo se tendra en cuenta los ultimos dos digitos del año (Ejemplo: no 2020, sino solo 20)
        fecha = fecha.split("-")      # aplicacion del metodo split()
        for k, v in mes.items():      # cambiar formato numérico de mes por el formato alfabético utilizando diccionario mes
            if fecha[1] == k:
                fecha[1] = v
        fecha = fecha[2] + "-" + fecha[1] + "-" + fecha[0] # concatenar y acomodar los elementos al formato dd-Mmm-aa  
        list_accidentes.append(fecha)    # agrega elemento a list_accidentes
            
    return list_accidentes      # retorno list_accidentes
