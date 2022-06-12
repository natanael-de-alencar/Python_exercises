#Programa que recebe um número e mostra o seu dobro, triplo e raiz quadrada

import math

numero = int(input("Digite um número: "))
print('O seu dobro é {}\n o seu triplo é {}\n e sua raiz quadrada é {}'.format((numero*2),(numero*3), math.sqrt(numero)))