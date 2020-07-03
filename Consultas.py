#!/usr/bin/env python

'''
Proyecto [Python]
Consulta de accidentes -Accidentología Vial-
---------------------------
Autor: Diego Farias
Version: 1.1

Descripcion:
Programa creado para la consulta de archivo .csv de 
registro de accidentes viales. Consulta particulares y 
consulta general.
'''

__author__ = "Diego Farias"
__email__ = "dfarias8791@gmail.com"
__version__ = "1.1"


import csv


def test_numeros(numero_inicial, numero_final, test):
    '''
    Función para chequear que el rango desde el numero inicial al numero final ingresados 
    por el usuario se encuentra completo y de no ser asi, reporte los numeros que faltan 
    cargarse. El programa seguirá solo si no falta ningun accidente que cargar en el rango
    especificado.
    ''' 
    
    fo.write('------------Reporte de faltante de accidentes------------------------\n')
    
    accidentes = []

    for i in range((numero_final - numero_inicial) + 1):
        numero = numero_inicial + i
        numero = str(numero)
        accidentes.append(numero)
    
    faltantes = []
    
    for accidente in accidentes:
        marca = False
        for i in range(len(data)):
            if data[i].get('Nº de Accidente') == accidente:
                marca = True
        if marca == False:
            print('Falta accidente',accidente)
            cadena = 'Falta accidente ' + str(accidente) + '\n'
            fo.write(cadena)
            faltantes.append(accidente)
    
    if len(faltantes) != 0:
        test = False
    
    return test      


def seleccion_menu(numero_inicial, numero_final, clave):
    '''
    Función para solicitar desde y hasta que número de accidente se desea consultar o, desde y 
    hasta que fecha se desea consultar. En caso de seleccionar la opcion 1, devuelve dos numeros 
    enteros con los numeros de accidentes seleccionados y en caso de seleccionar la opcion 2 devuelve
    dos numeros enteros que identifica a cada fecha ingresada. 
    '''    
    print('1 - Entre numeros de accidentes')
    print('2 - Entre fechas (NO DISPONIBLE)')
    opcion = int(input('Ingrese su opcion: '))
    if opcion == 1:
        numero_inicial = int(input('Ingrese el numero inicial: '))
        numero_final = int(input('Ingrese el numero final: '))
        clave = 'Nº de Accidente'

    return numero_inicial, numero_final, clave


def lista_accidentes(numero_inicial, numero_final, clave):
    '''
    Funcion para crear una lista de accidentes a evaluar comenzando con el primer numero ingresado
    por el usuario y terminando con el segundo numero ingresado por el usuario en la opción -por
    numero de accidente-. Esta lista se generará en todos los criterios de agrupamiento.
    '''

    if clave == 'Nº de Accidente':
        accidentes = []
        # bucle para hacer una lista de strings con numero de accidentes para comparacion con 
        # archivo .csv
        for i in range((numero_final - numero_inicial) + 1):
            numero = numero_inicial + i
            numero = str(numero)
            accidentes.append(numero)
    
    return accidentes


def por_distrito(numero_inicial, numero_final, clave):
    '''
    Permite agrupar accidentes según el distrito de ocurrencia teniendo en cuenta la opción ingresada
    por el usuario: entre numeros de accidentes o entre fechas.
    '''
    
    distritos = ('Barrancas', 'Cdad de Maipu','Coquimbito','Cruz de Piedra','Fray Luis Beltran','Gral Gutierrez','Lunlunta','Luzuriaga','Microcentro','Ortega','Rodeo Del Medio','Russell','San Roque')
    acum = 0
    
    fo.write('------------Reporte de accidentes por Distrito------------------------\n')

    accidentes = lista_accidentes(numero_inicial, numero_final, clave)
        
    # bucle para buscar los accidentes por distritos        
    for distrito in distritos:
        suma = 0
        for accidente in accidentes:          
            for i in range(len(data)):
                if data[i].get('Nº de Accidente') == accidente:
                    if data[i].get('Distrito') == distrito:
                        suma += 1
        print('Distrito:', distrito, 'cantidad:', suma)
        distrito = str(distrito)
        cadena = 'Distrito: ' + distrito + ': ' + str(suma) + '\n'
        fo.write(cadena)
        acum += suma
           
    print('Cantidad de accidentes:', acum)
    cadena = 'Cantidad de accidentes: ' + str(acum) + '\n'
    fo.write(cadena)


