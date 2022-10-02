#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('Insira o primeiro segmento: '))
r2 = float(input('Insira o segundo segmento: '))
r3 = float(input('Insira o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo.')
else:
    print('Os segmentos acima não podem formar um triangulo.')
    