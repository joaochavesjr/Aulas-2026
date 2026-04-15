valores = []

while 1:
    valor = input('Entre com o valor: ')

    if valor == 'fim':
        break

    try:
        valor = valor.replace(',', '.')
        valores.append(float(valor))
    except:
        print(f'\n*** Valor incorreto: {valor}\n')

total = sum(valores)
media = total / len(valores)

print('\nO total gasto no dia é: %0.2f' % total)
print('A média de gastos no dia é: %0.2f' % media)

