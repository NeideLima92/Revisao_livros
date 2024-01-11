from cliente.cliente_repositorio import *
from cliente.buscar_cliente import *
from cliente.listar_clientes import *


def editarCliente (id: int, nome: str):
    pessoa = buscarCliente(id)
    if pessoa:
        pessoa ['nome'] = nome
        print ("Dados alterados com sucesso!")
    else:
        print("Cleinte não encontrado!")



if __name__ == "__main__":
    listarClientes()
    editarCliente(1,"Bruno Alves")
    listarClientes()

