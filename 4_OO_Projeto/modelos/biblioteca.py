class Biblioteca:  # Classe
    bibliotecas = []  # Atributo

    def __init__(self, nome):  # metodo construtor
        self.nome = nome
        self._ativo = False  # atributo privado
        Biblioteca.bibliotecas.append(self)  # type: ignore

    def __str__(self):  # Metodo especial
        return self.nome

    @classmethod  # Decorador que
    def listar_bibliotecas(cls):
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome} - {biblioteca.ativo}")

    def alterna_estado(self):  # Metodo modificador de estado Metodo SET
        self._ativo = not self._ativo

    @property  # Decorador de propriedade, representa o metodo GET
    def ativo(self):
        return "atiavada" if self._ativo else "desativada"


biblioteca_cidade = Biblioteca("Biblioteca Cidade")  # Objeto
biblioteca_shopping = Biblioteca("Biblioteca Shopping")
biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()
print(biblioteca_cidade)
print(biblioteca_shopping)

Biblioteca.listar_bibliotecas()
