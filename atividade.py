import os
os.system("cls")

#vetores
nulist=[]
quantidades_n=5
#variaveis
for i in range(5):
    n=int(input("informe o número:"))



#prova real 

if n<0:
    n=0
    nulist.append(n)

for n in nulist:
    print(f"numero: {n}")

    
print ("\nexibindo numeros")
for i, nu in enumerate(nulist):
    print(f"{i+1} numero:{nu}")
