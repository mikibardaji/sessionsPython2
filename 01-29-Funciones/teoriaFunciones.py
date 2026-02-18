def saludar(): #() no te arguments entrada
    num = 5
    print("Hola mundo ", num)

def adios():
    print("Adios")



print("Programa Teoria funciones")
saludar()
saludar()
for i in range(5):
    adios()

def farenheitCelsius(gradosFarenheit):
    celsius = (gradosFarenheit - 32) * 5 / 9
    return celsius

def saludoCompleto(nombre, edat):
    print(f" te llamas {nombre} y tienes {edat} años")

#segunda utilidad funciones para que haga el calculo
# pasar de farenheit a celsius
temp1 = 77
celsius1 = farenheitCelsius(temp1)
print(f" farenheit {temp1} celsius : {celsius1}")

temp2 = 95
celsius2 = farenheitCelsius(temp2)
print(" farenheit ", temp1, " celsius ", celsius2)

temp3 = 50
celsius3 = farenheitCelsius(temp3)
print(celsius3)

saludoCompleto("Hector",14)
saludoCompleto("Eva",12)
saludoCompleto("David",10)