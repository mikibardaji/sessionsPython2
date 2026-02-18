menu = """
1. Llistar alumne
2. Afegir alumne al final
3. Afegir alumne en una posició concreta 
4. Eliminar alumne (demanes el nom)
5. Modificar alumne per posició
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
            print("Opcio Llistar alumnes")
        case 2:
            print("Opcio Afegir alumne al final")            
        case 3:
            print("Opcio Afegir alumne en una posició concreta")
        case 4:
            print("Opcio Eliminar alumne (demanes el nom)")            
        case 5:
            print("Opcio Modificar alumne per posició")
        case 6:
            print("Opcio Ordenar Llista")            
        case 7:
            print("Final programa")
        case _:
            print("Opcion no correcta")