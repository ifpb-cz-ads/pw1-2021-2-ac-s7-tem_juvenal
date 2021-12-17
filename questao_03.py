#3) Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
L1 = []
L2 = []

while True:
    v = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if v == 0:
        break
    L1.append(v)

while True:
        v = int(input("Digite um valor para a segunda lista (0 para terminar):"))
        if v == 0:
            break
        L2.append(v)

L3 = []
dual_list = L1[:]
dual_list.extend(L2)
x=0
while x< len(dual_list):
    y = 0
    while y < len(L3):
        if dual_list[x] == L3[y]:
            break
        y = y+1
    if y == len(L3):
       L3.append(dual_list[x])
    x = x+1
x=0
while x<len(L3):
    print(f"{x}: {L3[x]}")
    x = x+1

