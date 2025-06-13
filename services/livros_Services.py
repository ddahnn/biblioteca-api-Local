from models.Livro import Livro

livros = []
livros = [
    {"ISBN": 1, "titulo": "Dom Casmurro", "ano_publicacao": 1899, "editora": "Garnier", "autor": "Machado de Assis"},
    {"ISBN": 2, "titulo": "O Alquimista", "ano_publicacao": 1988, "editora": "Rocco", "autor": "Paulo Coelho"},
    {"ISBN": 3, "titulo": "Capitães da Areia", "ano_publicacao": 1937, "editora": "José Olympio", "autor": "Jorge Amado"},
    {"ISBN": 4, "titulo": "Grande Sertão: Veredas", "ano_publicacao": 1956, "editora": "José Olympio", "autor": "João Guimarães Rosa"},
    {"ISBN": 5, "titulo": "A Hora da Estrela", "ano_publicacao": 1977, "editora": "José Olympio", "autor": "Clarice Lispector"},
    {"ISBN": 6, "titulo": "Memórias Póstumas de Brás Cubas", "ano_publicacao": 1881, "editora": "Garnier", "autor": "Machado de Assis"}
]
'''
    -- CRUD  Livros
'''

#adiconar
def adicionar_livro(livro:Livro):
    if not all ([livro.isbn, livro.ano_publi, livro.autor, livro.titulo]):
        return {"Mensagem":"Necessario todos os dados para cadastro"}
    
    for livro_loc in livros:
        if livro_loc["ISBN"] == livro.isbn:
            if "quantidade" in livro_loc:
                livro_loc["quantidade"] += 1
            else:
                livro_loc["quantidade"] = 2  
            return {"Mensagem": f"Livro já cadastrado. Quantidade aumentada para {livro_loc['quantidade']}"}
        
        livro_dic = {
            'ISBN': livro.isbn,
            'titulo': livro.titulo,
            'autor': livro.autor,
            'editora': livro.editora,
            'ano_publicacao': livro.ano_publi,
            'disponivel': livro.disponivel,
            'quantidade': livro.quantidade if livro.quantidade > 0 else 1
        }
        livros.append(livro_dic)
        return {"Mensagem": "Livro adicionado com sucesso!", "Livro": livro_dic}
        


#Editar localiza livro por ISBN e altera os dados do mesmo
def editar(isbn, novos_dados: Livro):
    for livro in livros:
        if livro['ISBN'] == isbn:
            livro['titulo'] = novos_dados.titulo
            livro['autor'] = novos_dados.autor
            livro['editora'] = novos_dados.editora
            livro['ano_publicacao'] = novos_dados.ano_publi
            return {"Mensagem": "Livro atualizado com sucesso!", "Livro": livro}
    return {"Erro": f"Nenhum livro com o ISBN {isbn} foi encontrado."}



#remover (atravez do ISBN )
def remover_por_isbn(isbn:int):
    livro = buscar_Livro_Por_Isbn(isbn)
    if livro is not None:
        livros.remove(livro)
        return {"Aviso":"Livro removido com sucesso."}
    else:
        return{"Erro":"livro não localizado"}



#buscar por ISBN 
def buscar_Livro_Por_Isbn(isbn:int):
    for livro in livros:
        if livro['ISBN'] == isbn:
            return livro 
    return None



#Listar todos os livros da lista
def mostrar_Livros():
    return livros