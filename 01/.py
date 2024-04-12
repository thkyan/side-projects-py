import random

opcoes = ('pedra', 'papel', 'tesoura')
jogador = None
computador = random.choice(opcoes)
while jogador not in opcoes:
    jogador = input('escolha uma opção: (pedra, papel ou tesoura):')

print(f'jogador escolheu: {jogador}')
print(f'computador escolheu: {computador}')

if jogador == computador:
    print('deu empate!')
elif jogador == 'pedra'and computador == 'tesoura':
    print('você ganhouuu')
elif jogador == 'papel' and computador == 'pedra':
    print('você ganhouuu')
elif jogador == 'tesoura' and computador == 'papel':
    print('você ganhouuu')
else:
    print('você perdeuuu')