# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint (0, 10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'IP':
        tipo = str(input('Par ou impar? (P/I):')).strip().upper()[0]
    print('Você jogou {} e o computador jogou {}. Total de {}.'.format(jogador, computador, total))
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v =+ 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v =+ 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente!')
print('GAME OVER, você venceu {} vezes.'.format(v))

