# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nasc = int(input('Insira o ano que você nasceu: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar este ano.')
elif idade < 18:
    saldo1 = 18 - idade
    print('Você tera que se alistar daqui a {} anos.'.format(saldo1))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado a {} anos.'.format(saldo))
