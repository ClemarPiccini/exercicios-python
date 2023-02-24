#escreva um programa que leia uma medida em metros e converta para milimetros e centimetros:
medida = float(input('insira uma medida em metros:'))
cm = medida * 100
mm = medida * 1000
print('a medida {} metros é igual a {} cm e {} mm'.format(medida, cm, mm))
