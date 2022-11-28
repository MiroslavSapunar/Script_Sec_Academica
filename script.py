import csv
import datetime
import random

class _Examen:
    def __init__(self, fecha, inscriptos = 0):
        self.fecha = fecha
        self.inscriptos = inscriptos

    def checkear_fecha_examen_invalida(self):
        fecha = datetime.datetime.date(self.fecha)

        fecha_uno = datetime.date(2022,12,8)
        fecha_dos = datetime.date(2022,12,9)
        fecha_tres = datetime.date(2022,12,24)

        return fecha == fecha_uno or fecha == fecha_dos or fecha == fecha_tres

    def imprimir_info(self):
        print(f'fecha: {self.fecha}, incriptos: {self.inscriptos}')

class _Materia:
    def __init__(self, codigo=0, nombre=0):
        self.codigo = codigo
        self.nombre = nombre
        self.examenes = []

    def agregar_fecha(self, fecha):
        self.examenes.append(_Examen(fecha, random.randrange(15, 150)))

    def obtener_examenes(self):
        return self.examenes

    def optener_codigo(self):
        return self.codigo

    def checkear_codigo(self, codigo):
        return self.codigo == codigo

    def checkear_fechas_validas(self):
        fechas_validas = True
        for examen in self.examenes:
            if examen.checkear_fecha_examen_invalida():
                print("no cumple fecha")
                fechas_validas = False

        return fechas_validas

    def imprimir_info(self):
        print(f'codigo: {self.codigo}, nombre: {self.nombre}')
        for examen in self.examenes:
            examen.imprimir_info()

materias = []

with open('./Data/Dic 2022 - Feb-Mar 2023-Table 1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader)
    for row in csv_reader:
        if not any(materia.checkear_codigo(row[0]) for materia in materias):
            materias.append(
                _Materia(row[0], row[1])
            )
        materias[-1].agregar_fecha( datetime.datetime.strptime(row[5] + row[6], '%m/%d/%y%H:%M:%S %p'))

    cantidad_examenes = 0
    for materia in materias:
        if not materia.checkear_fechas_validas():
            materia.imprimir_info()

        cantidad_examenes += len(materia.obtener_examenes())

    print("cantidad de materias cargadas: ",len(materias))
    print("cantidad de examenes cargados: ",cantidad_examenes)

# with open('./Data/RELEVAMIENTO DE AULAS - AULA.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Las columnas de archivo son: {" - ".join(row)}')
#             line_count += 1
#         else:
#             print(f'Sede: {row[0]}, piso: {row[1]}, aula nº: {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')
