#"Pensamiento computacional seccion 17 laboratorio"
#19 de septiembre 2023
#Autor: Mariano Manzo
#Objetivos: Determinar las variables ingresadas con operaciones aritmeticas
#Entrada: 
#proceso
#Salida: Resultados de las operaciones aritmeticas
#Ejercicio 1: "operaciones aritmeticas"

N1=int(input("Ingrese cualquier numero:"))
N2=int(input("Ingrese cualquier numero:"))

opcion=""
while opcion != "7":
    print("Menu de opciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Exponenciacion")
    print("6. Cociente")
    print("7. Modulo")
    opcion= input("seleccione un opcion")
    if opcion=="1":
        print("Selecciono la 1")
        print(N1, "+", N2, "=", N1+N2)
    elif opcion=="2":
        print("Selecciono la 2")
        print(N1, "-", N2, "=", N1-N2)
    elif opcion=="3":
        print("Selecciono la 3")
        print(N1, "*", N2, "=", N1*N2)
    elif opcion=="4":
        print("Selecciono la 4")
        print(N1, "/", N2, "=", N1/N2)
    elif opcion=="5":
        print("Selecciono la 5")
        print(N1, "**", N2, "=", N1**N2)
    elif opcion=="6":
        print("Selecciono la 6")
        print(N1, "//", N2, "=", N1//N2)
    elif opcion=="7":
        print("Selecciono la 7")
        print(N1, "%", N2, "=", N1%N2)
    else:
        print("Error... debe ingresar una opcion valida")



N1=int(input("Ingrese cualquier numero:"))
N2=int(input("Ingrese cualquier numero:"))

#Operaciones y resultados
Suma= N1+N2
Resta= N1-N2 
Multiplicacion= N1*N2 
Division= N1/N2
Exponenciacion= N1**N2
Cociente= N1//N2 
Modulo= N1%N2

#Mostrar resultados
print("la suma es:",N1, "+", N2, "=", N1+N2 ) 
print("La resta es:",N1, "-", N2, "=", N1-N2 )
print("La multiplicacion es:",N1, "*", N2, "=", N1*N2 )
print("La division es:",N1, "/", N2, "=", N1/N2 )
print("La exponenciacion es:",N1, "**", N2, "=", N1**N2 )
print("El cociente es:",N1, "//", N2, "=", N1//N2 )
print("El modulo es: ",N1, "%", N2, "=", N1%N2)
