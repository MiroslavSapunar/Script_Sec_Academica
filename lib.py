from datetime import datetime, timedelta

class _Day:
    def __init__(self, date = "NULL", count = 0):
        self.date = date
        self.count = count

    def imprimir_info(self):
        print(f'Fecha y hora: {self.date}, count: {self.count}')
    
    def cantidad(self):
        return self.count

class _Aula:
    def __init__(self, piso, numero, capacidad):
        self.piso = piso
        self.numero = numero
        self.capacidad = int(capacidad)
        self.asignaciones = []

    def registrar_examen(self, examen):
        if self.examen_se_puede_asignar(examen):
            self.asignaciones.append(examen)
            examen.asignar()

    def examen_se_puede_asignar(self, examen):
        if len(self.asignaciones) == 0:
            return True
        else:
            if any(
            (examen.fecha_hora() == asignacion.fecha_hora() or examen.fecha_hora() < asignacion.fecha_hora() + timedelta(hours=4))
            for asignacion in self.asignaciones ):
            # print(f'no cumple: {examen.fecha_hora()}')
                return False
            else:
                return True

    def imprimir_info(self):
        print(f'Aula numero: {self.numero}, capacidad: {self.capacidad}')
        for asignacion in self.asignaciones:
            asignacion.imprimir_info()

class _Examen:
    def __init__(self, codigo = 'XXXX', materia = 'NULA', mesa = "NULA",fecha = '01/01/2000', hora = '00:00:01 AM', inscriptos = 0, es_lh = False):
        # fecha_completa = datetime.strptime(fecha+hora, "%m/%d/%Y%I:%M:%S %p")
        fecha_completa = datetime.strptime(fecha + "-" + hora, "%m/%d/%Y-%H:%M")
        self.materia = materia
        self.codigo = codigo
        self.mesa = mesa
        self.fecha = datetime.date(fecha_completa)
        self.hora = datetime.time(fecha_completa)
        self.inscriptos = inscriptos
        self.asignado = False
        self.es_lh = es_lh

    def asignar(self):
        self.asignado = True

    def esta_asignado(self):
        return self.asignado

    def lh(self):
        return self.es_lh

    def fecha_hora(self):
        return datetime.combine(self.fecha, self.hora)

    def imprimir_info(self):
        print(f'codigo: {self.codigo}, materia: {self.materia}, mesa: {self.mesa}, fecha: {self.fecha}, hora: {self.hora}, incriptos: {self.inscriptos}, asignado: {self.asignado}, LH: {self.es_lh}')
