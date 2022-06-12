# Simular o uso de um dado, gerando um valor de 1 até 6

import random as rd


class SimuladorDeDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'


def Iniciar(self):
    resposta = input(self.mensagem)
    if resposta == 'sim':
        self.GerarValorDoDado()


def GerarValorDoDado():
    print(rd.randint(self.valor_minimo, self.valor_maximo)

simulador=SimuladorDeDados()
simulador.Iniciar()
