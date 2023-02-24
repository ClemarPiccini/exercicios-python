

#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Insira um numero inteiro:'))
divisão = numero % 2 
if divisão == 1:
    print("O seu numero é IMPAR!!!")
else:
    print('O seu numero é PAR!!!')
