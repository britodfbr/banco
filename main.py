#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import datetime as dt
from pessoas import Funcionario, Cliente
from banco import Banco
from agencia import Agencia, AgenciaVirtual, AgenciaPrimium
from conta import ContaCorrente













def run():
    pass
    ger1 = Funcionario('0002', 'efsb', 'gerente', 'Eliana Ferreira dos Santos Brito', '123.456.789-00', 'eliana@incolume.com.br')
    banco = Banco(ger1, 'Incolume bank', 999, '3999-9999')
    print(banco)
    # Testes com Banco
    print(banco.novo_numero_agencia(), banco.novo_numero_conta())
    print(banco.novo_numero_agencia())
    print(banco.novo_numero_conta())
    print(banco.novo_numero_conta())
    print(banco._Banco__ultima_conta)

    # Testes com Agencia
    ger2 = Funcionario('1234', 'rbn', 'gerente', 'Ricardo Brito', '123.456.789-00', 'brito@incolume.com.br')
    ag1 = Agencia(banco, ger2, '2222-2222')
    print(ag1)


def run0():
    ger1 = Funcionario('1234', 'rbn', 'gerente', 'Ricardo Brito', '123.456.789-00', 'brito@incolume.com.br')
    cli1 = Cliente('Eliana Brito', '098.765.432-11', 'eliana@incolume.com.br', 8000, 100000)
    cli2 = Cliente("João Lira", "111.222.333-45", 'lira@hashtag.com.br', 5000, 50000)
    age1 = AgenciaVirtual(ger1, '5555-5555')
    conta01 = ContaCorrente(age1, '00001-1', cli1)
    conta02 = ContaCorrente(age1, '00002-4', cli2)
    print('-'*50)
    print(age1.num, age1.gerente.nome)
    print(conta01.cliente.nome, conta01.saldo, conta01.agencia.num, conta01.agencia.gerente.nome)
    print(conta02.cliente.nome, conta02.cliente.cpf, conta02.saldo, conta02.num, conta02.agencia.num)
    print(age1.contas)
    print(age1.registros)


if __name__ == '__main__':
    run()
