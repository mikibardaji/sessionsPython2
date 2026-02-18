def sumaGrans40(numeros):
    suma = 0
    for numUnic in numeros:
        if numUnic > 40:
            suma += numUnic
    return suma

# Exemples d'ús
llista = [10, 45, 6, 130, 80, 25]
print("La suma dels nombres superiors a 40 és:", sumaGrans40(llista)) 