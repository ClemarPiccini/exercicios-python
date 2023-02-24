#Crie um programa que peça um ano ao usuario e responda se o mesmo é ou não bissexto.
from datetime import date #pegar a data da maquina
ano = int(input('Que ano quer analisar? Se 0 for digitado, sera mostrado o ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}, É BISSEXTO'.format(ano))
else:
    print('O ano {}, NÃO É BISSEXTO'.format(ano))
