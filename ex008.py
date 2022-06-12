# Programa que recebe valor em metros e converte para centimetros e milimetros

distancia_km = float(input('Insira a distância em km: '))
distancia_cm = float(distancia_km * 10000)
distancia_mm = float(distancia_cm * 10)

print('A distância {}km, é {}cm e igual a {}mm'.format(
    distancia_km, distancia_cm, distancia_mm))
