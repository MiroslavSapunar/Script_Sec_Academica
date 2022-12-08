import csv
import datetime
import random
from lib import _Examen, _Aula

codigos = []
with open('./Data/codigos_materias.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader)
    for row in csv_reader:
            codigos.append(row[0])

# for codigo in codigos:
#     print(codigo)

december = datetime.date(2022,12,31)

examenes = []
# with open('./Data/Dic 2022 - Feb-Mar 2023-Table 1.csv') as csv_file:
# with open('./Data/Dic 2022.csv') as csv_file:
with open('./Data/Mesas_12_2022-03_2023.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
            if datetime.datetime.date(datetime.datetime.strptime(row[3], "%d/%m/%Y")) <= december:
                if any(row[0] == codigo for codigo in codigos):
                    examenes.append(
                        _Examen(row[0], row[1], row[2], row[3], row[4], random.randrange(15, 110), any(row[0] == codigo for codigo in codigos))
                    )

temp_sorted_list = sorted(examenes, key=lambda x: (x.inscriptos), reverse= True)
sortedList = sorted(temp_sorted_list, key=lambda x: (x.fecha, x.hora))

print(f'cantidad examenes: {len(sortedList)}')
# for examen in sortedList:
#     examen.imprimir_info()

aulas = []
# with open('./Data/RELEVAMIENTO DE AULAS - AULA.csv') as csv_file:
with open('./Data/RELEVAMIENTO DE AULAS - AULA_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        aulas.append(
            _Aula(row[1], row[2], row[4])
        )

sortedList_aulas = sorted(aulas, key=lambda x: x.capacidad)  

print(f'cantidad aulas: {len(sortedList_aulas)}')
# for aula in sortedList_aulas:
#     aula.imprimir_info()

fecha_prueba = datetime.date(2022,12,12)

no_asignados = []
for examen in sortedList:
    for aula in sortedList_aulas:
        exam_date = (datetime.date(examen.fecha.year, examen.fecha.month, examen.fecha.day))
        if not examen.esta_asignado() and examen.lh() and ( aula.capacidad / examen.inscriptos >= 0.85):
            aula.registrar_examen(examen)

print("ASIGNADOS")

for aula in sortedList_aulas:
    aula.imprimir_info()

print("NO ASIGNADOS")



count_asignados = 0
count_no_asignados = 0
for examen in sortedList:
    if examen.esta_asignado():
        count_asignados += 1
    else:
        examen.imprimir_info()
        count_no_asignados += 1


print("ASIGNADOS:")
print(count_asignados)
print("NO ASIGNADOS:")
print(count_no_asignados)

