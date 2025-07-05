
def menu():
    print("""
    +--------------------------------------+
    |_________________MENU_________________|
    |[1] Depositar                         |
    |[2] Sacar                             |
    |[3] Extrato                           |
    |[4] Criar Usuário                     |
    |[5] Criar Conta Corrente              |
    |[6] Para listar os Usuários           |
    |[7] Para listar as Contas Correntes   |
    |[0] Sair                              |
    +--------------------------------------+
    =>""")

def imprimir_lista(lista, apresentacao):
    for i, usuario in enumerate(lista, start=1):
                    print(f"\n----------------------------------------\n{apresentacao}")
                    for chave, valor in usuario.items():
                        print(f"{chave}: {valor}")

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return(extrato, saldo)

def saque(*, saldo, valor, extrato, limite , numero_saques):
    LIMITE_SAQUES = 3
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

    else:
                print("Operação falhou! O valor informado é inválido.")
    return(saldo, extrato, numero_saques)

def consultar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF: ")
    filtro_usuario = filtrar_usuario(cpf, usuarios)
    
    if filtro_usuario:
        return print("Usuário já tem cadastro")
    
    nome = input("Digite seu nome: ")
    nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereço: ")
    usuarios.append({"CPF": cpf, "Nome": nome, "Data de Nascimento": nascimento, "Endereço": endereco })
    print("Usuário cadastrado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(numero_contas, contas, usuarios):
    cpf = input("Digite seu CPF: ")
    filtro_usuario = filtrar_usuario(cpf, usuarios)

    if filtro_usuario == None:
        return print("Você não possui o CPF cadastrado, crie um usuário para prosseguir.")
    
    agencia = str(numero_contas).zfill(4)
    numero_da_conta = 100000+numero_contas
    contas.append({"CPF do proprietário": cpf, "Numero da Conta": str(numero_da_conta).zfill(6), "agencia": agencia})
    print("Conta criada com sucesso!")
    return(numero_contas+1)

def main():

    usuarios = []
    numero_contas = 1
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:
        menu()
        opcao = input()

        if opcao == "1": #DEPOSITO
            valor = float(input("Informe o valor do depósito: "))
            extrato, saldo = deposito(saldo, valor, extrato)


        elif opcao == "2": #SAQUE
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques
                )


        elif opcao == "3": #CONSULTANDO EXTRATO
            consultar_extrato(saldo, extrato=extrato)


        elif opcao == "4": #CRIANDO USUÁRIOS
            criar_usuario(usuarios)
            print(usuarios)


        elif opcao == "5": #CRIANDO CONTAS
            numero_contas = criar_conta(numero_contas, contas, usuarios)
            print(contas)


        elif opcao == "6": #LISTANDO USUARIOS
            imprimir_lista(usuarios, "USUARIOS")


        elif opcao == "7": #LISTANDO CONTAS
            imprimir_lista(contas, "CONTA CORRENTE")


        elif opcao == "0": #SAÍDA DO PROGRAMA
            break


        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()