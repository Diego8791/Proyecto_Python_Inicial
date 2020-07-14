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
import inicio_listas


def seleccion_menu():
    '''
    Función para solicitar desde y hasta que número de accidente se desea consultar o, desde y 
    hasta que fecha se desea consultar. En caso de seleccionar la opcion 1, devuelve dos numeros 
    enteros con los numeros de accidentes seleccionados y en caso de seleccionar la opcion 2 devuelve
    dos strings con las fechas ingresadas. 
    '''    
    print('-------------- Seleccione el rango de consulta ------------------')
    print('1 - Entre numeros de accidentes')
    print('2 - Entre fechas')
    print('3 - Salir')
    
    while True:     # se inicia un while para controlar que se elija una opcion correcta, y en caso de no ser asi reiniciar el menu
        opcion = input('Ingrese su opcion: ')
        
        if opcion == '1' or opcion == '2' or opcion == '3':   # se ingresa opcion elegida
            
            if opcion == '1':
                while True:           # se inicia un while para evaluar si el numero inicial y final son ingresos correctos
                    numero_inicial = int(input('Ingrese el numero inicial: '))
                    numero_final = int(input('Ingrese el numero final: '))
                    if numero_inicial <= numero_final:      # si el numero inicial ingresado es mayor que el final el programa continua
                        list_accidentes = inicio_listas.lista_numeros(numero_inicial, numero_final) # llamado al modulo inicio_listas, funcion lista_numeros
                        test = inicio_listas.test_numeros(list_accidentes, data) # llamado al modulo inicio_listas funcion test() para
                                                                                # verificar si el archivo Listado_de_accidentes.csv tiene
                                                                                # todos los registros de accidentes necesarios cargados
                        clave = 'Nº de Accidente'       # clave tomara este valor por la eleccion de la opcion 1 por parte del usuario
                        return list_accidentes, test, clave   # retorno a programa principal
                    else:
                        print('Numero inicial mayor al numero final, rectifique...')  # opcion de numero inicial y final incorrecta, se reinicia el menu para el ingreso de numeros

            elif opcion == '2':                                                              # eleccion por rango de fecha
                print('¡ATENCION!... El sistema no evaluará si faltan cargar accidentes')       # en la opcion por fecha NO SE REALIZA EL TEST para verificar el faltante de registros
                fecha_inicial = input('Ingrese fecha incial (dd-mm-aa, ej 01-01-20): ')     # fecha inicial tipo string
                fecha_final = input('Ingrese fecha final (dd-mm-aa, ej 01-01-20): ')        # fecha final tipo string
                list_accidentes = inicio_listas.lista_fecha(fecha_inicial, fecha_final)       # llamado al modulo inicio_listas funcion lista_fecha()
                test = True                    # como no se realiza el test de verificacion, siempre la variable test sera True, por lo que permitira realizar acciones posteriores
                clave = 'Fecha'                    # correspondiente a la opcion 2 elegida por el usuario
                return list_accidentes, test, clave         # retorno de valor de variables a programa principal
            else:
                return [], False, ''      # retorno de valor de variables a programa principal por haber elegido la opcion 3, con valor de variable test = False para terminar el programa
                break
        else:
            print('Opcion incorrecta')   # reinicia el menu
            

def por_distrito(list_accidentes, clave):
    '''
    Permite agrupar accidentes según el distrito de ocurrencia (distribucion geografica del
    departamento Maipu, provincia de Mendoza) teniendo en cuenta la opción ingresadapor el
    usuario: entre numeros de accidentes o entre fechas.
    '''
    
    distritos = ('Barrancas', 'Cdad de Maipu','Coquimbito','Cruz de Piedra','Fray Luis Beltran','Gral Gutierrez','Lunlunta','Luzuriaga','Microcentro','Ortega','Rodeo Del Medio','Russell','San Roque')
    acum = 0
    
    fo.write('------------Reporte de accidentes por Distrito------------------------\n')
        
    # bucle para buscar los accidentes por distritos        
    for distrito in distritos:            # se recorre cada elemento de la lista distritos
        suma = 0
        for accidente in list_accidentes:                   # Se recorre la lista list_accidentes
            for i in range(len(data)):                      # Se recorre el archivo Listado_de_accidentes.csv 
                if data[i].get(clave) == accidente:         # Se busca los valores de la clave 'Fecha' o 'Nº de Accidente' que coincidan con los elementos de list_accidentes
                    if data[i].get('Distrito') == distrito:   # Se agrupan segun coincidencia con el elemento distrito iterado
                        suma += 1
        print('Distrito:', distrito, 'cantidad:', suma)
        distrito = str(distrito)
        cadena = 'Distrito: ' + distrito + ': ' + str(suma) + '\n' # Se forma cadena para registro en archivo reporte.txt
        fo.write(cadena)
        acum += suma
    
    print('Cantidad de accidentes:', acum)
    cadena = 'Cantidad de accidentes: ' + str(acum) + '\n'
    fo.write(cadena)


