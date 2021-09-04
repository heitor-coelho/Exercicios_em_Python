produto1 = input().split()
c1 = int(produto1[0])
n1 = int(produto1[1])
v1 = float(produto1[2])
total1 = n1 * v1

produto2 = input().split()
c2 = int(produto2[0])
n2 = int(produto2[1])
v2 = float(produto2[2])
total2 = n2 * v2

total = total1 + total2
print(f'VALOR A PAGAR: R$ {total:.2f}')