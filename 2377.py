L, D = map(int,input().split())
k, P = map(int,input().split())
custo_total = (k * L) + (L // D * P)
print(custo_total)