import os
os.system("cls")

par=0
impar=0
#função
def par_impar(n):
    if n % 2==0:
        print("numero par")
        
    else:
        print("numero impar")


#chamando a função 
n=int(input("informe um numero:"))
par_impar(n)