#"Pensamiento computacional seccion 17 laboratorio"
#20 de septiembre 2023
#Autor: Mariano Manzo
#Objetivos: Determinar las variables ingresadas con operaciones aritmeticas
#Entrada: Los tres numeros ingresados
#proceso
#Salida: Resultados de las operaciones aritmeticas
#Ejercicio 3: "Jerarquía de operaciones"

a=int(input("Ingrese cualquier numero:"))
b=int(input("Ingrese cualquier numero:"))
c=int(input("Ingrese cualquier numero:"))

# Operaciones y resultados
op1= a*b+c
op2= a*(b+c)
op3= a/b*c
op4= 3*a+2*b/c^2

#Mostrar resultados
print("la op1 es:",op1 )
print("la op2 es:",op2 )
print("la op3 es:",op3 )
print("la op4 es:",op4 )
