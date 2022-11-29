import csv
import datetime
import random
from lib import _Examen, _Aula

examenes = []
with open('./Data/Dic 2022 - Feb-Mar 2023-Table 1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader)
    for row in csv_reader:
            examenes.append(
                _Examen(row[0], row[1], row[2], row[5], row[6], random.randrange(15, 110))
            )

temp_sorted_list = sorted(examenes, key=lambda x: (x.inscriptos), reverse= True)
sortedList = sorted(temp_sorted_list, key=lambda x: (x.fecha, x.hora))

# print("cantidad de examenes cargados: ",len(examenes))
# print("cantidad de examenes cargados: ",len(sortedList))

# for examen in sortedList:
#     examen.imprimir_info()


aulas = []
with open('./Data/RELEVAMIENTO DE AULAS - AULA.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        aulas.append(
            _Aula(row[1], row[2], row[4])
        )

sortedList_aulas = sorted(aulas, key=lambda x: x.capacidad)  

for aula in sortedList_aulas:
    aula.imprimir_info()

fecha_prueba = datetime.date(2022,12,12)

# for aula in sortedList_aulas:
#     for examen in sortedList:
#         print(fecha_prueba)
#         exam_date = (datetime.date(examen.fecha.year, examen.fecha.month, examen.fecha.day))
#         if aula.capacidad >= examen.inscriptos :
#             print("cumple condicion 1")
            # if datetime.date(examen.fecha) == fecha_prueba:
            #     print("cumple condicion 2 tambien")

