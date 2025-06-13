from pydantic import BaseModel

class Livro(BaseModel):
    isbn: int
    titulo: str
    autor: str
    editora: str
    ano_publi: int
    disponivel: bool = True
    quantidade: int = 1
