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
