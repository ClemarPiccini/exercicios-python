#Crie um programa que pergunte quanto dinheiro a pessoa tem na carteira e converta para dolar.
r = float(input('Quanto dinheiro você tem na carteira: R$'))
dolar = r / 5.16
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(r, dolar))
