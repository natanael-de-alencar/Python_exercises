#Algoritmo que le o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Informe o valor do produto: '))
preco_desconto = preco_produto - 0.05 * preco_produto

print('O valor com desconto de 5% é: R$ {}'.format(preco_desconto))