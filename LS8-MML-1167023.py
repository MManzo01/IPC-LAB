#"Pensamiento computacional seccion 17 laboratorio"
#26 de septiembre 2023
#Autor: Mariano Manzo López
#Objetivos: que el usuario eliga una opcion del menu y se muestre lo seleccionado
#Entrada: Ingresar el menu: factorial, Secuencia de Finobacci
#proceso
#Salida: mostrar en pantalla la secuencia del factorial según el numero ingresado y la secuencia de Fibonacci

X=int(input("Ingrese cualquier numero"))
Y=int(input("Ingrese un numero del menu de opciones"))

#Menu de opciones en ciclo
opcion=""
num=0
contador=1 
while opcion != "3":
    print("Menu de opciones")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir del programa")
    opcion = input("Ingrese la opcion elegida")
    if opcion =="1":
        print("Selecciono la FACTORIAL\n")
        num = int(input("Ingrese el numero: "))
        print("Vamos a MOSTRAR FACTORIAL de: ", num)
        while contador <= num:
            print(contador, "*")
            contador = contador + 1
    elif opcion == "2":
        print("Seleciono FIBONACCI\n")
        num = int(input("Ingrese el numero"))
        print("Vamos a MOSTRAR FIBONACCI de: ", num)
        contador=0 
        while contador <= num:
            print(contador, ",")
            contador = contador
    elif opcion == "3":
        print("Hasta pronto\n")
    else:
        print("Error... debe ingresar una opcion valida")


X=int(input("Ingrese cualquier numero"))
Y=int(input("Ingrese un numero del menu de opciones"))


