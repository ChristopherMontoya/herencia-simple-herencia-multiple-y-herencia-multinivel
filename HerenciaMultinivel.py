class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(f"Personaje: {self.nombre}")


class Guerrero(Personaje):
    def __init__(self, nombre, arma):
        super().__init__(nombre)
        self.arma = arma

    def atacar(self):
        print(f"{self.nombre} ataca con su {self.arma}.")


class Caballero(Guerrero):
    def __init__(self, nombre, arma, reino):
        super().__init__(nombre, arma)
        self.reino = reino

    def defender_reino(self):
        print(f"{self.nombre} defiende el reino de {self.reino}.")



caballero = Caballero("Arturo", "espada", "Camelot")

caballero.mostrar_nombre()
caballero.atacar()
caballero.defender_reino()