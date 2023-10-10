#Pensamiento computacional
#Sección 17
#10 de octubre de 2023
#Mariano Manzo
#Objetivo: invocar al módulo para conversión de un moneda a otra
#Entrada: cantidad en una moneda
#Procesos principales:
#Salida: Cantidad en la moneda convertida 

import Conversiones 

while True:
    try:
        centimetros = float(input("Ingrese la cantidad en centímetros: "))
        unidad = input("Elija la unidad a la que desea convertir (metros, kilómetros, pulgadas, pies): ")

        if unidad == "metros":
            resultado = round(Conversiones.cm_a_metros(centimetros),2)
            print(f"{centimetros} centímetros son {resultado} metros.")
        elif unidad == "kilómetros":
            resultado = round(Conversiones.cm_a_kilometros(centimetros),2)
            print(f"{centimetros} centímetros son {resultado} kilómetros.")
        elif unidad == "pulgadas":
            resultado = round(Conversiones.cm_a_pulgadas(centimetros),2)
            print(f"{centimetros} centímetros son {resultado} pulgadas.")
        elif unidad == "pies":
            resultado = round(Conversiones.cm_a_pies(centimetros),2)
            print(f"{centimetros} centímetros son {resultado} pies.")
        else:
            print("Unidad no reconocida. Por favor, elija una de las opciones mencionadas.")

        continuar = input("¿Desea realizar otra conversión? (s/n): ")
        if continuar.lower() != "s":
            break

    except ValueError:
        print("Ingrese una cantidad válida en centímetros.")

        print("Programa terminado.")
