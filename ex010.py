#Programa que recebe o valor em reais e converte em dolar para o usuário.
#cotação do dolar em junho de 2022. 1 dolar = 4,90 reais.

valor_real_BR = float(input('Digite o valor que possui em conta: '))
valor_dolar_US = valor_real_BR / 4.90

print('Seu saldo disponível em dolar é ${} '.format(valor_dolar_US))