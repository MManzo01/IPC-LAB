#Introducción a la Programación
#Sección: 17
#19/10/2023
#Mariano Manzo López
#Objetivo:Aplicar el uso de cadenas en python
#Entrada:Palabra ingresada por el usuario
#Procesos principales:
#Salida: mostrar el nuevo texto que se formó

# Solicitar una palabra al usuario
palabra = input("Ingresa una palabra: ")

# Mostrar las primeras tres letras de la palabra
primeras_tres_letras = palabra[:3]
print("Las primeras tres letras de la palabra son:", primeras_tres_letras)

# Almacenar las primeras tres letras en una nueva cadena
nueva_subcadena = primeras_tres_letras

# Solicitar un nuevo texto al usuario
nuevo_texto = input("Ingresa un nuevo texto: ")

# Recorrer el texto carácter a carácter y sustituir "O" por "x"
nuevo_texto_modificado = ""
for letra in nuevo_texto:
    if letra == "O" or letra == "o":
        nuevo_texto_modificado += "x"
    else:
        nuevo_texto_modificado += letra

# Mostrar el nuevo texto modificado
print("El nuevo texto modificado es:", nuevo_texto_modificado)
