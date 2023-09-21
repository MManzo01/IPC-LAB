#"Pensamiento computacional seccion 17 trabajo laboratorio"
#21 de septiembre 2023
#Autor: Mariano Manzo
#Objetivos: Practicar el uso de las instruciones para condicionales y ciclos, resolver problemas mediante el uso de variables y contadores
#Entrada: Numero ingresado de uno al diez
#proceso
#Salida: Mostrar la tabla de multiplicación del numero indicado por el usuario

print("Mariano Andres manzo Lopez")
while True:
    N=int(input("Ingrese un numero del uno al diez"))
    for i in range(1,11):
        result=N*i
        print(result)
    x = input("Desea ingresar mas datos?")
    if x =="no":
         break