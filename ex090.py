# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')
