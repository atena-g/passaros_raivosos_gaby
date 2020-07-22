class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Nde .ara t.i porang {id(self)}'


if __name__ == '__main__':
    Gabriely = Pessoa(nome = 'Gabriely')
    Gustavo = Pessoa(nome='Gustavo')
    Guilherme = Pessoa(nome='Guilherme')
    Livio = Pessoa(Gabriely, Gustavo, Guilherme, nome = 'Livio')
    print(Pessoa.cumprimentar(Livio))
    print(id(Livio))
    print(Livio.cumprimentar())
    print(Livio.nome)
    print(Livio.idade)
    for filho in Livio.filhos:
        print(filho.nome)