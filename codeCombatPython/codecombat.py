
class heroi:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def dimeNombre(self):
        print("O nome do heroi é: " + self.nome)


#programa principal para ejercicio 0
heroi1 = heroi("Guerreiro", 100, 20)
heroi1.dimeNombre()

#programa principal para ejercicio 1
