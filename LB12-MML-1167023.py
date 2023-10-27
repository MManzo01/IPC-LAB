#"Pensamiento computacional seccion 17 laboratorio"
#24 de octubre 2023
#Autor: Mariano Manzo
#Objetivos: Realizar un código para administrar una lista de contactos
#Entrada: Declarar una variable tipo lista para los contactos
#proceso
#Salida: Mostrar la lista de contactos ordenada y la original
#Ejercicio: "Tarea LAB semana 12"

#Declarar una variable tipo lista.
contactos = []

#Solicitar la cantidad de contactos y agregarlos a la lista.
n = int(input("Ingrese la cantidad de contactos que va a ingresar: "))
for _ in range(n):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    contactos.append([nombre, telefono])

#Mostrar la lista de contactos completa.
print("Lista de contactos completa:")
for contacto in contactos:
    print(contacto)

#Eliminar un contacto por nombre.
nombre_eliminar = input("Ingrese el nombre del contacto que desea eliminar: ")
for contacto in contactos:
    if contacto[0] == nombre_eliminar:
        contactos.remove(contacto)

#Mostrar la lista de contactos actualizada.
print("Lista de contactos actualizada:")
for contacto in contactos:
    print(contacto)

#Ordenar la lista alfabéticamente por nombre.
contactos.sort(key=lambda x: x[0])

#Mostrar la lista ordenada.
print("Lista de contactos ordenada alfabéticamente:")
for contacto in contactos:
    print(contacto)

#Ingresar un nuevo contacto con el nombre en mayúsculas.
nombre_mayusculas = input("Ingrese el nombre del nuevo contacto en mayúsculas: ")
telefono_nuevo = input("Ingrese el número de teléfono del nuevo contacto: ")
contactos.append([nombre_mayusculas, telefono_nuevo])

#Ingresar un nuevo contacto en una posición específica.
posicion = int(input("Ingrese la posición donde debe guardar el nuevo contacto: "))
nombre_nuevo = input("Ingrese el nombre del nuevo contacto: ")
telefono_nuevo = input("Ingrese el número de teléfono del nuevo contacto: ")
contactos.insert(posicion, [nombre_nuevo, telefono_nuevo])

#Mostrar la lista de contactos completa.
print("Lista de contactos completa:")
for contacto in contactos:
    print(contacto)

#Crear una copia de la lista original y ordenarla alfabéticamente de forma descendente.
copia_contactos = contactos.copy()
copia_contactos.sort(key=lambda x: x[0], reverse=True)

#Mostrar la lista ordenada y la lista original.
print("Lista de contactos ordenada alfabéticamente de forma descendente:")
for contacto in copia_contactos:
    print(contacto)

print("Lista de contactos original (sin cambios):")
for contacto in contactos:
    print(contacto)
