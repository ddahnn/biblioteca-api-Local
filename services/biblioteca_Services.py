emprestimos = []
from . import livros_Services, cliente_Services
from models import Livro, Cliente
from datetime import date, timedelta, datetime



def alugar_livro(matricula, isbn):
    cliente = cliente_Services.localiza_Cliente_Por_Matricula(matricula)
    livro = livros_Services.buscar_Livro_Por_Isbn(isbn)
    if cliente is None:
        return {"Erro":f"Cliente com a matricula {matricula} não foi encontrado."}
    if livro is None:
        return {"Erro":f'o livro com o ISBN {isbn}, não foi encontrado. por favor verifique e tente novamente.'}
    if len(cliente['livros_alugados']) >= 3:
        return {"Erro":f"O cliente {cliente['nome']}, já possui 3 livros alugados."}
    if livro['disponivel'] == False:
        return {"Erro":f"O livro {livro['titulo']}, já esta alugado."}
    hoje = date.today()
    data_entrega = hoje + timedelta(days=7)
    aluguel = {
        'isbn': livro['ISBN'],
        'matricula': cliente['matricula'],
        'retirada': hoje.strftime('%d/%m/%Y'),
        'data_entrega': data_entrega.strftime('%d/%m/%Y')
    }
    livro['disponivel'] = False
    cliente['livros_alugados'].append(livro)
    emprestimos.append(aluguel)
    return {"Mensagem":"Livro alugado com sucesso!", "emprestimo":aluguel}



def devolver_livro(matricula, isbn):
    cliente = cliente_Services.localiza_Cliente_Por_Matricula(matricula)
    livro = livros_Services.buscar_Livro_Por_Isbn(isbn)
    if cliente is None:
        return {"Erro": f"Cliente com matrícula {matricula} não encontrado."}
    if livro is None:
        return {"Erro": f"Livro com ISBN {isbn} não encontrado."}
    emprestimo_encontrado = None
    for emprestimo in emprestimos:
        if emprestimo['matricula'] == matricula and emprestimo['isbn'] == isbn:
            emprestimo_encontrado = emprestimo
            break
    if emprestimo_encontrado is None:
        return {"Erro": "Empréstimo não encontrado para esse cliente e livro."}
    data_entrega = date.today()
    data_prevista = datetime.strptime(emprestimo_encontrado['data_entrega'], '%d/%m/%Y').date()
    dias_atraso = (data_entrega - data_prevista).days
    if dias_atraso > 0:
        mensagem_atraso = f"Devolvido com {dias_atraso} dias de atraso."
    else:
        mensagem_atraso = "Devolução no prazo."
    livro['disponivel'] = True
    if livro in cliente['livros_alugados']:
        cliente['livros_alugados'].remove(livro)
    emprestimos.remove(emprestimo_encontrado)
    return {
        "Mensagem": "Livro devolvido com sucesso!",
        "Detalhes": mensagem_atraso,
        "Livro": livro['titulo'],
        "Cliente": cliente['nome']
    }


def exibir_alugueis_ativos():
    if len(emprestimos) == 0:
        return {"Erro":"A lista está vazia. Nenhum emprestimo esta ativo atualmente."}
    else:
        return emprestimos
    

def exibir_livros_disponiveis():
    livros_disponiveis = []
    for livro in livros_Services.livros:
        if livro['disponivel'] == True:
            livros_disponiveis.append(livro)
    if len(livros_disponiveis) == 0:
        return {"Mensagem": "Nenhum livro disponível no momento."}
    else:
        return livros_disponiveis