from fastapi import FastAPI, HTTPException
from services import livros_Services, cliente_Services, biblioteca_Services
from models.Livro import Livro
from models.Cliente import Cliente



app = FastAPI()






@app.get('/')
def home():
    return {'Mensagem':'Api funcionando corretamente!'}




'''
    ->  INICIO rotas livro
'''

@app.post('/livro/adicionar_livro')
def adicionar_livro(livro:Livro):
    return livros_Services.adicionar_livro(livro)




@app.get('/livro/localizar')
def localizar():
    return livros_Services.mostrar_Livros()





@app.get('/livro/localizar_livro/{isbn}')
def localizar_livro(isbn: str):
    livro = livros_Services.buscar_Livro_Por_Isbn(isbn)
    if livro is None:
        raise HTTPException(status_code=404, detail=f"Livro com ISBN {isbn} não encontrado.")
    return livro




@app.put('/livro/editar_livro/{isbn}')
def editar_livro(isbn: int, novos_dados: Livro):
    return livros_Services.editar(isbn, novos_dados)




@app.delete('/livro/deletar_livro/{isbn}')
def excluir_livro(isbn:str):
    return livros_Services.remover_por_isbn(isbn)


'''
    ->   FIM rotas livros
'''


'''
    ->    INICIO Rotas Clientes
'''
@app.get('/client/')
def home_cli():
    return {"Mensagem":"Area cliente funcionando"}


#remover cliente por matricula
@app.delete('/client/delete_client/{matricula}')
@app.delete('/client/delete_client/{matricula}')
def delete_client(matricula):
    return cliente_Services.delete_user(matricula)

# adiciona um cliente a lista
@app.post('/client/add_user/')
def adicionar_usuario(cliente:Cliente):
    return cliente_Services.adicionar_usuario(cliente)


#edita cadastro do cliente
@app.put('/client/editar_user/{matricula}')
def altera_cadastro(matricula, dados:Cliente):
    return cliente_Services.alterar_cadastro_cli(matricula, dados)


#lista de usuarios
@app.get('/client/mostar_usuarios/')
def user_views():
    return cliente_Services.exibir_lista_cli()


@app.get('/client/loc_matricula/{matricula}')
def user_info(matricula):
    return cliente_Services.localiza_Cliente_Por_Matricula(matricula)

'''
    ->   FIM rotas livros
'''


'''
    ->    INICIO Rotas Bibliotecas
'''
# inicio bilbioteca
@app.get("/biblioteca")
def biblioteca():
    return {"Mensagem": "API BIBLIOTECA funcionando"}


#alugar livro
@app.post('/bilioteca/alugar/{matricula}/{isbn}')
def aluguel(matricula:str, isbn:int):
    return biblioteca_Services.alugar_livro(matricula, isbn)


#devolver livro
@app.delete('/bilioteca/devolver/{matricula}/{isbn}')
def devolver(matricula:str, isbn:int):
    return biblioteca_Services.devolver_livro(matricula, isbn)


#Exibir alugeis ativos
@app.get('/biblioteca/emprestimo')
def exibir_emprestimos_ativos():
    return biblioteca_Services.exibir_alugueis_ativos()


# Exibir livros disponiveis
@app.get('/biblioteca/livros_disponiveis')
def exibir_livros_disponiveis():
    return biblioteca_Services.exibir_livros_disponiveis()