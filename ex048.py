# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # conta o numero de algoritimos
        soma = soma + c # soma os numeos apresentados
print('A soma dos {} numeros solicitados é {}'.format(cont, soma))
