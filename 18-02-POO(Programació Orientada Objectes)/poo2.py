import os
class Person:
    def __init__(self, name2, age,city): #Constructor, al momento de crear un objeto de la clase Person, se le deben pasar los parametros name2, age y city
        self.name = name2
        self.age = age
        self.city = city #self.city es diferente a city, el primero es el atribudo de clase y el segundo es un parametro de entrada
        self.alive = True #Atributo de clase alive, se inicializa en True
        self.km = 0 #Atributo de clase km, se inicializa en 0 

    def saludar(self): #Metodo de la clase Person, se le pasa el parametro self, que hace referencia al objeto que llama al metodo
        if self.alive: # Condicion para verificar si el objeto que llama al metodo esta vivo, si alive es True, se ejecuta el bloque de codigo dentro del if
            print("Hola, mi nombre es " , self.name) 
        else:
            print("BUUUUAFFFFFGFGFGGFGFG")

    def kill(self): 
        self.alive = False # Modificación del atributo alive del objeto que llama al metodo, se cambia a False

    def andar(self):
        if self.alive==True:
            self.km += 1 # Modificación del atributo km del objeto que llama al metodo, se incrementa en 1
        else:
            self.km +=5 
        for i in range(0, self.km): # Bucle for para imprimir el numero de kilometros que ha andado el objeto que llama al metodo, se ejecuta desde 1 hasta km+1, ya que el rango no incluye el ultimo numero
            print("=", end="") # Imprime un "=" sin salto de linea, el parametro end="" hace que no se imprima un salto de linea al final de la impresion

ciudadano1 = Person("Enric",20,"Barcelona") # Creación de un objeto de la clase Person, se le pasan los parametros name2, age y city
ciudadano2 = Person("Alex",18,"Hospitalet") # Creación de otro objeto de la clase Person, se le pasan los parametros name2, age y city
ciudadano3 = Person("Jefferson",19,"Cornella") # Creación de otro objeto de la clase Person, se le pasan los parametros name2, age y city

print("Nombre 1", ciudadano1.name) # Acceso al atributo name del objeto ciudadano1
print("Nombre 2", ciudadano2.name) # Acceso al atributo name del objeto ciudadano2
print("Nombre 3", ciudadano3.name) # Acceso al atributo name del objeto ciudadano
ciudadano2.age = 119
print("Edad 2", ciudadano2.age) # Acceso al atributo age del objeto ciudadano2
ciudadano2.saludar() # Llamada al metodo saludar del objeto ciudadano2
ciudadano2.kill() # Llamada al metodo kill del objeto ciudadano2
print("Ciudadano 2 esta vivo?", ciudadano2.alive) # Acceso al atributo alive del objeto ciudadano2
ciudadano2.saludar() # Llamada al metodo saludar del objeto ciudadano2, aunque el ciudadano2 esta muerto, el metodo saludar sigue funcionando, ya que no hay ninguna condicion que impida su ejecucion
os.system("cls")
ciudadano3.andar() # Llamada al metodo andar del objeto ciudadano3, el objeto ciudadano3 ha andado 1 km, por lo que se imprime un "="
print(ciudadano3.km) # Acceso al atributo km del objeto ciudadano3, se imprime 1, ya que el objeto ciudadano3 ha andado 1 km
ciudadano3.andar() # Llamada al metodo andar del objeto ciudadano3,
print()
ciudadano3.andar()
print("mato al ciudadano")
ciudadano3.kill()
ciudadano3.andar()
#Crea una classe Rectangle amb els atributs base i alçada. Afegeix un mètode per calcular l'àrea ($base \times alçada$).
