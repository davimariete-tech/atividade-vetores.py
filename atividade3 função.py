import os
os.system("cls")


def numero(n):
    if n>0:
        print("positivo")
    if n<0:
        print("negativo")


#chamando a função
n=int(input("digite um numero:"))
numero(n)