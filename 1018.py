v = int(input(''))
print(v)
cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedulas in cedulas:
    qtd_cedulas = int(v / cedulas)
    print(f'{qtd_cedulas} nota(s) de R$ {cedulas},00')
    v -= qtd_cedulas * cedulas