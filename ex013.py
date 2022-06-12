# Algoritmo que lê o salário informado pelo usuário e mostra o novo salário com aumento de 15%.

salario = float(input('Informe o valor do salário: '))

salario_aumento = salario + salario * 0.15

print('O atual salário com aumento de 15% é R$ {:.2f}'.format(salario_aumento))