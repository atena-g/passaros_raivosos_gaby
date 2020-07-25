class Pessoa:
    olhos=2
    nariz=1
    boca=1
    orelhas=2

    def __init__(self, *filhos, nome = None, idade = 32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Nde .ara t.i porang! Meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Mulher(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão.'

class Mutante(Pessoa):
    olhos=3
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. 3 Cabeçadas.'

if __name__ == '__main__':
    Gabriely = Mulher(nome = 'Gabriely')
    Gustavo = Mutante(nome='Gustavo')
    Guilherme = Pessoa(nome='Guilherme')
    Livio = Pessoa(Gabriely, Gustavo, Guilherme, nome = 'Livio')
    print(Pessoa.cumprimentar(Livio))
    print(id(Livio))
    print(Livio.cumprimentar())
    print(Livio.idade)
    print(Livio.nome)
    Livio.sobrenome = 'Rodrigues Rocha'
    print(Livio.sobrenome)
    for filho in Livio.filhos:
        print(filho.nome)
    del(Livio.filhos)
    print(Livio.__dict__)
    print(Gabriely.__dict__)
    print(Mutante.__dict__)
    print(Pessoa.metodo_estatico())
    print(Livio.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Mulher))
    print(Gustavo.cumprimentar())
    print(Gabriely.cumprimentar())