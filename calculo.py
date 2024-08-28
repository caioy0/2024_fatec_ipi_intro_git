from op1 import *
from op2 import *
import time

#cria a calculadora
class Calculadora:

    def initmenu(self):
        while True:
            print("1 - soma \n 2- sub \n 3- mult \n 4- div")
            choose = int(input("Select an option: "))
            match choose:
                case 1:
                    Somme.somar()
                case 2:
                    Soustraire.subtrair()
                case 3:
                    Multiplication.multiplicar()
                case 4:
                    Division.dividir()
                case _:
                    print("Invalid option")
                    time.sleep(1)
                    return calc.initmenu()
            
calc = Calculadora()
calc.initmenu()