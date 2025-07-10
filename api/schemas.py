from pydantic import BaseModel
from datetime import date
from typing import Optional

class TesteSistemaBase(BaseModel):
    id_implementacao: int
    resultado: Optional[str]
    detalhes_teste: Optional[str]
    data_teste: date
    responsavel_teste: str
    status: str

class TesteSistemaCreate(TesteSistemaBase):
    pass

class TesteSistemaUpdate(TesteSistemaBase):
    pass

class TesteSistemaOut(TesteSistemaBase):
    id_teste_sistema: int

    class Config:
        from_attributes = True
