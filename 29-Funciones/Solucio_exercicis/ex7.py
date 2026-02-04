def mesGranLlista(numeros):
    maxim = numeros[0]
    for n in numeros:
        if n > maxim:
            maxim = n
    return maxim

# Exemples d'ús
llista = [12, 45, 3, 89, 27]
print("El nombre més gran de la llista és:", llista)
print(mesGranLlista(llista))