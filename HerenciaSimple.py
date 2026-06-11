class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindraje: {self.cilindraje} cc")


moto = Motocicleta("Yamaha", "MT-07", 689)
moto.mostrar_info()