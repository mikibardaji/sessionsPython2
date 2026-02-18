class Point:
    x = 5 #Atributo de clase Coordenada x
    y = 7 #Atributo de clase Coordenada y

nom = "Hola" # Variable global tipo string
num = 10 # Variable global tipo entero

puntoCoordenada = Point() # Creación de un objeto de la clase Point
print("Coordenada x sin modificar " , puntoCoordenada.x) # Acceso al atributo x del objeto puntoCoordenada
print("Coordenada y sin modificar " , puntoCoordenada.y) # Acceso al atributo y del objeto puntoCoordenada
puntoCoordenada.x = 10 # Modificación del atributo x del objeto puntoCoordenada
puntoCoordenada.y = 15 # Modificación del atributo y del objeto puntoCoordenada
print("Coordenada x modificada" , puntoCoordenada.x) # Acceso al atributo x del objeto puntoCoordenada
puntoCoordenada2 = Point() # Creación de otro objeto de la clase Point
print("Coordenada x del segundo punto sin modificar " , puntoCoordenada2.x)

del puntoCoordenada # Eliminación del objeto puntoCoordenada
print("Coordenada x sin modificar " , puntoCoordenada.x) # Acceso al atributo x del objeto puntoCoordenada