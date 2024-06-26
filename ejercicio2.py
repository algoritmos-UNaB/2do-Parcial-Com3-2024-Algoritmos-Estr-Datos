import datetime

class Alumno:
    def __init__(self, nombre,dni,fecha_ingreso,carrera):
        self.nombre = nombre
        self.dni = dni
        self.fecha_ingreso = fecha_ingreso
        self.carrera = carrera 

def modificar_datos(self,diccionario):
    for clave, valor in diccionario.items():
        if clave == 'nombre':
            self.nombre = valor
        elif clave == 'dni':
            self.dni == valor
        elif clave == 'fecha_ingreso':
            self.fecha_ingreso == valor
        elif clave == 'carrera':
            self.carrera == valor

def antiguedad(self):
    hoy = datetime.date.today()
    return hoy - self.fecha_ingreso

def __eq__ (self, distinto_alumno):
    if isinstance(distinto_alumno,Alumno):
        return self.dni == distinto_alumno.dni
    else:
        return False 
def __str__(self):
        return f"Alumno(Nombre={self.datos['Nombre']}, DNI={self.datos['DNI']}, Fecha_ingreso={self.datos['Fecha_ingreso']}, Carrera={self.datos['Carrera']})"
