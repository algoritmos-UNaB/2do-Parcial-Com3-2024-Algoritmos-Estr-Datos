import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo
    
    def __iter__(self):
        return ListaDoblementeEnlazadaIterador(self.primero)

    def lista_random(self, cantidad):
        nombres = ["Andrea", "Micaela", "Nahuel", "Omar"]
        carreras = ["Medicina", "Arquitectura", "Abogacia", "Ingenieria"]
        
        for _ in range(cantidad):
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = datetime.date(random.randint(2000, 2024), random.randint(1, 12), random.randint(1, 28))
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            self.agregar(alumno)
        return self

class Iterador:
        def __init__(self, lista):
            self.lista = lista
            self.actual = lista.primero

        def __iter__(self):
            return self

        def __next__(self):
            if self.actual is None:
                raise StopIteration

            dato = self.actual.dato
            self.actual = self.actual.siguiente
            return dato 