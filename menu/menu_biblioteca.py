from livro.buscar_livro import *
from livro.deletar_livro import *
from livro.editar_livro import *
from livro.listar_livros import *
from livro.livro_repositorio import *
from livro.registrar import *

def menuBiblioteca():
    print("--------- Menu Biblioteca -------------")
    print("Escolha uma da opções abaixo")
    print("1 - Cadastrar livro")
    print("2 - Editar livro")
    print("3 - Remover livro")
    print("4 - Buscar livro")
    print("5 - Listar livros")
    print("6 - Mostrar Menu")
    print("7 - Sair")

    while True:
        opcao = int(input("O que você deseja fazer?"))
        if opcao == 1:
            titulo = input("Informe o titulo do livro:")
            editora = input("Informe a editora do livro:")
            registrarLivro(titulo,editora)
        elif opcao == 2:
            id = int(input("Informe o Id do livro: "))
            titulo = input("Informe o novo titulo do livro:")
            editora = input("Informe a nova editora do lvro:")
            disponivel = True
            editarLivro(id,titulo, editora,True)
        elif opcao == 3:
            id = int(input("Informe o Id do livro: "))
            deletarLivro(id)
        elif opcao == 4:
            id = int(input("Informe o Id do livro: "))
            print(buscarLivro(id))
        elif opcao == 5:
            listarLivros()
        elif opcao == 6:
            print("1 - Cadastrar livro")
            print("2 - Editar livro")
            print("3 - Remover livro")
            print("4 - Buscar livro")
            print("5 - Listar livros")
            print("6 - Mostrar Menu")
            print("7 - Sair")
        elif opcao == 7:
            print("A curiosidade está para o conhecimento como o desinteresse está para a ignorância.")
            break
        else:
            print("Opção não encontrada")


menuBiblioteca()