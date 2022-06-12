# Programa que pergunta a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o acarro custa R$ 60 por dia e R$0,15 por km rodado.

dist_percorrida = float(input('Digite a distância percorrida: '))
dias_alugado = int(input('Digite o número de dias de alugue: '))
valor_pagar = (dias_alugado * 60) + (0.15 * dist_percorrida)

print('O preço a pagar será {}'.format(valor_pagar))
