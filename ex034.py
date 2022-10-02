#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Insira seu salario: '))
aumento1 = salario + (salario * 10 / 100)
aumento2 = salario + (salario * 15 / 100)
if salario <= 1250:
    print('Seu novo salario com o aumento sera de {}'.format(aumento2))
else:
    print('Seu novo salario com o aumento sera de{}'.format(aumento1))
