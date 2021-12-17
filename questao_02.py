#2) Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

L1 = []
L2 = []
x = 0
while True:
    n = int(input("Digite um número (0 para sair):"))
    if n == 0:
       break
    L1.append(n)
    
while True:
     n = int(input("Digite um número (0 para sair):"))
     if n == 0:
       break
     L2.append(n)

L3 = L1+L2
print(L3)


