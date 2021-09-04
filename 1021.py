valor = float(input(''))
notas = [100, 50, 20, 10, 5, 2,]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for notas in notas:
    qtd_notas = int(valor / notas)
    print(f'{qtd_notas} nota(s) de R$ {notas:.2f}')
    valor -= qtd_notas * notas

print('MOEDAS:')
for moedas in moedas:
    qtd_moedas = int(round( valor,2) / moedas)
    print(f'{qtd_moedas} moeda(s) de R$ {moedas:.2f}')
    valor -= qtd_moedas * moedas