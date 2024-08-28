#import the code from other files

from operationb import *
from operationa import *
import time
import os

#create the main brain yeaaah
class Calculatrice:

    def initmenu(self):
        while True:
            os.system('clear')
            print("1- Sum \n2- Soustraire \n3- Multiplication \n4- Division \n5- exit")
            choose = int(input("Select an option: "))
            match choose:
                case 1:
                    Somme.somar() #call sum
                case 2:
                    Soustraire.subtrair() #call sub
                case 3:
                    Multiplication.multiplicar() #call mult
                case 4:
                    Division.dividir() #call division
                case 5:
                    break
                case _:
                    print("Invalid option")
                    time.sleep(1)
                    return calc.initmenu()
            input("\nPress a key to continue... ")

#function to loop work
calc = Calculatrice()
calc.initmenu()