def por_horario(numero_inicial, numero_final, clave):
    '''
    Función para agrupar accidentes por horario de ocurrencia entre un numero
    de accidente inicial y un numero de accidente final.
    '''
    # print(numero_inicial, numero_final, clave)
   
    intervalos_tiempo = ['00:00-02:00','02:01-04:00','04:01-06:00','06:01-08:00','08:01-10:00','10:01-12:00','12:01-14:00','14:01-16:00','16:01-18:00','18:01-20:00','20:01-22:00','22:01-23:59']  
    
    fo.write('------------Reporte de accidentes por Horario------------------------\n')

    accidentes = lista_accidentes(numero_inicial, numero_final, clave) 
     
    for intervalo in intervalos_tiempo:
        acum_0 = acum_1 = acum_2 = acum_3 = acum_4 = acum_5 = acum_6 = acum_7 = acum_8 = acum_9 = acum_10 = acum_11 = 0
        for accidente in accidentes:    
            for i in range(len(data)):
                if data[i].get('Nº de Accidente') == accidente:
                    time = data[i].get('Hora')
                    time = time.split(":")
                    for j in range(3):
                        time[j] = int(time[j])
                    total_time = time[0] * 60 + time[1]
                    if total_time <= 120:
                        acum_0 += 1
                    elif total_time <= 240:
                        acum_1 += 1    
                    elif total_time <= 360:
                        acum_2 += 1
                    elif total_time <= 480:
                        acum_3 += 1
                    elif total_time <= 600:
                        acum_4 += 1
                    elif total_time <= 720:
                        acum_5 += 1
                    elif total_time <= 840:
                        acum_6 += 1
                    elif total_time <= 960:
                        acum_7 += 1
                    elif total_time <= 1080:
                        acum_8 += 1
                    elif total_time <= 1200:
                        acum_9 += 1
                    elif total_time <= 1320:
                        acum_10 += 1
                    else:
                        acum_11 += 1
    
    acumulado = [acum_0, acum_1,acum_2, acum_3, acum_4, acum_5, acum_6, acum_7,acum_8, acum_9,acum_10, acum_11]
    
    for i in range(12):
        print('Horario', intervalos_tiempo[i],'total:',acumulado[i])
        cadena = 'Horario ' + str(intervalos_tiempo[i]) + ', total: ' + str(acumulado[i]) + '\n'
        fo.write(cadena)
    
    print('La cantidad de accidentes son:', sum(acumulado))
    cadena = 'La cantidad de accidentes son: ' + str(sum(acumulado)) + '\n'
    fo.write(cadena)


def por_lugar(numero_inicial, numero_final, clave):
    '''
    Fución para agrupar los accidentes que se toman en dependencia policial y que se toman en 
    lugar del hecho entre rango de dos numeros de accidentes determinados por el usuario.
    '''

    fo.write('------------Reporte de accidentes por donde se toma------------------------\n')

    accidentes = lista_accidentes(numero_inicial, numero_final, clave) 
    
    # clasifica por tomados en el lugar del hecho o en dependencia
    suma_lugar = 0
    suma_depen = 0
    acum = 0
    for accidente in accidentes:
        for i in range(len(data)):
            if data[i].get('Nº de Accidente') == accidente:        
                if data[i].get('En Donde Se Toma') == 'EN LUGAR DEL HECHO':
                    suma_lugar += 1
                else:
                    suma_depen += 1
                acum += 1
    print('Lugar del hecho:', suma_lugar,'\nEn dependencia:', suma_depen)
    cadena = 'En lugar del hecho: ' + str(suma_lugar) + ' / ' + 'En dependencia: ' + str(suma_depen) + '\n' 
    fo.write(cadena)
    print('Cantidad de accidentes:', acum)
    cadena = 'Cantidad de accidetes: ' + str(acum) + '\n'
    fo.write(cadena)

    
