#Introduccion aa la programacion trabajo supervisado
#28/09/23
#Mariano Manzo Lopez
#Objetivo: 
#Entrada: 
#Procesos principales: 
#Salida: Mostrar: 

for numero in range(1, 26):
    if numero < 25:
        print(numero, end=',')
    else:
        print(numero)

numero = 1
while numero <= 25:
    if numero < 25:
        print(numero, end=",")
    else:
        print(numero)
    numero+=1
print()
    
for numero in range(5, 51, 5):
    if numero < 50:
        print(numero, end=',')
    else:
        print(numero)

numero = 5
while numero <= 50:
    if numero < 50:
        print(numero, end=",")
    else:
        print(numero)
    numero+=5
print()  

for numero in range(20, -2, -2):
    if numero > 0:
        print(numero, end=', ')
    else:
        print(numero)

numero = 20
while numero >= 0:
    if numero>0:
       print(numero, end=",")
    else:
        print(numero)
    numero-=2