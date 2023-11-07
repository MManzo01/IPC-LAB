#"Pensamiento computacional seccion 17 laboratorio"
#7 de noviembre 2023
#Autor: Mariano Manzo
#Objetivos: Crear un programa que gestiones los atributos de la clase Automovil
#Entrada: Clase llamada automovil y sus atributos
#proceso:
#Salida: Resultados de los datos ingresados por el usuario según la información solicitada

class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = False
        self.tipoCambioDolar = 0.0
        self.descuentoAplicado = 0.0

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInformacion(self):
        precio_dolares = self.precio / self.tipoCambioDolar
        disponibilidad = self.MostrarDisponibilidad()
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares ${precio_dolares}. {disponibilidad}"

    def AplicarDescuento(self, porcentaje_descuento):
        if porcentaje_descuento >= 0 and porcentaje_descuento <= 100:
            self.descuentoAplicado = porcentaje_descuento
            descuento = (porcentaje_descuento / 100) * self.precio
            self.precio -= descuento


# Solicitar al usuario ingresar los datos
auto = Automovil()
auto.DefinirMarca(input("Ingrese la marca del automóvil: "))
auto.DefinirModelo(int(input("Ingrese el modelo del automóvil: ")))

auto.DefinirPrecio(float(input("Ingrese el precio del automóvil en quetzales: ")))
auto.DefinirTipoCambio(float(input("Ingrese el tipo de cambio en dólares: ")))

print("\nInformación del automóvil:")
print(auto.MostrarInformacion())

descuento = float(input("\nIngrese el descuento a aplicar en quetzales: "))
auto.AplicarDescuento(descuento)
print("\nInformación del automóvil con descuento aplicado:")
print(auto.MostrarInformacion())




