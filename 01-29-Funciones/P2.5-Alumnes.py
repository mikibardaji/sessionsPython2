import os #Importo llibreria del sistema operatiu perque vull netejar la pantalla. No ho heu de saber
def limpiarPantalla():
    #Pone pausa y borra la pantalla  
    input("Aprieta Enter para volver menú...")
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrarSuperheroes(lista):
    print("Lista de superheroe: ")
    print("For con el range ")
    # Opcio 1 --> Contar amb la variable posic que em dona la posició
    # for posic  in range(len(lista)): # estas indicando que i empezando por 0 cambiara de 1 en 1 hasta llegar a el numero de ocurrencias que tenga la lista en ese momento
    #         print((posic+1), "-", lista[posic]) # (posici+1) es para que se vea BONITO, la posició 0 se imprimirà 1, la posición 1 se imprimira 2  
    #         # y luego lista[posic] pinta el contenido de esas listad

    #Opcion 2 foreach en cada vuelta el contenido de una de las posiciones se vuelca en la variable nombre
    print("For con el  in, for el each ")            
    ordenLista = 0
    for nombre in lista:
        ordenLista += 1; #aumenta el valor de la variable en 1
        print(ordenLista, "-", nombre) #esta opción me da el nombre, pero no se en que posición esta.... por eso invento la variable vueltas para que cuente
        #     print(f"{ordenLista} - {nombre}") #otra manera de visualizarlo

        print("superheroes en clase: ", len(lista))


menu = """
1. Llistar superheroe
2. Afegir superheroe al final
3. Afegir superheroe en una posició concreta 
4. Eliminar superheroe (demanes el nom)
5. Modificar superheroe per posició
6. Ordenar Llista 
7. Sortir
"""

listaPersonas = ["Ironman","Superman","Batman","Hulk"]


opcio = 0 #valor fake
while opcio!=7:
    print("")
    print("**** Fase1b****")
    print(menu)
    opcio = int(input("Pon una opcion: "))
    match(opcio):
        case 1:
            mostrarSuperheroes(listaPersonas)
            limpiarPantalla()
        case 2:
            nuevoSuperheroe = input("Pon el nuevo superheroe de la clase: ")
            listaPersonas.append(nuevoSuperheroe) # l'afegeix al final
            print("Superheroe añadido...\n")
            print("Superheroes: " , len(listaPersonas))  #El len em dona quants hi ha   
            limpiarPantalla()
        case 3:
            posicio = int(input("Pon en que posicion quieres poner al nuevo (numero): "))
            nom = input("Pon el nombre del nuevo superheroe: ")
            listaPersonas.insert(posicio,nom) # Inserta a la posició, si sol fiques listaPersonas.insert(nom) s'afegiria al final
            print("Afegit" , nom , " a la posició ", posicio , "... ")
            limpiarPantalla()
        case 4:
            nom = input("Pon el superheroe a eliminar: ")
            trobat = False
            for buscat in listaPersonas:
                if (buscat == nom): 
                    listaPersonas.remove(nom) # si no hagues comprovat que existia, al fer remove(nom) donaria un error QUANT NO EXISTIS
                    print("Borrado ", nom) 
                    trobat = True
            if (trobat == False): #es troba a l'alçada del for, per tant vol dir que s'executa al SORTIR del for.
                print("No existe", nom) # si esta a false es que no l'ha trobat

            #Opció 2: fa el mateix que l'altra
            for buscat in listaPersonas:
                if(buscat==nom):
                    listaPersonas.remove(nom) # si no hagues comprovat que existia, al fer remove(nom) donaria un error QUANT NO EXISTIS
                    print("Borrado ", nom) 
            else: #aquest else, NO ES DEL IF, sino que es quant ha acabat el for si MAI ha entrat al if, llavors fa else... si ha entrat un cop, ja no entra aquest if
                print("No existe", nom)

            limpiarPantalla()
        case 5:
            posicio = int(input("Pon que posicion quieres cambiar: "))
            nom = input("Pon el nuevo nombre: ")
            nom_antic = listaPersonas[posicio] #Guardo lo que contenia en una variable SOLA para no perder el contenido ANTIGUO
            listaPersonas[posicio] = nom #ya puedo machacar esa posición.
            print("Cambiado", nom_antic, " por ", nom)
            limpiarPantalla()
        case 6:
            listaPersonas.sort() #metodo de listas que ordena, no hay mas, es conocerlo
            print("Lista Ordenada")
            limpiarPantalla()            
        case 7:
            print("Final programa")
        case _:
            print("Opcion no correcta")
