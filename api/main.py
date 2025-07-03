from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from datetime import date
from typing import Literal

from  api import models, database

# Inicializa o aplicativo FastAPI
app = FastAPI(
    title="API de Testes de Sistema",
    description="Uma API para gerenciar registros de testes de sistema.",
    version="1.0.0"
)

# Cria as tabelas no banco de dados (execute isso uma vez)
@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=database.engine)

# Modelos Pydantic para Requisição/Resposta
class TesteSistemaBase(BaseModel):
    id_implementacao: int = Field(..., description="ID da Implementação testada.")
    resultado: Literal["Sucesso", "Falha", "Parcial"] = Field(..., description="Resultado do teste.")
    detalhes_teste: str = Field(..., description="Descrição dos testes executados.")
    data_teste: date = Field(..., description="Data da execução. Formato: YYYY-MM-DD")
    responsavel_teste: str = Field(..., description="Nome do testador.", max_length=100)
    status: Literal["1", "2"] = Field(..., description="[1] - Em andamento, [2] - Em aceite.")

class TesteSistemaCreate(TesteSistemaBase):
    pass

class TesteSistemaUpdate(TesteSistemaBase):
    pass

class TesteSistemaResponse(TesteSistemaBase):
    id_teste_sistema: int = Field(..., description="ID único do teste de sistema.")

    class Config:
        orm_mode = True # Habilita o modo ORM para mapeamento automático do modelo SQLAlchemy

# Endpoints da API

@app.post("/testes_sistema/", response_model=TesteSistemaResponse, status_code=201)
def criar_teste_sistema(test_data: TesteSistemaCreate, db: Session = Depends(database.get_db)):
    """
    Cria um novo registro de teste de sistema.
    """
    db_test = models.TesteSistema(**test_data.model_dump())
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

@app.get("/testes_sistema/", response_model=list[TesteSistemaResponse])
def ler_todos_testes_sistema(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """
    Retorna todos os registros de testes de sistema.
    """
    testes = db.query(models.TesteSistema).offset(skip).limit(limit).all()
    return testes

@app.get("/testes_sistema/{test_id}", response_model=TesteSistemaResponse)
def ler_teste_sistema(test_id: int, db: Session = Depends(database.get_db)):
    """
    Retorna um registro de teste de sistema pelo seu ID.
    """
    test = db.query(models.TesteSistema).filter(models.TesteSistema.id_teste_sistema == test_id).first()
    if test is None:
        raise HTTPException(status_code=404, detail="Teste de Sistema não encontrado")
    return test

@app.put("/testes_sistema/{test_id}", response_model=TesteSistemaResponse)
def atualizar_teste_sistema(test_id: int, test_data: TesteSistemaUpdate, db: Session = Depends(database.get_db)):
    """
    Atualiza um registro de teste de sistema existente.
    """
    db_test = db.query(models.TesteSistema).filter(models.TesteSistema.id_teste_sistema == test_id).first()
    if db_test is None:
        raise HTTPException(status_code=404, detail="Teste de Sistema não encontrado")

    for key, value in test_data.model_dump().items():
        setattr(db_test, key, value)

    db.commit()
    db.refresh(db_test)
    return db_test

@app.delete("/testes_sistema/{test_id}", response_model=dict)
def deletar_teste_sistema(test_id: int, db: Session = Depends(database.get_db)):
    """
    Deleta um registro de teste de sistema pelo seu ID.
    """
    db_test = db.query(models.TesteSistema).filter(models.TesteSistema.id_teste_sistema == test_id).first()
    if db_test is None:
        raise HTTPException(status_code=404, detail="Teste de Sistema não encontrado")

    db.delete(db_test)
    db.commit()
    return {"mensagem": "Teste de Sistema deletado com sucesso"}