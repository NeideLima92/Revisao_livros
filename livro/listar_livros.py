from livro.livro_repositorio import *
from livro.registrar import *

def listarLivros ():
    print("----- LISTA DE LIVROS -----")
    for livro in livros:
        print(f"Id: {livro['id']}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Editora: {livro['editora']}")
        print(f"Disponível: {livro['disponivel']}")
        print("*"*50)


if __name__ == "__main__":
    registrarLivro('teste', 'teste02')
    listarLivros()