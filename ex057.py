#  Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('INSIRA SEU SEXO: (M/F) ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso.').format(sexo)


