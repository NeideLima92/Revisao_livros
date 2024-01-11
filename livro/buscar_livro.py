from livro.livro_repositorio import *

def buscarLivro (id:int) -> dict or None:
    for livro in livros:
        if id==livro['id']:
            return livro
    return None

if __name__ == "__main__":
    print(buscarLivro(1))
    print(buscarLivro(3))