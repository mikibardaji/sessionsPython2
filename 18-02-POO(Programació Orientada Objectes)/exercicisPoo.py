class Rectangle:
    def __init__(self, base, alçada):
        self.base = base
        self.alçada = alçada

    def calcular_area(self):
        return self.base * self.alçada


class Llum:
    def __init__(self, ubicacio):
        self.ubicacio = ubicacio
        self.estat = False

    def encendre(self):
        self.estat = True

    def apagar(self):
        self.estat = False

    def siEstaEncesa(self):
        if self.estat:
            print(f"La llum de {self.ubicacio} està encesa.")
        else:
            print(f"La llum de {self.ubicacio} està apagada.")


if __name__ == "__main__":
    llum1 = Llum("cuina")
    llum2 = Llum("menjador")
    
    llum1.encendre()
    llum1.apagar()  # Ja està apagada, però per seguir les instruccions
    llum2.encendre()
    
    llum1.siEstaEncesa()
    llum2.siEstaEncesa()
