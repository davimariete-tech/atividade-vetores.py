import os
os.system("cls")

#função com passagem de parametros

def sadudação(nome,idade):
    print(F"ola, {nome}! bem vindo(a)!")
    print(f"sua idade é: {idade}")

def alt(altura, peso):
    print(F"altura:{altura}")
    print(F"peso:{peso}")
    
# chamamndo a função
nome=input("digite seu nome: ")
idade=int(input("digite sua idade:"))
sadudação(nome, idade)

altura=float(input("informe a altura:"))
peso=float(input("informe o peso:"))