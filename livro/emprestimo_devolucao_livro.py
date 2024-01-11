from livro.livro_repositorio import *
from livro.buscar_livro import *
from livro.registrar import *
from livro.listar_livros import *

def emprestarLivro (id: int):
    livro = buscarLivro(id)
    if not livro:
        print("Livro não encontrado!")
        return
    if not livro ['disponivel']:
        print("Livro indisponível!")
        return
    livro['disponivel']=False
    print("Emprestimo realizado com sucesso!")


def devolverLivro (id: int):
    livro = buscarLivro(id)
    if not livro:
        print("Livro não encontrado!")
        return
    if livro ['disponivel']:
        print("Livro já disponível!")
        return
    livro['disponivel']=True
    print("Devolução realizada com sucesso!")

if __name__ == "__main__":
    listarLivros()
    emprestarLivro(1)
    listarLivros()
    devolverLivro(1)
    listarLivros()
