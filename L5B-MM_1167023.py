#"Pensamiento computacional seccion 17 laboratorio"
#12 de septiembre 2023
#Autor: Mariano Manzo
#Objetivos: Aprender a utilizar operadores de comparacion y practicar el uso de las estructuras selectivas IF, IF-ElSE, IF-ELIF
#Entrada: Dia
#proceso
#Salida: Muestra e dia de la semana
#Ejercicio 2
#leer los datos de entrada
numdia=input("Numero de dia: ")

#Convertir la entrada a tipo entero
numdia=int(numdia)

#Comparar los nuemros
if numdia < 0 or numdia > 7:
    print(numdia, "Error, el numero a ingresar debe estar contenido entre 1 y 7")
if numdia == 1:
    print("Dia es lunes")
elif numdia == 2:
    print("Dia es martes")
elif numdia == 3:
    print("Dia es miercoles")
elif numdia == 4:
    print("Dia es Jueves")
elif numdia == 5:
    print("Dia es Viernes")
elif numdia == 6:
    print("Dia es Sabado")
elif numdia == 7:
    print("Dia es Domingo")
else:
    print("No es un dia de la semana")