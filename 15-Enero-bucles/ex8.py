# Fes un programa que et demani 10 numer
#  i al finalitzar et digui la suma, pero si introdueixis el 666, s'acabi de demanar numeros (també ha de dir la suma de tots els numeros introduits).
num_introducidos = 0
acum_suma = 0
numero = 0
# salgo si llego a 10 numeros o introduzco el 666
while num_introducidos<10 and numero != 666:
    numero = int(input("pon un numero "))
    if (numero!=666):
        num_introducidos += 1
        acum_suma += numero
print(" has introducido ", num_introducidos, " numeros")
print(" la suma total es ", acum_suma)