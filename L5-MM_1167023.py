#"Pensamiento computacional seccion 17 laboratorio"
#12 de septiembre 2023
#Autor: mariano Manzo
#Objetivos: Aprender a utilizar operadores de comparacion y practicar el uso de las estructuras selectivas IF, IF-ElSE, IF-ELIF
#Entrada: Numero 
#proceso
#Salida: Resultado
#Ejercicio 1
#leer los datos de entrada
num1=input("Numero Entero: ")

#Convertir la entrada a tipo entero
num1=int(num1)

#Comparar los nuemros
if num1 > 0:
    print(num1, "es positivo")
if num1 < 0:
    print(num1, "es negativo")
if num1 == 0:
    print(num1, "es igual que")