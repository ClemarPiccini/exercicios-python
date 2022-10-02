# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
ano = date.today().year
nascimento = int(input('Insira o ano que você nasceu: '))
idade = ano - nascimento
if idade == 9 or idade < 9:
    print('Sua categoria é a MIRIM.')
elif idade >= 9 and idade < 14:
    print('Sua categoria é a INFANTIL.')
elif idade >= 14 and idade < 19:
    print('Sua categoria é a JUNIOR.')
elif idade >= 19 and idade < 25:
    print('Sua categoria é a SENIOR.')
elif idade >= 25:
    print('Sua categoria é a MASTER.')
