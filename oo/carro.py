"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade:
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade.
2) Método acelerar, que deverá incrementar a velocidade de uma unidade.
3) Método frear, que deverá decrementar a velocidade de duas unidades.

A Direção terá a responsabilidade de controlar a direção. Oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método virar à direita.
3) Método virar à esquerda.

    Exemplo:
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor acelerar()
    >>> motor.velocidade
    2
    >>> motor acelerar()
    >>> motor.velocidade
    3
    >>> motor frear()
    >>> motor.velocidade
    1
    >>> motor frear()
    >>> motor.velocidade
    0
    >>> #testando direção
    >>> direção = Direção()
    >>> direção.valor
    'Norte'
    >>> direção.virar_a_direita()
    >>> direção.valor
    'Leste'
    >>> direção.virar_a_direita()
    >>> direção.valor
    'Sul'
    >>> direção.virar_a_direita()
    >>> direção.valor
    'Oeste'
    >>> direção.virar_a_direita()
    >>> direção.valor
    'Norte'
    >>> direção.virar_a_esquerda()
    >>> direção.valor
    'Oeste'
    >>> carro = Carro(direção, motor)
    >>> carro.calcular_velocidade
    0
    >>> carro.acelerar
    >>> carro.calcular_velocidade
    1
    >>> carro.frear
    >>> carro.calcular_velocidade
    0
    >>> carro.calcular_direção
    'Oeste'
"""

class Carro:
     def __init__(self, *motor, *direcao):
         self.motor = motor
         self.direcao = direcao

     NORTE = 'Norte'
     LESTE = 'Leste'
     SUL = 'Sul'
     OESTE = 'Oeste'

     class Direção(self):
         rotação_a_direita_dct={
             NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE
         }
         rotação_a_esquerda_dct={
             NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE
         }
         def __init__(self):
             self.valor = LESTE

         def girar_a_direita(self):
             self.valor = self.rotação_a_direita_dct[self.valor]
         def girar_a_esquerda(self):
             self.valor = self.rotação_a_esquerda_dct[self.valor]



     class Motor():
         def __init__(self):
             self.velocidade = 0
         def acelerar (self):
             self.acelerar += 1
         def frear (self):
             self.acelerar -= 2
             self.velocidade = max(0, self.velocidade)



