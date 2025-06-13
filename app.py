from fastapi import FastAPI, HTTPException
from services import livros_Services, cliente_Services
from models.Livro import Livro
from models.Cliente import Cliente



app = FastAPI()



@app.get('/')
def home():
    return {'Mensagem':'Api funcionando corretamente!'}




'''
    ->  INICIO rotas livro
'''

@app.post('/adicionar_livro')
def adicionar_livro(livro:Livro):
    return livros_Services.adicionar_livro(livro)




@app.get('/localizar')
def localizar():
    return livros_Services.mostrar_Livros()





@app.get('/localizar_livro/{isbn}')
def localizar_livro(isbn: int):
    livro = livros_Services.buscar_Livro_Por_Isbn(isbn)
    if livro is None:
        raise HTTPException(status_code=404, detail=f"Livro com ISBN {isbn} não encontrado.")
    return livro




@app.put('/editar_livro/{isbn}')
def editar_livro(isbn: int, novos_dados: Livro):
    return livros_Services.editar(isbn, novos_dados)




@app.delete('/deletar_livro/{isbn}')
def excluir_livro(isbn:int):
    return livros_Services.remover_por_isbn(isbn)


'''
    ->   FIM rotas livros
'''


'''
    ->    INICIO Rotas Clientes
'''

#remover cliente por matricula
@app.delete('/user/delete_client')
def delete_client(matricula):
    return cliente_Services.delete_user(matricula)

# adiciona um cliente a lista
@app.post('/add_user/')
def adicionar_usuario(cliente:Cliente):
    return cliente_Services.adicionar_usuario(cliente)


#edita cadastro do cliente
@app.put('/editar_user/{matricula}')
def altera_cadastro(matricula, dados:Cliente):
    return cliente_Services.alterar_cadastro_cli(matricula, dados)


#lista de usuarios
@app.get('/mostar_usuarios/')
def user_views():
    return cliente_Services.exibir_lista_cli()


@app.get('/loc_matricula/{matricula}')
def user_info(matricula):
    return cliente_Services.localiza_Cliente_Por_Matricula(matricula)