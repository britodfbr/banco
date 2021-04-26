import datetime as dt
class Pessoa:
    def __init__(self, nome, cpf, email:str=None, data_nasc: dt.datetime=None):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.data_nasc = data_nasc


class Funcionario(Pessoa):
    domain = 'incolume.com.br'
    def __init__(self, matricula, login, cargo, nome, cpf, email):
        self.matricula = matricula
        self.login = login
        self.cargo = cargo
        super().__init__(nome, cpf, email)

    @property
    def emailfuncional(self):
        return f'{self.login}@{self.domain}'

class Cliente(Pessoa):
    def __init__(self, nome, cpf, email, renda, patrimonio):
        self.renda = renda
        self.patrimonio = patrimonio
        super().__init__(nome, cpf, email)