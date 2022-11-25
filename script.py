import csv
import datetime
import random

class Materia:
    def __init__(self, codigo=0, nombre=0):
        self.codigo = codigo
        self.nombre = nombre
        self.examenes = []

    def agregar_fecha(self, fecha):
        self.examenes.append(Examen(fecha, random.randrange(15, 150)))

    def obtener_examenes(self):
        return self.examenes

    def optener_codigo(self):
        return self.codigo

    def checkear_codigo(self, codigo):
        return self.codigo == codigo
    
    def imprimir_info(self):
        print(f'codigo: {self.codigo}, nombre: {self.nombre}')
        for examen in self.examenes:
            examen.imprimir_info()

class Examen:
    def __init__(self, fecha, inscriptos = 0):
        self.fecha = fecha
        self.inscriptos = inscriptos

    def imprimir_info(self):
        print(f'fecha: {self.fecha}, incriptos: {self.inscriptos}')

        


materias = []

with open('./Data/Dic 2022 - Feb-Mar 2023-Table 1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    # header = next(csv_reader)
    next(csv_reader)
    # print(header)
    # line_count = 0
    for row in csv_reader:
        if not any(materia.checkear_codigo(row[0]) for materia in materias):
            materias.append(
                Materia(row[0], row[1])
            )
        materias[-1].agregar_fecha( datetime.datetime.strptime(row[5]+ "-" + row[6], '%m/%d/%y-%H:%M:%S %p'))


    for materia in materias:
        materia.imprimir_info()

    print("cantidad de materias cargadas: ",len(materias))

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
