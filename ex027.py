#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Insira seu nome completo:')).strip()
nome = n.split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu ultimo nome é {}'.format(nome[len(nome)-1]))