def por_horario(list_accidentes, clave):
    '''
    Función para agrupar accidentes por horario de ocurrencia entre un numero
    de accidente inicial y un numero de accidente final p bien entre dos fechas
    solicitadas por el usuario.
    '''
      
    fo.write('------------Reporte de accidentes por Horario------------------------\n')

    intervalos_tiempo = ('00:00-02:00','02:01-04:00','04:01-06:00','06:01-08:00','08:01-10:00','10:01-12:00','12:01-14:00','14:01-16:00','16:01-18:00','18:01-20:00','20:01-22:00','22:01-23:59')   
    acum_0 = acum_1 = acum_2 = acum_3 = acum_4 = acum_5 = acum_6 = acum_7 = acum_8 = acum_9 = acum_10 = acum_11 = 0
    
    for accidente in list_accidentes:    # Se recorre cada elemento de la lista list_accidentes
        for i in range(len(data)):
            if data[i].get(clave) == accidente: # Se buscan los registros cuyos valores coinciden con la clave 'Nº de Accidente' o 'Fecha', segun corresponda, del archivo Listado_de_accidentes.csv
                time = data[i].get('Hora') # se clasifica segun el valor en la clave 'Hora' de los registros en el archivo Listado_de_accidentes.csv
                time = time.split(":")  # se utiliza el metodo split() para transformar el valor string en una lista de elementos 
                for j in range(3):     # se itera en la lista creada anteriormente para obtener un valor entero correspondiente al equivalente en minutos de la hora de ocurrencia 
                    time[j] = int(time[j]) 
                total_time = time[0] * 60 + time[1] 
                if total_time <= 120:      # Se clasifica segun el valor obtenido en minutos
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
        cadena = 'Horario ' + str(intervalos_tiempo[i]) + ', total: ' + str(acumulado[i]) + '\n'  # se forma la cadena para el rigistro en archivo reporte.txt
        fo.write(cadena)
    
    print('La cantidad de accidentes son:', sum(acumulado))
    cadena = 'La cantidad de accidentes son: ' + str(sum(acumulado)) + '\n'
    fo.write(cadena)


def por_lugar(list_accidentes, clave):
    '''
    Fución para agrupar los accidentes que se toman en dependencia policial y que se toman en 
    lugar del hecho (relevamiento pericial) entre rango de dos numeros de accidentes determinados
    o entre dos fechas ingresadas por el usuario.
    '''
    
    fo.write('------------Reporte de accidentes por donde se toma------------------------\n')
    
    # clasifica por tomados en el lugar del hecho o en dependencia
    suma_lugar = 0
    suma_depen = 0
    acum = 0
    for accidente in list_accidentes:  # se recorre cada elemento de la lista list_accidentes
        for i in range(len(data)):
            if data[i].get(clave) == accidente:     # Se buscan registros en Listado_de_accidentes.csv donde la clave 'Nº de Accidente' o 'Fecha' segun corresponda, coincida con el elemento evaluado en list_accidentes
                if data[i].get('En Donde Se Toma') == 'EN LUGAR DEL HECHO': # Se agrupan segun clave 'En Donde Se Toma' en archivo Listado_de_accidentes.csv
                    suma_lugar += 1
                else:
                    suma_depen += 1
                acum += 1
    print('Lugar del hecho:', suma_lugar,'\nEn dependencia:', suma_depen)
    cadena = 'En lugar del hecho: ' + str(suma_lugar) + ' / ' + 'En dependencia: ' + str(suma_depen) + '\n' # Se crea cadena para el registro en archivo reporte.txt
    fo.write(cadena)
    print('Cantidad de accidentes:', acum)
    cadena = 'Cantidad de accidetes: ' + str(acum) + '\n'
    fo.write(cadena)


