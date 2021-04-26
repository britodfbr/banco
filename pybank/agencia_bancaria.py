from banco import Banco
from agencia import Agencia
from inspect import stack


class AgenciaBancaria:
    def __init__(self, banco: Banco, agencia: Agencia):
        self.banco = banco
        self.agencia = agencia


    def add_agencia(self, agencia: Agencia):
        self.__agencias.append(agencia)
        self._add_registro(stack()[0][3], agencia.num)