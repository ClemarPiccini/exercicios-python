#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Insira um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O valor {} convertido para BINÁRIO, é igual a {}.'.format(num, bin(num)))
elif opção == 2:
    print('O valor {} convertido para OCTAL, é igual a {}.'.format(num, oct(num)))
elif opção == 3:
    print('O valor {} convertido para HEXADECIMAL, é igual a {}.'.format(num, hex(num)))
else:
    print('ESCOLHA INVALIDA.')
