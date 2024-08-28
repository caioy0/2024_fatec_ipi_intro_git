#cria funcao de multiplicacao
class Multiplication:

    def multiplicar():
        a1 = float(input("Insira um numero: "))
        a2 = float(input("Insira um numero: "))
        print(f"answer: {a1*a2}")

#cria funcao de divisao
class Division: 

    def dividir():
        a1 = float(input("Insira um numero: "))
        a2 = float(input("Insira um numero: "))
        if a2 != 0:
            print(f"answer: {a1/a2}")
        else:
            print("hm")