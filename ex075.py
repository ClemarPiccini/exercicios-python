# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.
núm = (int(input('Digite um número: ')),
 int(input('Digite um número: ')), 
 int(input('Digite um número: ')),  
 int(input('Digite um número: ')))
print('Você digitou os valores: {}'.format(núm))
print('O valor 9 apareceu {} vezes.'.format(núm.count(9)))
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1} posição.') #o f no inicio do print é uma forma de usar o format.
else:
    print('O numero 3 não foi digitado em nenhuma posição.')
print('Os numeros pares digitados foram', end= ' ')
for n in núm:
    if n % 2 == 0:
        print(n, end= ' ')
