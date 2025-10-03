import os 
os.system("cls")

print("===TABUADA===")
n = 0

def tabuada(numero):

    for i in range(1,11): 
        n = numero * i
        print(f"{numero} x {i} = {n}")
numero=int(input("digite o numero:"))

tabuada(numero)


