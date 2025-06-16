from pydantic import BaseModel

class Livro(BaseModel):
    isbn: str
    titulo: str
    autor: str
    editora: str
    ano_publi: int
    disponivel: bool = True
    quantidade: int = 1
