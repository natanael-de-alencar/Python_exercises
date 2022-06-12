#Programa que cria a tabela periódica de um número de input

numero = int(input('Digite um número: '))
aux = 0
print('*' * 50)
print('Tabuada de {}'.format(numero))
print('*' * 50)

while(aux <= 10):
    print('{0} x {1} = {2}'.format(aux, numero, (aux*numero)))
    aux = aux + 1