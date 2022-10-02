# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros
valor = float(input('Qual o valor da compra? R$:'))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro ou cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção: '))
if opção == 1:
    total = valor - (valor * 10 / 100)
    print('O valor da compra fica {:.2f}.'.format(total))
elif opção == 2:
    total = valor - (valor * 5 / 100)
    print('O valor da compra fica {:.2f}.'.format(total))    
elif opção == 3:
    print('O valor da compra fica {:.2f}.',format(valor))
elif opção == 4:
    total = valor + (valor * 20 / 100)
    print('O valor da compra vai ficar {:.2f}.'.format(total))
else:
    print('OPÇÃO INVALIDA. TENTE NOVAMENTE.')
