#Introduccion aa la programacion trabajo supervisado
#6/09/23
#Mariano Manzo Lopez
#Objetivo: 
#Entrada: 
#Procesos principales: 
#Salida: Mostrar: 

def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def fibonacci(numero):
    if numero <= 0:
        return []
    elif numero == 1:
        return [0]
    elif numero == 2:
        return [0, 1]
    else:
        secuencia = [0, 1]
        while len(secuencia) < numero:
            siguiente_numero = secuencia[-1] + secuencia[-2]
            secuencia.append(siguiente_numero)
        return secuencia

while True:
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")

    opcion = input("Ingrese el número de opción que quiere ejecutar: ")

    if opcion == "1":
        numero = int(input("Ingrese un número: "))
        resultado = factorial(numero)
        print(f"{numero}! = {resultado}")
    elif opcion == "2":
        numero = int(input("Ingrese un número: "))
        secuencia = fibonacci(numero)
        print(f"Secuencia de Fibonacci({numero}): {', '.join(map(str, secuencia))}")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")