def por_consecuencia(list_accidentes, clave):
    '''
    Función para agrupar los accidentes que han tenido personas lesionadas y aquellas que no
    han sufrido lesiones en un un rango de dos numeros de accidentes o entre dos fechas
    ingresados por el usuario
    '''

    fo.write('------------Reporte de accidentes por Consecuencia------------------------\n')
    
    # clasifica por accidentes con lesiones o sin lesiones, solo existiendo estas dos opciones posibles.
    suma_conlesiones = 0
    suma_sinlesiones = 0
    acum = 0
    for accidente in list_accidentes:      # Se recorre las la lista list_accidentes
        for i in range(len(data)):
            if data[i].get(clave) == accidente:   # Busca la coincidencia entre el elemento de la lista list_accidentes y clave 'Nº de Accidente' o 'Fecha' segun corresponda en archivo Listado_de_accidente.csv
                if data[i].get('Lesiones') == 'Con Lesiones':     # Se suman las opciones con lesiones en una variable y sin lesiones en otra variable
                    suma_conlesiones += 1
                else:
                    suma_sinlesiones += 1
                acum += 1
    print('Con lesiones:', suma_conlesiones,'\nSin lesiones:', suma_sinlesiones)  # Devuelve resultado
    cadena = 'Con lesiones: ' + str(suma_conlesiones) + ' / ' + 'Sin lesiones: ' + str(suma_sinlesiones) + '\n' # Se forma una cadena para registro en archivo reporte.txt
    fo.write(cadena)
    print('Cantidad de accidentes:', acum)
    cadena = 'Cantidad de accidetes: ' + str(acum) + '\n'
    fo.write(cadena)


def tipo_de_colision(list_accidentes, clave):
    '''
    Función para clasificar los accidentes por tipo de colisión en un rango entre un numero
    de accidente inicial y un numero de accidente final o entre dos fechas ingresados
    por el usuario.
    '''
    
    fo.write('------------Reporte de accidentes por Tipo de Colision------------\n')

    # bucle para formar una lista con tipos de colision, donde se registrara una sola vez cada uno de los
    # tipos de colision, aunque existan varios accidentes con el mismo tipo de colision
    # creando la lista tipos_colision 
    tipos_colision = []
    
    for accidente in list_accidentes:           # Se recorre la lista list_accidentes
        for i in range(len(data)):      
            if data[i].get(clave) == accidente:         # Compara la clave 'Fecha' o 'Nº de Accidente' segun corresponda con cada elemento de list_accidentes
                marca = False
                colision = data[i].get('Tipo Colision')    
                for j in range(len(tipos_colision)):    # Se busca si ya existe un elemento con el tipo de colision en lista tipos_colision, de no existir lo registra
                    if tipos_colision[j] == colision:
                        marca = True
                if marca == False:
                    tipos_colision.append(colision)
    
    # Agrupamiento por tipo de colision, utilizando las listas tipos_colision
    # y list_accidentes y el archivo Lista_de_accidentes.csv
    acum = 0
    for tipos in tipos_colision:
        suma = 0
        for accidente in list_accidentes:
            for i in range(len(data)):
                if data[i].get(clave) == accidente:     
                    if data[i].get('Tipo Colision') == tipos:
                        suma += 1
        acum += suma
        print('tipo de colisión:',tipos,':', suma)
        cadena = 'Tipo de colision: ' + str(tipos) + ' = ' + str(suma) + '\n' # Se crea la cadena para ser registrado en el 
                                                                              # archivo reporte.txt por cada tipo de colision
        fo.write(cadena)
    print('Cantidad de accidentes procesados:', acum)    # Devuelve el total de archivos procesados.
    cadena = 'Cantidad de accidentes procesados: ' + str(acum) + '\n'
    fo.write(cadena)  


