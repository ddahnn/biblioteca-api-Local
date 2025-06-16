from models.Cliente import Cliente

matricula = 000
clientes = [
    {
        "matricula": "001",
        "nome": "Ana Silva",
        "telefone": "11999990001",
        "livros_alugados": [],
        "quantia_livros": 0
    },
    {
        "matricula": "002",
        "nome": "Bruno Souza",
        "telefone": "11999990002",
        "livros_alugados": [],
        "quantia_livros": 0
    },
    {
        "matricula": "003",
        "nome": "Carla Pereira",
        "telefone": "11999990003",
        "livros_alugados": [],
        "quantia_livros": 0
    },
    {
        "matricula": "004",
        "nome": "Daniel Costa",
        "telefone": "11999990004",
        "livros_alugados": [],
        "quantia_livros": 0
    },
    {
        "matricula": "005",
        "nome": "Eduarda Lima",
        "telefone": "11999990005",
        "livros_alugados": [],
        "quantia_livros": 0
    },
    {
        "matricula": "006",
        "nome": "Felipe Alves",
        "telefone": "11999990006",
        "livros_alugados": [],
        "quantia_livros": 0
    },
    {
        "matricula": "007",
        "nome": "Gabriela Rocha",
        "telefone": "11999990007",
        "livros_alugados": [],
    }
]




#Remover usuario
def delete_user(matricula:str):
    cliente = localiza_Cliente_Por_Matricula(matricula)
    if cliente is not None:
        clientes.remove(cliente)
        return {"Mensagem":f"O cliente com a matricula {matricula} foi excluida com sucesso!"}
    else:
        return {"Erro":f"O usuário coma matricula {matricula}, nao foi econtrado, não existe, ou a lista está vazia."}
    




#alterar cadastro
def alterar_cadastro_cli(matr: str, dados: Cliente):
    for user in clientes:
        if user['matricula'] == matr:
            user['nome'] = dados.nome
            user['telefone'] = dados.telefone
            user['livros_alugados'] = dados.livros_alugados
            return {"Mensagem": "Cadastro atualizado com sucesso!", "Cliente": user}
    return {"Erro": f"Cliente com matrícula {matr} não encontrado."}




# Adicionar cliente
def adicionar_usuario(cliente: Cliente):
    if not all([cliente.nome, cliente.telefone]):
        return {"Erro": "Todos os campos (exceto matrícula) são necessários para o cadastro."}
    nova_matricula = gerar_matricula()
    cliente_dic = {
        "matricula": nova_matricula,
        "nome": cliente.nome,
        "telefone": cliente.telefone,
        "livros_alugados": []
    }
    clientes.append(cliente_dic)
    return {"Mensagem": "Cliente adicionado com sucesso!", "Cliente": cliente_dic}


#localizar por (Matricula)
def localiza_Cliente_Por_Matricula(matricula:str):
    for pessoa in clientes:
        if pessoa['matricula'] == matricula:
            return pessoa
    return None



#  Exibir lista completa
def exibir_lista_cli():
    if len(clientes) == 0:
        return {"Mensagem":"A lista esta vazia"}
    else:
        return clientes






def gerar_matricula():
    if not clientes:
        return "001"
    ultimas_matriculas = [int(cliente['matricula']) for cliente in clientes]
    nova = max(ultimas_matriculas) + 1
    return str(nova).zfill(3)