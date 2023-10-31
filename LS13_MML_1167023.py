#"Pensamiento computacional seccion 17 laboratorio"
#31 de octubre 2023
#Autor: Mariano Manzo
#Objetivos: Desarrollar una clase que gestiones la información ingresada por el usuario
#Entrada: 
#proceso:
#Salida: 
#Ejercicio: "Datos Persona"

from datetime import datetime

class Persona:
    def __init__(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellido_casada = ""
        self.fecha_nacimiento = None

    def insertar_nombres(self, nombres):
        self.nombres = nombres

    def insertar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def insertar_apellido_casada(self, apellido_casada):
        self.apellido_casada = apellido_casada

    def insertar_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        if self.apellido_casada:
            return f"{self.apellidos} de casada {self.apellido_casada}"
        else:
            return self.apellidos

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def obtener_nombre_completo(self):
        return f"{self.nombres} {self.obtener_apellidos()}"

    def obtener_edad(self):
        if self.fecha_nacimiento:
            today = datetime.today()
            age = today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
            return age
        else:
            return None

# Solicitar datos al usuario
nombre = input("Ingrese nombres: ")
apellido = input("Ingrese apellidos: ")
apellido_casada = input("Ingrese apellido de casada (deje en blanco si no tiene): ")
fecha_nacimiento_str = input("Ingrese fecha de nacimiento (formato: YYYY-MM-DD): ")

# Convertir la fecha de nacimiento a un objeto datetime
if fecha_nacimiento_str:
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d')
else:
    fecha_nacimiento = None

# Crear una instancia de la clase Persona
persona = Persona()

# Insertar los datos ingresados
persona.insertar_nombres(nombre)
persona.insertar_apellidos(apellido)
if apellido_casada:
    persona.insertar_apellido_casada(apellido_casada)
persona.insertar_fecha_nacimiento(fecha_nacimiento)

# Mostrar la información de la persona
print("\nInformación de la persona:")
print("Nombre completo:", persona.obtener_nombre_completo())
print("Edad:", persona.obtener_edad())



