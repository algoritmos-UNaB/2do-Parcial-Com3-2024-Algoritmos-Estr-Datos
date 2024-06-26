
#EJERCICIO 1.
# Definir una clase Fecha. Formato: (dd, mm, aaaa).

# La clase debe contener métodos para facilitar:

# calcular_dif_fecha(): Calcular la distancia entre dos fechas.
# Sobrecarga de métodos:

# __str__
# __add__
# __eq__
# Importante:

# Cuando creamos (instanciamos) una Fecha, si es llamada sin parámetros, por defecto contendra la "fecha de hoy".

# Pueden agregar más atributos y métodos, si lo consideran necesario.
from datetime import datetime, deltatime

class Fecha:
    def __init__(self, dia= 0, mes= 0, año= 0)
        if dia == 0 or mes == 0 or año ==0:
            self.fecha = datetime.now()
        else: 
            self.fecha = datetime(dia,mes,año)

    def calcular_dif_fecha(self,otra_fecha):
        type(otra_fecha) != Fecha:.
            print("El argumento debe ser una instancia de la clase fecha.")
            return None
        if self.fecha > self.otra_fecha.fecha:
            diferencia_dias = self.fecha - otra_fecha.fecha
        else:
            diferencia_dias = otra_fecha.fecha - self.fecha
            return delta days 

    def __str__(self):
        return f"{self.fecha.day}/{self.fecha.month}/{self.fecha.year}"

    def __add__(self, dias):
        if type(dias) != int:
            print("el argumento debe ser un entero que representa el numero de dias.")
            return self
        nueva_fecha = self.fechas + timedelta(days=dias)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def __eq__(self, otra_fecha):
        if type(otra_fecha) != Fecha:
            return False
        return self.fecha == otra_fecha.fecha

    def main():
    
    fecha1 = Fecha(15, 6, 2024)
    fecha2 = Fecha(20, 6, 2024)
    fecha_hoy = Fecha()

    print("Fecha 1:", fecha1)
    print("Fecha 2:", fecha2)
    print("Fecha de hoy:", fecha_hoy)

    diferencia = fecha1.calcular_dif_fecha(fecha2)
    print("Diferencia en días:", diferencia)

    fecha_sumada = fecha1 + 10
    print("Fecha 1 + 10 días:", fecha_sumada)

    igualdad = fecha1 == fecha2
    print("¿Fecha 1 es igual a Fecha 2?:", igualdad)

if __name__ == "__main__":
    main()
#EJERCICIO 2. 

# Definir una clase Alumno como un diccionario, el cual contiene los datos:


# { "Nombre" : 'string',
#   "DNI" : 'integer' ,
#   "FechaIngreso" : 'Fecha',
#   "Carrera" : 'cualquier tipo' }
# La clase debe contener métodos para facilitar:

# Cambiar uno o varios datos del Alumno.
# antiguedad():Calcular la hace cuánto tiempo que el alumno esta inscripto en la carrera.
# Sobrecarga de métodos:

# __str__
# __eq__
# Importante:

# Un Alumno puede estar inscripto en sólo una carrera.
# Pueden agregar más atributos y métodos, si lo consideran necesario.


class Alumno:
    def __init__(self,nombre,dni,fecha_ingreso,carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrrera
    }

    def cambniar_datos(self, nombre=None, dni= None, fecha_ingreso=None, carrera=None):.

        if nombre:
            self.datos["Nombre"] = nombre
        if dni: 
            self.datos["DNI"] = dni
        if FechaIngreso:
            self.datos["fecha_ingreso"] = fecha_ingreso
        if carrera:
            self.datos["Carrera"] = carrera

    def antiguedad(self)
        fecha_ingreso = self.datos["FechaIngreso"]
        diferencia = datetime.now() - fecha_ingreso.fecha
        return diferencia.days // 365

    def __str__(self)
        return f"Nombre: {self.datos['Nombre']}, DNI: {self.datos['DNI']}, Fecha de Ingreso: {self.datos['FechaIngreso']}, Carrera: {self.datos['Carrera']}"

    def __eq__(self, otro_alumno):
        if not isinstance(otro_alumno, Alumno)
            return False
        return self.datos == otro_alumno.datos

    def main():
        fecha_ingreso_alumno = Fecha(1, 1, 2020)
        alumno1 = Alumno("Leonel Messi", 12345678, fecha_ingreso_alumno, "Futnolista")
        alumno2 = Alumno("Macarena Brizuela", 98765432, fecha_ingreso_alumno, "Enfermera")

        alumno1.cambiar_datos(carrera="Ciencias de la Computación")

        antiguedad_alumno1 = alumno1.antiguedad()
        print(f"Antigüedad de {alumno1.datos['Nombre']} en años: {antiguedad_alumno1}")

        print(alumno1)
        print(alumno2)

        print("los alumnos son iguales?", alumno1 == alumno2)

    if __name__ == "__main__":
        main()
        
