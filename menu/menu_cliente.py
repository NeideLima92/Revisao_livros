from cliente.buscar_cliente import *
from cliente.cliente_repositorio import *
from cliente.deletar_cliente import *
from cliente.editar_cliente import *
from cliente.listar_clientes import *
from cliente.registrar_cliente import *

def menuCliente():
    print("--------- Menu Cliente -------------")
    print("Escolha uma da opções abaixo")
    print("1 - Cadastrar cliente")
    print("2 - Editar cliente")
    print("3 - Remover cliente")
    print("4 - Buscar cliente")
    print("5 - Listar cliente")
    print("6 - Mostrar Menu")
    print("7 - Sair")

    while True:
        opcao = int(input("O que você deseja fazer?"))
        if opcao == 1:
            nome = input("Informe o nome do cliente:")
            registrarCliente(nome)
        elif opcao == 2:
            id = int(input("Informe o Id do cliente: "))
            nome = input("Informe o novo nome do cliente:")
            editarCliente(id,nome)
        elif opcao == 3:
            id = int(input("Informe o Id do cliente: "))
            deletarCliente(id)
        elif opcao == 4:
            id = int(input("Informe o Id do cliente: "))
            print(buscarCliente(id))
        elif opcao == 5:
            listarClientes()
        elif opcao == 6:
            print("1 - Cadastrar cliente")
            print("2 - Editar cliente")
            print("3 - Remover cliente")
            print("4 - Buscar cliente")
            print("5 - Listar cliente")
            print("6 - Mostrar Menu")
            print("7 - Sair")
        elif opcao == 7:
            print("Volte sempre!")
            break
        else:
            print("Opção não encontrada")


menuCliente()