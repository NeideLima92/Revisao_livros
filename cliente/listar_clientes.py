from cliente.cliente_repositorio import *


def listarClientes ():
    print("----- CLIENTES CADASTRADOS -----")
    for pessoas in clientes:
        print(f"Id: {pessoas['id']}")
        print(f"Nome: {pessoas['nome']}")
        print("*"*50)


if __name__ == "__main__":
    listarClientes()