from pydantic import BaseModel
from datetime import date

class TesteSistemaBase(BaseModel):
    id_implementacao: int
    resultado: str
    detalhes_teste: str
    data_teste: date
    responsavel_teste: str
    status: str

class TesteSistemaCreate(TesteSistemaBase):
    pass

class TesteSistemaOut(TesteSistemaBase):
    id_teste_sistema: int

    class Config:
        orm_mode = True
