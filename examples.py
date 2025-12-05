"""Pequeño módulo con demos de las principales mecánicas de Python.
Cada función imprime una demostración corta y autocontenida."""

import os
from contextlib import contextmanager


def variables_demo():
    x = 10
    y = 3.14
    s = "hola"
    b = True
    print("Variables:")
    print(f"  x (int) = {x}")
    print(f"  y (float) = {y}")
    print(f"  s (str) = {s}")
    print(f"  b (bool) = {b}")


def control_flow_demo():
    n = 5
    print("Control de flujo (for + if):")
    for i in range(n):
        if i % 2 == 0:
            print(f"  {i} es par")
        else:
            print(f"  {i} es impar")


def data_structures_demo():
    lista = [1, 2, 3]
    tupla = (4, 5)
    conjunto = {1, 2, 3}
    dic = {"a": 1, "b": 2}
    print("Estructuras de datos:")
    print(f"  lista: {lista}")
    print(f"  tupla: {tupla}")
    print(f"  conjunto: {conjunto}")
    print(f"  diccionario: {dic}")


def functions_demo():
    def suma(a, b=0):
        return a + b

    print("Funciones:")
    print(f"  suma(2,3) = {suma(2,3)}")
    print(f"  suma(5) = {suma(5)}")


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}"


class Empleado(Persona):
    def __init__(self, nombre, puesto):
        super().__init__(nombre)
        self.puesto = puesto

    def info(self):
        return f"{self.nombre} - {self.puesto}"


def classes_demo():
    print("Clases e herencia:")
    p = Persona("Ana")
    e = Empleado("Luis", "Dev")
    print(f"  Persona.saludar: {p.saludar()}")
    print(f"  Empleado.info: {e.info()}")


def exceptions_demo():
    print("Excepciones:")
    try:
        x = 1 / 0
    except ZeroDivisionError as ex:
        print(f"  Capturada: {ex}")


def file_io_demo():
    fname = "sample.txt"
    print("File I/O:")
    with open(fname, "w", encoding="utf-8") as f:
        f.write("Linea 1\nLinea 2\n")
    print(f"  Escribí {fname}")
    with open(fname, "r", encoding="utf-8") as f:
        contenido = f.read()
    print("  Contenido:")
    print(contenido)
    try:
        os.remove(fname)
        print(f"  Eliminé {fname}")
    except OSError:
        pass


def comprehension_generator_demo():
    print("Comprensión y generadores:")
    cuadrados = [x*x for x in range(6)]
    gen = (x*x for x in range(6))
    print(f"  lista comprensiva: {cuadrados}")
    print(f"  primer elemento generador: {next(gen)}")


def decorator_demo():
    def mi_decorador(func):
        def wrapper(*args, **kwargs):
            print("  -> Antes")
            res = func(*args, **kwargs)
            print("  -> Después")
            return res
        return wrapper

    @mi_decorador
    def decir(msg):
        print(f"    {msg}")

    print("Decorador:")
    decir("Hola desde decorador")


@contextmanager
def ejemplo_context_manager(name):
    print(f"Abrir {name}")
    try:
        yield name
    finally:
        print(f"Cerrar {name}")


def context_manager_demo():
    print("Context manager:")
    with ejemplo_context_manager("recurso") as r:
        print(f"  Usando {r}")


ALL_DEMOS = {
    "variables": variables_demo,
    "control_flow": control_flow_demo,
    "data_structures": data_structures_demo,
    "functions": functions_demo,
    "classes": classes_demo,
    "exceptions": exceptions_demo,
    "file_io": file_io_demo,
    "comprehension": comprehension_generator_demo,
    "decorator": decorator_demo,
    "context_manager": context_manager_demo,
}


def list_demos():
    return list(ALL_DEMOS.keys())


def run_demo(name):
    demo = ALL_DEMOS.get(name)
    if not demo:
        raise KeyError(f"Demo desconocida: {name}")
    demo()