def por_consecuencia(numero_inicial, numero_final, clave):
    '''
    Función para agrupar los accidentes que han tenido personas lesionadas y aquellas que no
    han sufrido lesiones en un un rango de dos numeros de accidentes ingresados por el usuario
    '''

    fo.write('------------Reporte de accidentes por Consecuencia------------------------\n')
    
    accidentes = lista_accidentes(numero_inicial, numero_final, clave) 
    
    # clasifica por accidentes con lesiones o sin lesiones
    suma_conlesiones = 0
    suma_sinlesiones = 0
    acum = 0
    for accidente in accidentes:
        for i in range(len(data)):
            if data[i].get('Nº de Accidente') == accidente:        
                if data[i].get('Lesiones') == 'Con Lesiones':
                    suma_conlesiones += 1
                else:
                    suma_sinlesiones += 1
                acum += 1
    print('Con lesiones:', suma_conlesiones,'\nSin lesiones:', suma_sinlesiones)
    cadena = 'Con lesiones: ' + str(suma_conlesiones) + ' / ' + 'Sin lesiones: ' + str(suma_sinlesiones) + '\n' 
    fo.write(cadena)
    print('Cantidad de accidentes:', acum)
    cadena = 'Cantidad de accidetes: ' + str(acum) + '\n'
    fo.write(cadena)

    
def tipo_de_colision(numero_inicial, numero_final, clave):
    '''
    Función para clasificar los accidentes por tipo de colisión en un rango entre un numero
    de accidente inicial y un numero de accidente final ingresados por el usuario.
    '''

    fo.write('------------Reporte de accidentes por Tipo de Colision------------\n')

    accidentes = lista_accidentes(numero_inicial, numero_final, clave) 
    
    # bucle para formar lista con tipos de colision
    tipos_colision = []
    for accidente in accidentes:
        for i in range(len(data)):
            if data[i].get('Nº de Accidente') == accidente:
                marca = False
                colision = data[i].get('Tipo Colision')
                for j in range(len(tipos_colision)):
                    if tipos_colision[j] == colision:
                        marca = True
                if marca == False:
                    tipos_colision.append(colision)
    
    acum = 0
    for tipos in tipos_colision:
        suma = 0
        for accidente in accidentes:
            for i in range(len(data)):
                if data[i].get('Nº de Accidente') == accidente:
                    if data[i].get('Tipo Colision') == tipos:
                        suma += 1
        acum += suma
        print('tipo de colisión:',tipos,':', suma)
        cadena = 'Tipo de colision: ' + str(tipos) + ' = ' + str(suma) + '\n'
        fo.write(cadena)
    print('Cantidad de accidentes procesados:', acum)
    cadena = 'Cantidad de accidentes procesados: ' + str(acum) + '\n'
    fo.write(cadena)


def lugar_hecho(numero_inicial, numero_final, clave):
    '''
    Funcion que clasifica los accidentes segun el lugar de ocurrencia tomando
    los datos de latitud y longitud, acumulando las cantidades de aquellos que
    se repiten
        Planteo del problema:
            1º- Se crea una lista con los numeros de accidentes a evaluar
            2º- Se crean tres listas [latitud] [longitud] [domicilio] que
                registra direcciones solo si estas no se encuentran ya 
                registradas
            3º- Se recorre la listas de longitud y latitud y se realiza el 
                acumulado.
    '''
    # Se abre archivo reporte
    fo.write('------------------Accidentes clasificados por lugar de ocurrencia------------------\n')

    accidentes = lista_accidentes(numero_inicial, numero_final, clave) 

    # bucle para crear las sistas latitud, longitud y direccion si repetir ninguna direccion
    # donde tendran la misma posicion la latitud, la longitud y la direccion cada una en su 
    # respectiva lista
      
    latitud = []
    longitud = []
    direccion = []

    for accidente in accidentes:
        registra = False
        for i in range(len(data)):
            if data[i].get('Nº de Accidente') == accidente:
                for j in range(len(latitud)):
                    if (latitud[j] == data[i].get('Latitud')) and (longitud[j] == data[i].get('Longitud')):
                        registra = True
                if registra == False:
                    latitud.append(data[i].get('Latitud'))
                    longitud.append(data[i].get('Longitud'))
                    direccion.append(data[i].get('Lugar de Accidente'))
        
    # bucle para acumular la cantidad la cantidad de accidentes en cada uno de los lugares
    acum = 0
    for j in range(len(latitud)):
        suma = 0
        for i in range(len(data[i])):
            if (latitud[j] == data[i].get('Latitud')) and (longitud[j] == data[i].get('Longitud')):
                suma += 1
        print(direccion[j], suma)
        cadena = str(direccion[j]) + ' : ' + str(suma) + '\n'
        fo.write(cadena)
        acum += suma
    print('La cantidad de accidentes procesados son: ', acum)   
    cadena = 'La cantidad de accidentes procesados son: ' + str(acum) + '\n'
    fo.write(cadena)
    
   
