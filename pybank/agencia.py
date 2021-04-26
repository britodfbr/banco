from .banco import Banco
import datetime as dt
from inspect import stack
from .conta import ContaBancaria
from .pessoas import Funcionario


class Agencia:
    def __init__(self, banco: Banco, gerente: Funcionario, telefone):
        self.gerente = gerente
        self.num = Banco.gerador_numero_agencia()
        self.telefone = telefone
        self.__contas = []
        self.__registros = []
        banco.add_agencia(self)

    @property
    def registros(self):
        return self.__registros

    @property
    def contas(self):
        return self.__contas

    def _add_registro(self, *args, **kwargs):
        # reg = (dt.datetime.utcnow(), *args, **kwargs)
        reg = (dt.datetime.utcnow(), *args)
        self.__registros.append(reg)

    def add_conta(self, conta: ContaBancaria):
        self.__contas.append(conta)
        self._add_registro(stack()[0][3], conta, conta.cliente.cpf, conta.saldo)


class AgenciaVirtual(Agencia):
    def __init__(self, gerente, telefone):
        super().__init__(gerente, '001-1', telefone)


class AgenciaPrimium(Agencia):
    pass