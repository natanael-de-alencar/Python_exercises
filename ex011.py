#Programa que recebe a largura e altura de uma parede em metros e calcula a área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
tinta = area / 2

print('A área da parede é {} m² e será necessário {} L de tinta'.format(area, tinta))