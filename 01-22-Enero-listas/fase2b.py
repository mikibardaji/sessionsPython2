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


opcio = 0
while opcio!=7:
    print("")
    print("**** Fase1b****")
    print(menu)
    opcio = int(input("Pon una opcion: "))
    match(opcio):
        case 1:
            print("Lista de superheroe: ")
            for i  in range(len(listaPersonas)):
                    print((i+1), "-", listaPersonas[i])
            print("superheroes en clase: ", len(listaPersonas))
        case 2:
            nuevoSuperheroe = input("Pon el nuevo superheroe de la clase: ")
            listaPersonas.append(nuevoSuperheroe)
            print("Superheroe añadido...")
            print("Superheroes: " , len(listaPersonas))                        
        case 3:
            posicio = int(input("Pon en que posicion quieres poner al nuevo (numero): "))
            nom = input("Pon el nombre del nuevo superheroe: ")
            listaPersonas.insert(posicio,nom)
            print("Afegit" , nom , " a la posició ", posicio , "... ")
        case 4:
            nom = input("Pon el superheroe a eliminar: ")
            trobat = False
            for buscat in listaPersonas:
                if (buscat == nom):
                    listaPersonas.remove(nom)
                    print("Borrado ", nom) 
                    trobat = True
            if (trobat == False):
                print("No existe", nom)
        case 5:
            posicio = int(input("Pon que posicion quieres cambiar: "))
            nom = input("Pon el nuevo nombre: ")
            nom_antic = listaPersonas[posicio]
            listaPersonas[posicio] = nom
            print("Cambiado", nom_antic, " por ", nom)
        case 6:
            listaPersonas.sort()
            print("Lista Ordenada")            
        case 7:
            print("Final programa")
        case _:
            print("Opcion no correcta")