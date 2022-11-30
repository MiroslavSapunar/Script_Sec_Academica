import datetime

class _Aula:
    def __init__(self, piso, numero, capacidad):
        self.piso = piso
        self.numero = numero
        self.capacidad = int(capacidad)
        self.asignaciones = []

    def imprimir_info(self):
        print(f'Aula numero: {self.numero}, capacidad: {self.capacidad}')
        for asignacion in self.asignaciones:
            asignacion.imprimir_info()

class _Examen:
    def __init__(self, codigo = 'XXXX', materia = 'NULA', mesa = "NULA",fecha = '01/01/2000', hora = '00:00:01 AM', inscriptos = 0):
        fecha_completa = datetime.datetime.strptime(fecha+hora, "%m/%d/%y%I:%M:%S %p")
        self.materia = materia
        self.codigo = codigo
        self.mesa = mesa
        self.fecha = datetime.datetime.date(fecha_completa)
        self.hora = datetime.datetime.time(fecha_completa)
        self.inscriptos = inscriptos
        self.correctamente_asignado = False

    def asignar(self):
        self.correctamente_asignado = True

    def imprimir_info(self):
        print(f'codigo: {self.codigo}, materia: {self.materia}, mesa: {self.mesa}, fecha: {self.fecha}, hora: {self.hora}, incriptos: {self.inscriptos}')
