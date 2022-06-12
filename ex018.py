# Programa que recebe um ângulo qualquer e exibeo valor do seno, cosseno e tangente do ângulo.

import math 

angulo = float(input('Insira o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno do angulo é: {}, o cosseno é: {} e a tangente é: {}'.format(seno, cosseno, tangente))