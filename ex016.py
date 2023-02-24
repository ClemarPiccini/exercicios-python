#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('Insira um numero:'))
print('o numero interio de {} é {}'.format(num, trunc(num)))
