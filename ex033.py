 #Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Insira o primeiro numero: '))
b = int(input('Insira o segundo numero: '))
c = int(input('Insira o terceiro numero: ')) 
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {} e o menor número é {}'.format(maior, menor))
