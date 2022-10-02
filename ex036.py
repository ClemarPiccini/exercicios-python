#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valorcasa = float(input('Qual o valor da casa que você quer comprar? R$'))
valorsalario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você quer pagar o imovel?'))
prestacao = valorcasa / (anos * 12)
minimo = valorsalario * 30 / 100
print ('Para pagar uma casa de R${} em {} anos, a prestação sera de R${}.'.format(valorcasa, anos, prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONSEDIDO!!!')
else:
    print('Emprestimo NEGADO.')
    