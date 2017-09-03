class Requisito:

    def __init__(self, nome):
        self.nome = nome
        self.ocorrencias = 0
        self.salarios = []

    def add(self, salario):
        self.ocorrencias += 1
        if salario > 0:
            self.salarios.append(salario)

    def printEstat(self):
        print(self.nome)
        print("\tFrequência: %d" %(self.ocorrencias))
        print("\tVagas com salário: %d" %(len(self.salarios)))
        if len(self.salarios) > 0:
            print("\tMédia de salário: R$ %.2f" %(sum(self.salarios)/len(self.salarios)) )
