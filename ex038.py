#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
num = int(input('Insira o primeiro número:'))
num2 = int(input('Insira o segundo número:'))
if num > num2:
    print('O numero {}, que foi digitado primeiro, é maior que o {} que foi digitado por segundo.'.format(num, num2))
elif num < num2:
    print('O numero {}, que foi digitado por segundo, é maior que o {}, que foi digitado primeiro.'.format(num2, num))
elif num == num2:
    print('Os números {} e {} são iguais.'.format(num, num2))
