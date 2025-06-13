from pydantic import BaseModel
from typing import Optional

class  Cliente(BaseModel):
    matricula:Optional[str] = None
    nome:str
    telefone:str
    livros_alugados:list = []
    quantia_livros:int= 0
