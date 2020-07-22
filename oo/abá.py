class Pessoa:
    def __init__(self, nome = None, idade = 13):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Nde .ara t.i porang'

if __name__ == '__main__':
    p = Pessoa('Guilherme,')
    print(Pessoa.cumprimentar(p))
    print(p.nome)
    p.nome = 'Gabriely e'
    print(p.nome)
    p.nome = 'Gustavo!'
    print(p.nome)
    print(p.idade)