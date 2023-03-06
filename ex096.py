# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(larg, comp):
    a = larg * comp
    print(a)


l = float(input('LARGURA EM METROS: '))
c = float(input('COMPRIMENTO EM METROS: '))
area(l, c)
