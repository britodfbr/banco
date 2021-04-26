from .pessoas import Cliente


class ContaBancaria:
    def __init__(self, num, cliente: Cliente):
        self.num = num
        self.cliente = cliente
        self.saldo = 0
        self.agencia = None
        self.limite = 0

    @property
    def registros(self):
        return self.__registros


class ContaCorrente(ContaBancaria):
    def __init__(self, agencia, num, cliente):
        super().__init__(num, cliente)
        self.agencia = agencia
        self.agencia.add_conta(self)

    def __repr__(self):
        return f"{self.agencia.num}/{self.num}"

class Cartao(ContaBancaria):
    pass