if __name__ == '__main__':

    # Menú al ingresar
    numero_inicial = 0
    numero_final = 0
    test = True
   
    print('-------------------------------Consultas----------------------------')
    print('1 - Cantidad de accidentes por distrito')
    print('2 - Por horario')
    print('3 - Por lugar donde se toma la denuncia')
    print('4 - Por consecuencia')
    print('5 - Por tipo de colision')
    print('6 - Por lugar de accidente')
    print('7 - General')
    print('8 - Salir')

    with open('Listado_de_accidentes.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
        fo = open('reporte.txt', 'w')

        marca = True
        while marca == True:
            opcion = int(input('Ingrese su opcion: '))
            if opcion == 1:
                numero_inicial, numero_final, clave = seleccion_menu(0, 0, '')
                marca = False
                test = test_numeros(numero_inicial, numero_final, test)
                if test == True:
                    por_distrito(numero_inicial, numero_final, clave)
                else:
                    print('Debe cargar accidentes entre los numeros solicitados, el programa finalizará')
            elif opcion == 2:
                numero_inicial, numero_final, clave = seleccion_menu(0, 0, '')
                marca = False
                test = test_numeros(numero_inicial, numero_final, test)
                if test == True:
                    por_horario(numero_inicial, numero_final, clave)
                else:
                    print('Debe cargar accidentes entre los numeros solicitados, el programa finalizará')
            elif opcion == 3:
                numero_inicial, numero_final, clave = seleccion_menu(0, 0, '')
                marca = False
                test = test_numeros(numero_inicial, numero_final, test)
                if test == True:
                    por_lugar(numero_inicial, numero_final, clave)
                else:
                    print('Debe cargar accidentes entre los numeros solicitados, el programa finalizará')
            elif opcion == 4:
                numero_inicial, numero_final, clave = seleccion_menu(0, 0, '')
                marca = False
                test = test_numeros(numero_inicial, numero_final, test)
                if test == True:
                    por_consecuencia(numero_inicial, numero_final, clave)
                else:
                    print('Debe cargar accidentes entre los numeros solicitados, el programa finalizará')
            elif opcion == 5:
                numero_inicial, numero_final, clave = seleccion_menu(0, 0, '')
                marca = False
                test = test_numeros(numero_inicial, numero_final, test)
                if test == True:
                    tipo_de_colision(numero_inicial, numero_final, clave)
                else:
                    print('Debe cargar accidentes entre los numeros solicitados, el programa finalizará')
            elif opcion == 6:
                numero_inicial, numero_final, clave = seleccion_menu(0, 0, '')
                marca = False
                test = test_numeros(numero_inicial, numero_final, test)
                if test == True:
                    lugar_hecho(numero_inicial, numero_final, clave)
                else:
                    print('Debe cargar accidentes entre los numeros solicitados, el programa finalizará')
            elif opcion == 7:
                numero_inicial, numero_final, clave = seleccion_menu(0, 0, '')
                marca = False
                test = test_numeros(numero_inicial, numero_final, test)
                if test == True:
                    por_distrito(numero_inicial, numero_final, clave)
                    lugar_hecho(numero_inicial, numero_final, clave)
                    por_horario(numero_inicial, numero_final, clave)
                    por_lugar(numero_inicial, numero_final, clave)
                    por_consecuencia(numero_inicial, numero_final, clave)
                    tipo_de_colision(numero_inicial, numero_final, clave)
                else:
                    print('Debe cargar accidentes entre los numeros solicitados, el programa finalizará')
            elif opcion == 8:
                print('Programa terminado...')
                break
            else:
                print('Opcion incorrecta...')
        fo.close() 