#Um programa que recebe algo e mostra o tipo primito e todas as informações sobre ela

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumérico?', a.isalnum())