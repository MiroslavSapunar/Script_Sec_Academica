import csv

# materia = {
#     "codigo": "XXXX",
#     "nombre": "Nn",
#     "Fechas":[],
# }


def info_materia(materia):
    print(f'codigo: {materia["codigo"]}, nombre: {materia["nombre"]}')

def info_fechas_materia(materia):
    i = 1
    for date in materia["fechas"]:
        print(f'fecha nº{i} el {date}')
        i+=1


materias = []

with open('./Data/Dic 2022 - Feb-Mar 2023-Table 1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    header = next(csv_reader)
    print(header)
    # line_count = 0
    for row in csv_reader:
        if not any(materia['codigo'] == row[0] for materia in materias):
            materias.append(
                {
                    "codigo": row[0],
                    "nombre":row[1],
                    "fechas": [row[5]]
                }
            )
        else:
            materia = materias[-1]
            print('materia: ', str(materia))
            # (materias[index])["fechas"].append(row[6])
            # materias['fechas'] + row[6]


    print("cantidad de materias cargadas: ",len(materias))
    # for materia in materias:
    #     info_materia(materia)
    #     info_fechas_materia(materia)
    #     if line_count == 0:
    #         print(f'Las columnas de archivo son: {" - ".join(row)}')
    #         line_count += 1
    #     else:
    #         print(f'Sede: {row[0]}, piso: {row[1]}, aula nº: {row[2]}.')
    #         line_count += 1
    # print(f'Processed {line_count} lines.')


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
