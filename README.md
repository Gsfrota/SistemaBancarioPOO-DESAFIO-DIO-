# Sistema Bancário Simples (Desafio da DIO)

Um projeto de sistema bancário simples, desenvolvido em Python utilizando programação orientada a objetos (POO).

## Descrição

Este é um sistema bancário simples implementado em Python como parte de um desafio proposto pela Digital Innovation One (DIO). O objetivo é demonstrar o uso de conceitos de programação orientada a objetos (POO) para modelar e implementar um sistema que permite realizar operações básicas em contas correntes.

## Funcionalidades

- Depositar: Permite ao usuário depositar um valor em uma conta corrente existente.
- Sacar: Permite ao usuário sacar um valor de uma conta corrente existente.
- Extrato: Permite ao usuário visualizar o extrato de uma conta corrente, mostrando todas as transações realizadas e o saldo atual.
- Sair: Encerra o programa.
- 
## Componentes Principais:

- Cliente: Representa um cliente do banco, com informações como nome, CPF, data de nascimento e endereço. Um cliente pode ter uma ou mais contas correntes.
- Conta: Representa uma conta corrente, com um número único, um saldo, um cliente associado e um histórico de transações.
- Transação: Classe abstrata que define o comportamento das transações, como depósitos e saques.
- Depósito e Saque: Implementações concretas de transações específicas.
- Histórico: Mantém o registro de todas as transações realizadas em uma conta corrente.
- Menu: Fornece um menu interativo para o usuário selecionar as operações desejadas

## Como Usar

1. Execute o arquivo `main.py`.
2. Siga as instruções apresentadas no terminal para interagir com o sistema.
3. Para depositar, sacar ou exibir o extrato, você precisará fornecer o CPF do cliente associado à conta corrente.




