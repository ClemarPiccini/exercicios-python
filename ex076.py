# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('lápis', 1.75, 
'borracha', 3.50, 
'apontador', 4,
'caderno', 15.90)
print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end= ' ')
    else:
        print(f'R${listagem[pos]:.>7.2f}')
print('-' * 40)
