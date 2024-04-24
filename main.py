from textwrap import dedent
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        else:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        return False

    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        if valor > self._limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif len(self.historico.transacoes) >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = self.efetuar_transacao(conta)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

    def efetuar_transacao(self, conta):
        raise NotImplementedError("Subclasses must implement efetuar_transacao method.")


class Saque(Transacao):
    def efetuar_transacao(self, conta):
        return conta.sacar(self.valor)


class Deposito(Transacao):
    def efetuar_transacao(self, conta):
        return conta.depositar(self.valor)


def menu():
    return input(dedent("""\

        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [q]\tSair
        => """))


def criar_cliente():
    cpf = input("Informe o CPF (somente números): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    return PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)


def criar_conta(cliente, numero_conta):
    return ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)

            if cliente is None:
                print("\n@@@ Cliente não encontrado! @@@")
                continue

            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            conta = cliente.contas[0]
            transacao.registrar(conta)

        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)

            if cliente is None:
                print("\n@@@ Cliente não encontrado! @@@")
                continue

            valor = float(input("Informe o valor do saque: "))
            transacao = Saque(valor)
            conta = cliente.contas[0]
            transacao.registrar(conta)

        elif opcao == "e":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)

            if cliente is None:
                print("\n@@@ Cliente não encontrado! @@@")
                continue

            conta = cliente.contas[0]
            print("\n================ EXTRATO ================")
            for transacao in conta.historico.transacoes:
                print(f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}")
            print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
            print("=========================================")

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

    print("\nSessão encerrada.")


if __name__ == "__main__":
    main()
