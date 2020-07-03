TÍTULO: CONSULTA DE ARCHIVO CSV

NIVEL: PYTHON INICIAL

Introduccion:
El proyecto tiene por objeto extraer datos de archivo .csv siguiendo diferentes criterios de agrupamiento elegidos por el usuario. Se utilizan datos generales correspondientes aaccidentes de tránsito.

Informacion del proyecto:
El presente proyecto se realiza en el marco del curso Python Inicial (nivel 1) de lenguaje Python.

Documentación:
- Archivos: Consultas.py, Listado_de_accidentes.csv y reporte.txt (descargar todos en la misma carpeta).
- Puesta en marcha y uso: al iniciar Consultas.py, se mostrara un menu con los criterios de agrupamiento disponibles. Al seleccionar uno de estos criterios (opcion del 1 al 7), se mostrara un segundo menu para seleccionar entre un rango de numeros de accidentes o entre un rango de fechas (opcion no disponible en esta version). Al seleccionar el rango de accidentes, el archivo evaluara si este rango esta completo (que no falte registrarse ningun accidente), si el rango esta completo el programa seguira con el agrupamiento elegido, si faltan registros el programa informara que registros faltan y terminara. El archivo repote.txt contendra la informacion obtenida por el programa.
Se incluye la opcion General (7) para obtener todos los criterios de agrupamiento disponible en un solo archivo reporte.txt.

Informacion extra:
Se puede probar el funcionamiento del programa eligiendo cualquiera de los criterios de agrupamiento y como numero inicial 2000675 y numero final 2000679, donde el programa realizara la consulta elegida. con el numero inicial 2000670 y numero final 2000671 (rango completo de archivo Listado_de_accidentes.csv) el programa informará los registros faltantes. 