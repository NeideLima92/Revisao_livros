from cliente.cliente_repositorio import *
from cliente.registrar_cliente import *
from cliente.buscar_cliente import *
from cliente.listar_clientes import *

def deletarCliente (id:int):
    pessoa = buscarCliente(id)
    if pessoa:
        clientes.remove(pessoa)
        print("Cliente removido com sucesso!")
    else:
        print("Cliente não encontrado!")

if __name__ == "__main__":
    print(buscarCliente(1))
    registrarCliente("Neide")
    listarClientes()
    deletarCliente (1)
    listarClientes()

