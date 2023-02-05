import csv
import datetime
import random
from lib import _Examen, _Day

february = datetime.date(2022,12,31)

examenes = []
with open('./Data/Evaluaciones_Integradoras_2023-02-03.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
            if datetime.datetime.date(datetime.datetime.strptime(row[4], "%m/%d/%Y")) >= february:
                if (row[7] == "Las Heras"):
                    examenes.append(
                        _Examen(row[1], row[2], row[3], row[4], row[5], random.randrange(15, 110), True)
                    )

sortedList = sorted(examenes, key=lambda x: (x.fecha, x.hora))

previously_date = sortedList[0].fecha_hora()
print(f'{previously_date}')

count = 1
counts = []

print(f'cantidad examenes: {len(sortedList)}')


for examen in sortedList[1:]:
    if examen.fecha_hora() == previously_date:
        count+=1
    else:
        counts.append(_Day(previously_date, count))
        count = 1
        previously_date = examen.fecha_hora()

print(f'cantidad cuentas: {len(counts)}')
for day in counts:
    day.imprimir_info()

total = 0
for day in counts:
    total += day.cantidad()

print(total)
