x = input()
x = x.split(' ')

a = float(x[0])
b = float(x[1])

c = ((b * 100) / a) - 100.00

print(f'{c:.2f}%')