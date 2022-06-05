"""
    Association -   Use
    Agregation  -   Has
    Composition -   is owner
    Inheritance -   is
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

    # Cliente tem seu metódo falar
    def falar(self):
        print('Estou em CLIENTE.')


# Member Overlap
# Class ClienteVIP inherit from Client from Pessoa
# Can replace any member of the class.
class ClienteVIP(Cliente):
    def falar(self):
        # executa metódo falar da super classe Pessoa
        super().falar()
        # executa metódo falar da super classe Pessoa
        Pessoa.falar(self)
        print('Any thing...')


class Aluno(Pessoa):
    def estudar(self):        
        print(f'{self.nomeclasse} estudando...')
