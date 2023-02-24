#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep # faz o computador esperar um tempo para continuar o codigo
computador = randint (0, 5) #faz o computador sortear.
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Qual número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS, você me ganhou!!!')
else:
    print('GANHEI, eu pensei no numero {} e não no {}!!!'.format(computador, jogador))
    