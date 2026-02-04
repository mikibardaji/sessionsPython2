# llibreria per pintar per consola
# instalar a powershell pip install colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)

print(Fore.GREEN + "Text verd")
# print(Back.YELLOW + "Fons groc")
# print(Style.BRIGHT + "Brillante")
print(Style.RESET_ALL + "normal")
cierto = True
if (cierto==True):
    print("era cierto")
print (cierto)