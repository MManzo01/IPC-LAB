# Declarar variables
LP1 = 1
LP2 = 2
PVMC1 = 0
PVMC2 = 0
CMCM1 = 0
CMCM2 = 0
E1 = 0
E2 = 0
CHE1 = 0
CHE2 = 0
#listas vacías
CHTE1 = [] 
CHTE2 = []
GTLP1 = 0
GTLP2 = 0
CTCHE1= 0
CTCHE2 = 0


# Menú para ingresar datos de la línea de producción 1
print("Datos para la Línea de Producción 1:")
PVMC1 = int(input("Precio de venta por metro cuadrado: "))
CMCM1 = int(input("Cantidad de metros cuadrados vendidos en línea 1: "))
E1 = int(input("Número de empleados en línea 1 (1-20): "))

# Validar el número de empleados
if E1 < 1 or E1 > 20:
    print("Número de empleados no válido. Debe ser entre 1 y 20.")
else:
    for i in range(E1):
        horasTrabajadas1 = int(input(f"Cantidad de horas trabajadas por empleado {i + 1} (2-20): "))
        costoPorHora1 = int(input(f"Costo por hora del empleado {i + 1} (25-100): "))
        if horasTrabajadas1 < 2 or horasTrabajadas1 > 20 or costoPorHora1 < 25 or costoPorHora1 > 100:
            print("Datos de empleado no válidos. Revise las restricciones.")
            break
        CHE1 += costoPorHora1
        CHTE1.append([horasTrabajadas1, costoPorHora1])

# Menú para ingresar datos de la línea de producción 2
print("\nDatos para la Línea de Producción 2:")
PVMC2 = int(input("Precio de venta por metro cuadrado: "))
CMCM2 = int(input("Cantidad de metros cuadrados vendidos en línea 2: "))
E2 = int(input("Número de empleados en línea 2 (1-20): "))

# Validar el número de empleados
if E2 < 1 or E2 > 20:
    print("Número de empleados no válido. Debe ser entre 1 y 20.")
else:
    for i in range(E2):
        horasTrabajadas2 = int(input(f"Cantidad de horas trabajadas por empleado {i + 1} (2-20): "))
        costoPorHora2 = int(input(f"Costo por hora del empleado {i + 1} (25-100): "))
        if horasTrabajadas2 < 2 or horasTrabajadas2 > 20 or costoPorHora2 < 25 or costoPorHora2 > 100:
            print("Datos de empleado no válidos. Revise las restricciones.")
            break
        CHE2 += costoPorHora2
        CHTE2.append([horasTrabajadas2, costoPorHora2])

# Calcular ganancia total, costo total y ganancia neta para ambas líneas de producción
GTLP1 = CMCM1 * PVMC1
for horas, costo in CHTE1:
    CTCHE1 += horas * costo
GN1 = GTLP1 - CTCHE1

GTLP2 = CMCM2 * PVMC2
for horas, costo in CHTE2:
    CTCHE2 += horas * costo
GN2 = GTLP2 - CTCHE2

# Calcular el índice de eficiencia para ambas líneas de producción
IE1 = round((GN1 / E1), 0)
IE2 = round((GN2 / E2), 0)

# Determinar la línea de producción con el mayor índice de eficiencia
if IE1 > IE2:
    LPME = LP1
else:
    LPME = LP2

# Mostrar resultados

print("\nResultados:")
print("Ganancia Neta Línea de Producción 1: ", GN1)
print("Costo Total Línea de Producción 1: ", CTCHE1)
print("Ganancia Total Línea de Producción 1: ", GTLP1)
print("Índice de eficiencia Línea de producción 1", IE1)
print("Ganancia Neta Línea de Producción 2: ", GN2)
print("Costo Total Línea de Producción 2: ", CTCHE2)
print("Ganancia Total Línea de Producción 2: ", GTLP2)
print("Índice de eficiencia Línea de producción 2", IE2)
print("Línea de Producción con Mayor Índice de Eficiencia: ", LPME)