def lugar_hecho(list_accidentes, clave):
    '''
    Funcion que clasifica los accidentes segun el domicilio de ocurrencia tomando
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

    fo.write('------------------Accidentes clasificados por lugar de ocurrencia------------------\n')

    # bucle para crear las sistas latitud, longitud y direccion si repetir ninguna direccion
    # donde tendran la misma posicion la latitud, la longitud y la direccion cada una en su 
    # respectiva lista
      
    latitud = []
    longitud = []
    direccion = []

    for accidente in list_accidentes:                # Recorre list_accidentes
        registra = False
        for i in range(len(data)):                      # Recorre archivo Listado_de_accidentes.csv
            if data[i].get(clave) == accidente:         # Evalua si la clave 'Nº de Accidente' o 'Fecha' coincide con el elemento en list_accidentes
                for j in range(len(latitud)):           # Recorre la lista latitud
                    if (latitud[j] == data[i].get('Latitud')) and (longitud[j] == data[i].get('Longitud')): 
                        registra = True                 # Si en la lista latitud y longitud encuentra elementos idénticos a los valores 'Latitud' y 'Longitud', no se realiza agrega
                if registra == False:                   # Si no se encuentra el valor de latitud y longitud se registra en las listas latitud, longitud y direccion
                    latitud.append(data[i].get('Latitud'))
                    longitud.append(data[i].get('Longitud'))
                    direccion.append(data[i].get('Lugar de Accidente'))

    # bucle para acumular la cantidad la cantidad de accidentes en cada uno de los domicilios
    acum = 0                                                                            # Se recorren las listas y el archivo Listado_de_accidentes para agrupar por cada domicilio
    for j in range(len(latitud)):
        suma = 0
        for i in range(len(data)):
            if (latitud[j] == data[i].get('Latitud')) and (longitud[j] == data[i].get('Longitud')):
                suma += 1
        print(direccion[j], suma)
        cadena = str(direccion[j]) + ' : ' + str(suma) + '\n'
        fo.write(cadena)                    # Se escribe en archivo reporte.txt
        acum += suma
    print('La cantidad de accidentes procesados son: ', acum)               # Se informa la cantidad de accidentes procesados
    cadena = 'La cantidad de accidentes procesados son: ' + str(acum) + '\n'
    fo.write(cadena)


if __name__ == '__main__':
 
    with open('Listado_de_accidentes.csv') as csvfile:
        fo = open('reporte.txt', 'w')
        data = list(csv.DictReader(csvfile))
        list_accidentes, test, clave = seleccion_menu()  # llamado a la funcion seleccion_menu
        
        # si la variable booleana test tiene el valor False, el programa no permitira realizar otra accion por lo que terminara
        while test == True:     # comienzo de while siempre que la variable test sea True   
            print('-------------------------------Consultas----------------------------')
            print('1 - Cantidad de accidentes por distrito')
            print('2 - Por horario')
            print('3 - Por lugar donde se toma la denuncia')
            print('4 - Por consecuencia')
            print('5 - Por tipo de colision')
            print('6 - Por lugar de accidente')
            print('7 - General')
            print('8 - Salir')
            print('---------------------------------------------------------------------')
        
            opcion = int(input('Ingrese su opcion: '))
            if opcion == 1:
                por_distrito(list_accidentes, clave)
                print('Programa terminado')
                test = False
            elif opcion == 2:
                por_horario(list_accidentes, clave)
                print('Programa terminado')
                test = False
            elif opcion == 3:
                por_lugar(list_accidentes, clave)
                print('Programa terminado')
                test = False
            elif opcion == 4:
                por_consecuencia(list_accidentes, clave)
                print('Programa terminado')
                test = False
            elif opcion == 5:
                tipo_de_colision(list_accidentes, clave)
                print('Programa terminado')
                test = False
            elif opcion == 6:
                lugar_hecho(list_accidentes, clave)
                print('Programa terminado')
                test = False
            elif opcion == 7:
                por_distrito(list_accidentes, clave)
                por_horario(list_accidentes, clave)
                por_lugar(list_accidentes, clave)
                por_consecuencia(list_accidentes, clave)
                tipo_de_colision(list_accidentes, clave)
                lugar_hecho(list_accidentes, clave)
                print('Programa terminado')
                test = False
            elif opcion == 8:
                break
            else:
                print('Opción inválida')
        
        fo.close()
        