# EJERCICIO 3.
# Crear una clase ListaDoblementeEnlazada cuyos nodos contengan como dato objetos del tipo Alumno. Implementar un Iterador para la lista enlazada (será útil en el siguiente ejercicio). La lista tendrá un método lista_ejemplo() el cual retorna un lista doblemente enlazada de alumnos cargada con datos aleatorios (random).

# Importante:

# Pueden agregar más atributos y métodos, si lo consideran necesario.


import random
from datetime import datetime, timedelta

#Clase Fecha, Alumno, Nodo

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.actual = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.ultimo is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo

    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is None:
            self.actual = self.primero
            return Noner
        else:
            dato = self.actual.dato
            self.actual = self.actual.siguiente
            return dato

    @staticmethod
    def lista_ejemplo(num_alumnos=4):
        alumno1 = Alumno("Leonel Messi", 12345678, fecha_ingreso_alumno, "Futnolista")
        alumno2 = Alumno("Macarena Brizuela", 98765432, fecha_ingreso_alumno, "Enfermera")
        lista = ListaDoblementeEnlazada()
        
        contador = 0
        while contador < num_alumnos:
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 99999999)
            dia = random.randint(1, 28)
            mes = random.randint(1, 12)
            año = random.randint(2015, 2021)
            fecha_ingreso = Fecha(dia, mes, año)
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            lista.agregar(alumno)
            contador += 1

        return lista

def main():
    lista_alumnos = ListaDoblementeEnlazada.lista_ejemplo(4)

    for alumno in lista_alumnos:
        if alumno is not None:
            print(alumno)

if __name__ == "__main__":
    main()

# EJERCICIO 4.
# Ejercicio 4:
# Implementar una función que permita ordenar la Lista Doblemente Enlazada "de Alumnos" (ejer. anterior). Pueden utilizar cualquier método de ordenación, pero deben implentarlo (no pueden usar el método sort de Python).

# El criterio de ordenación es: Fecha de Ingreso

# Importante:

# No usar el método sort de Python.
# Pueden agregar más atributos y funciones/métodos, si lo consideran necesario.

import random
from datetime import datetime, timedelta

#Clase Fecha, Alumno, Nodo y ListaDoblementeEnlazada

def ordenar_lista_por_fecha(lista):
    if lista.primero is None:
        return
    
    actual = lista.primero
    while actual.siguiente:
        siguiente = actual.siguiente
        while siguiente:
            if actual.dato.fecha_ingreso.fecha > siguiente.dato.fecha_ingreso.fecha:
                actual.dato, siguiente.dato = siguiente.dato, actual.dato
            siguiente = siguiente.siguiente
        actual = actual.siguiente

def main():
    lista_alumnos = ListaDoblementeEnlazada()
    lista_alumnos.lista_ejemplo(4)

    print("Lista original:")
    for alumno in lista_alumnos:
        print(alumno)

    ordenar_lista_por_fecha(lista_alumnos)

    print("\nLista ordenada por fecha de ingreso:")
    for alumno in lista_alumnos:
        print(alumno)

if __name__ == "__main__":
    main()

# # Se debe crear un directorio en el cual guardaremos en un archivo una "lista de alumnos". Luego, deberán mover el directorio a una nueva ruta (path). Finalmente deben borrar el nuevo archivo y el nuevo directorio. NO útilizar el módulo shutil (pueden usa el módulo os).

# # En resumen: crear directorio; guardar en un archivo una "lista de alumnos"; mover el directorio; borrar archivo y directorio.

# # Importante:

# # NO USAR shutil
# # Recodar el manejo de excepciones, si las hay.
# # Pueden agregar más atributos y funciones/métodos, si lo consideran necesario.

import os
import random
from datetime import datetime

#Clase Fecha, Alumno, Nodo y ListaDoblementeEnlazada 

def crear_directorio_guardar_datos_mover_y_borrar():
    
    directorio_origen = "./lista_alumnos"
    if not os.path.exists(directorio_origen):
        os.makedirs(directorio_origen)
    else:
        print(f"El directorio '{directorio_origen}' ya existe.")

    
    lista_alumnos = ListaDoblementeEnlazada.lista_ejemplo(4)
    archivo_alumnos = os.path.join(directorio_origen, "alumnos.txt")

    with open(archivo_alumnos, "w") as f:
        for alumno in lista_alumnos:
            f.write(str(alumno) + "\n")

    print(f"Archivo 'alumnos.txt' guardado en '{directorio_origen}'.")

    
    directorio_destino = "./nueva_ruta/lista_alumnos"
    try:
        os.rename(directorio_origen, directorio_destino)
        print(f"Directorio '{directorio_origen}' movido a '{directorio_destino}'.")
    except OSError as e:
        print(f"No se pudo mover el directorio: {e}")

    
    try:
        os.remove(os.path.join(directorio_destino, "alumnos.txt"))
        os.rmdir(directorio_destino)
        print(f"Archivo y directorio '{directorio_destino}' borrados correctamente.")
    except OSError as e:
        print(f"No se pudo borrar el archivo y directorio: {e}")

def main():
    crear_directorio_guardar_datos_mover_y_borrar()

if __name__ == "__main__":
    main()