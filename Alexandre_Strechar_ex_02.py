class Aluno:
    def __init__(self, matricula, nome, prova1, prova2, trabalho1):
        self.matricula = matricula
        self.nome = nome
        self.prova1 = prova1
        self.prova2 = prova2
        self.trabalho1 = trabalho1
        self.media = self.media()

    def media(self):
        return (2.5*self.prova1+2.5*self.prova2+2.0*self.trabalho1)/(7)

    def final(self):
        if self.media >= 4 and self.media < 7:
            return True
        else:
            return False

alexandre = Aluno("3IA", "Alexandre", 7, 7, 7)
print(alexandre.final()) 
