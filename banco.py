from pessoas import Funcionario
from inspect import stack
from agencia import Agencia


class Banco:
    def __init__(self, gerente: Funcionario, nome:str, num: str, telefone: str):
        self.gerente = gerente
        self.nome = nome
        self.num = num
        self.telefone = telefone
        self.__agencias = []
        self.__registros = []
        self.__ultima_conta = "000000000-0"
        self.__num_agencias = []

    @property
    def registros(self):
        return self.__registros

    def add_agencia(self, agencia: Agencia):
        self.__agencias.append(agencia)
        self._add_registro(stack()[0][3], agencia.num)

    def gerador_numero_conta(self):
        n = int(self.__ultima_conta[: self.__ultima_conta.index('-')])
        while True:
            c = f"{n:09}-{n ** 7 //10 % 10}"
            if c > self.__ultima_conta:
                self.__ultima_conta = c
                yield self.__ultima_conta
            n += 1

    def gerador_numero_agencia(self):
        n = 1
        while True:
            c = f"{n:03}-{n ** 31 //1 % 10}"
            if c not in self.__num_agencias:
                self.__num_agencias.append(c)
                yield c
            n += 1

    def novo_numero_conta(self):
        gen_num = self.gerador_numero_conta()
        return next(gen_num)

    def novo_numero_agencia(self):
        gen_num = self.gerador_numero_agencia()
        return next(gen_num)

    def __str__(self):
        return f'<{self.nome}: {self.num}>'