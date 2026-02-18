listaAlumnos = ["Anderson","Brian","Alex","Izan"]
coeficientesIntelect = [100,200,50,10,45]
# print(coeficientesIntelect)
# cuantos items tiene una lista
print(len(coeficientesIntelect))
listaMezclada = ["Pepe", True, 23, "Juan", 4]
print("posicion 3", listaMezclada[3])# para acceder a una posición lista
listaMezclada[2] = 50 # cambio el valor en la posicion
print(listaMezclada)
# AÑADIR MAS VALORES DENTRO DE UNA LISTA
#Añadir al final de la lista --> append
listaMezclada.append("Cumpleaños")
print(listaMezclada)
#añadir en la posicion que quiero
listaMezclada.insert(2,"Orgiventura")
print(listaMezclada)
# Borrar por posicion , borrar por la ultima o borrar por valor
#borrar la ultima es pop(), posicion pop(3)
#borrar por posicion seria del listaMezclada[2]
#borrar por valor si existe listaMezclada.remove("Orgiventura")

for nombre in listaAlumnos:
    if (nombre!="Izan"):
        print(nombre)
    else:
        print("El innombrabler")

# averiguando el indice de la lista
for i in range(len(listaAlumnos)):
    if (listaAlumnos[i]=="Brian"):
        print("Brian esta en la posicion" , i) # La i va cambiando
        # es el indice y empieza por 0