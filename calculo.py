#import the code from other files

from operation2 import *
from operation1 import *
import time
import os

#Class that call all the objects from other files hm... v2.1.0 calculator
class Calculatrice:

    def initmenu(self):
        while True: #loop
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
                    break #stop loop
                case _:
                    print("Invalid option")
                    time.sleep(1)
                    return calc.initmenu() #return to the selection numbers
            input("\nPress a key to continue... ")
#class all in one, this one does not call other objects from other classes v3.0.0 calculator
class NewCalculum:

    def menuinit(self):
        while True:
            os.system('clear') #clean the screen
            a1=float(input("Choose a number: "))
            symbol = str(input("Choose the symbol: "))
            if symbol not in {"+","-","*","/"}:
                print("Please select + or - or * or /")
                input("\nPress a key to continue... ")
                return calc2.menuinit()
            a2=float(input("Choose another number: "))
            if symbol == "+":
                print(f"answer: {a1+a2}")
            elif symbol == "-":
                print(f"answer: {a1-a2}")
            elif symbol == "*":
                print(f"answer: {a1*a2}")
            elif symbol == "/":
                if a2 == 0:
                    print("not here man")
                    input("\nPress a key to continue... ")
                    return calc2.menuinit()
                print(f"answer: {a1/a2}")
            choice = str(input("\nPress a key to continue... \nOr type exit to return to menu: "))
            if choice == "exit":
                break

#function to loop work
xc = 0
while True:
    os.system('clear')
    print("1- v2.1.0 \n2- v3.0.0 \n3- exit")
    xc = int(input("Select type of calculator: "))
    match xc:
        case 1:
            calc = Calculatrice()
            calc.initmenu()
        case 2:
            calc2 = NewCalculum()
            calc2.menuinit()
        case 3:
            break
        case _:
            print("hm")
            time.sleep(1.5)