import matplotlib.pyplot as plt
import numpy as np


class Requisito:

    def __init__(self, nome):
        self.nome = nome
        self.ocorrencias = 0
        self.salarios = []

    def add(self, salario):
        self.ocorrencias += 1
        if salario > 0:
            self.salarios.append(salario)

    def salarioMedio(self):
        if len(self.salarios) > 0:
            return sum(self.salarios)/len(self.salarios)
        else:
            return 0


    def printEstat(self):
        print(self.nome)
        print("\tFrequência: %d" %(self.ocorrencias))
        print("\tVagas com salário: %d" %(len(self.salarios)))
        if len(self.salarios) > 0:
            print("\tMédia de salário: R$ %.2f" %( self.salarioMedio() ))

def converteSalario(salarioVetor):
    """
    Converte um parágrafo com a ocorrência de salário em
    um número decimal.
    Ex:
        paragrafo <= 'Salário: de R$ 1.800 - R$ 2.000'
        vetor <= ['Salário:', 'de', 'R$', '1.800', '-', 'R$', '2.000']
        retorno <= ( 1800.00 + 2000.00 ) / 2
    """
    # para cada palavra dentro do vetor:
    f = 0
    cont = 0
    for s in salarioVetor:
        # tenta fazer a conversao para float:
        try:
            f += 1000*float(s)
        # caso a palavra não seja uma representação válida de float:
        except ValueError:
            # passa para a próxima
            continue
        cont += 1
    if cont != 0:
        f = f/cont
    return f

def ScrapView(reqs):
    y1 = []
    y2 = []
    x = []
    for req in reqs:
        y1.append(reqs[req].salarioMedio())
        y2.append(reqs[req].ocorrencias)
        x.append(req)

    index = np.arange(len(reqs))
    width = 0.35

    fig, ax = plt.subplots()
    plt.xticks(rotation=70)
    rects1 = ax.bar(index, y1, width, color='r')
    ax.set_xticks(index)
    ax.set_xticklabels(x)
    ax.set_title('Salário Médio dos Requisitos de Emprego no Indeed')
    plt.xlabel('Requisito')
    plt.ylabel('Salário Médio (R$)')

    fig, ax = plt.subplots()
    plt.xticks(rotation=70)
    rects2 = ax.bar(index, y2, width, color='b')
    ax.set_xticks(index)
    ax.set_xticklabels(x)
    ax.set_title('Frequência dos Requisitos de Emprego no Indeed')
    plt.xlabel('Requisito')
    plt.ylabel('Frequência')


    plt.show()
