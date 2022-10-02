#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
nota1 = float(input('Insira a primeira nota:'))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua media foi {}.'.format(media))
if media < 5.0:
    print('Você foi REPROVADO.')
elif media > 7.0 or media == 7.0:
    print('Você foi APROVADO.')
elif media > 5.0 and media < 6.9:
    print('Você esta de RECUPERAÇÃO.')
