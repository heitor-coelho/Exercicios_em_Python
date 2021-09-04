tem_total = int(input(''))

qt_s = [3600, 60, 1]
resultado = []

for alvo in qt_s:
    qtd = int(tem_total / alvo)
    resultado.append(str(qtd))
    tem_total -= qtd * alvo 
    
print(":".join(resultado))    