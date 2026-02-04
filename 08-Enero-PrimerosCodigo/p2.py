
# Fes un programa que demana una frase llarga 
# qualsevol i després demana 2 valors enters. 
# El programa ha de retornar la frase 
# comprensa entre la primera posició del vaor 
# enter que has demanat i la segona posicio, o 
# sigui la frase retallada , mira't aquest link 
# https://www.w3schools.com/python/python_strings_slicing.asp
frase = input("Pon una frase larga ")
pos1 = int(input("Introduce posicion inicial: "))
pos2 = int(input("Introduce posicion final: "))
# frase2 = frase[pos1:pos2]
print(frase[pos1:pos2])