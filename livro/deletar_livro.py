from livro.livro_repositorio import *
from livro.buscar_livro import *
from livro.registrar import *
from livro.listar_livros import *

def deletarLivro (id:int):
    livro = buscarLivro(id)
    if livro:
        livros.remove(livro)
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado!")

if __name__ == "__main__":
    registrarLivro('2', '4', )
    listarLivros()
    deletarLivro(1)
    listarLivros()