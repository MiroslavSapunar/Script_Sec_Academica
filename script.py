import csv


with open('./Data/RELEVAMIENTO DE AULAS - AULA.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Las columnas de archivo son: {" - ".join(row)}')
            line_count += 1
        else:
            print(f'Sede: {row[0]}, piso: {row[1]}, aula nº: {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
