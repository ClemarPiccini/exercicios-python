#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes
from gc import is_finalized


r1 = float(input('Insira o primeiro segmento: '))
r2 = float(input('Insira o segundo segmento: '))
r3 = float(input('Insira o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!!!')
    elif r1 != r2 !=r3 !=r1:
        print('ESCALENO!!!')
    else:
        print('ISÓCELES!!!')
else:
    print('Os segmentos acima não podem formar um triangulo.')
    