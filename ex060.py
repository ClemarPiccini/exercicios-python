# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
n = int(input('Insira um numero para calcular sua fatorial:'))
f = factorial(n)
print('A fatorial do numero {} é {}.'.format(n, f))
