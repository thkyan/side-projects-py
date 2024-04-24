comidas = []
precos = []
total = 0

while True:
    comida = input('qual comida deseja comprar? (s para sair)')
    if comida.lower() == 's':
        break
    else:
        preco = float(input(f'insira o valor da {comida}: R$'))
        comidas.append(comida)
        precos.append(preco)

print('---- seu carrinho ----')
for comida in comidas:
    print(comida, end='')

for preco in precos:
    total += preco

print(f'o valor total é de {total}')