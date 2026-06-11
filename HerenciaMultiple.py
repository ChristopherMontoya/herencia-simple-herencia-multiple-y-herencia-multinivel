class Camara:
    def tomar_foto(self):
        print("Foto tomada")


class Telefono:
    def hacer_llamada(self):
        print("Llamada realizada")


class Smartphone(Camara, Telefono):
    def abrir_aplicacion(self):
        print("Aplicación abierta")


celular = Smartphone()

celular.tomar_foto()
celular.hacer_llamada()
celular.abrir_aplicacion()