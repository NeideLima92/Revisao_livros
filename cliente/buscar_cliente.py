from cliente.cliente_repositorio import *

def buscarCliente (id:int) -> dict or None:
    for pessoa in clientes:
        if id==pessoa['id']:
            return pessoa
    return None

if __name__ == "__main__":
    print(buscarCliente(1))
    print(buscarCliente(3))