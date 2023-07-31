saldo = 0
saques = 0
depositos = 0


def sacar(valor):
    global saldo, saques
    if saldo >= valor:
        saldo -= valor
        saques += 1
    else:
        print("Saldo insuficiente.")


def depositar(valor):
    global saldo, depositos
    if valor > 0:
        saldo += valor
        depositos += 1
    else:
        print("Valor informado invalido.")


def extrato(saques, depositos, saldo):
    print(f"Saques:  {saques}")
    print(f"Depositos:  {depositos}")
    print(f"Saldo: R$ {saldo:.2f}")


while True:
    print("Menu\n1-Deposito\n2-Saques\n3-Extrato\n4-Sair")
    op = int(input("Digite um numero: "))

    if op == 1:
        valor = float(input("Digite o valor a ser depositado: "))
        depositar(valor)
        print("Valor depositado.")

    elif op == 2:
        if saques < 3:
            valor = float(input("Digite o valor a ser sacado: "))
            if 500>=  valor <= saldo:
                sacar(valor)
                print("Valor sacado.")
            else:
                print("Valor informado invalido.")
        else:
            print("Limite de saques alcançado.")

    elif op == 3:
        extrato(saques, depositos, saldo)

    elif op == 4:
        break
