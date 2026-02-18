pokemon1 = input("Pon el primer pokemon: ")
pokemon2 = input("Pon el segundo Pokemon: ")
pokemon1 = pokemon1.upper()
pokemon2 = pokemon2.upper()


if (pokemon1=="FUEGO" and (pokemon2=="AGUA"
                           or pokemon2 == "DRAGON"
                           or pokemon2 == "FUEGO"
                           or pokemon2 == "ROCA")):
    
    print(f"El tipo {pokemon1.capitalize()} pierde contra el tipo {pokemon2.capitalize()}")
elif(pokemon2=="FUEGO" and (pokemon1=="AGUA"
                           or pokemon1 == "DRAGON"
                           or pokemon1 == "FUEGO"
                           or pokemon1 == "ROCA")):
    print(f"El tipo {pokemon2.capitalize()} pierde contra el tipo {pokemon1.capitalize()}")

    if (num!=0)