# Programa que recebe os valores do cateto oposto e cateto adjacente de um triângulo retângulo
# retorna o comprimento da hipotenusa. OBS: h² = a² + b² - Eq. Pitágoras.

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2))**(1/2)

print('O valor da hipotenusa é: {}'.format(hipotenusa))
