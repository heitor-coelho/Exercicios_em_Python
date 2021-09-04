a, b, c = map(int,input().split())
x, y, z = map(int,input().split())

xa = x // a
yb = y // b
zc = z // c
t = xa * yb * zc
print(t)