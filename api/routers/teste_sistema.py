from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import TesteSistemaCreate, TesteSistemaOut
from crud import criar_teste, listar_testes

router = APIRouter(prefix="/testes", tags=["Testes de Sistema"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TesteSistemaOut)
def criar_teste_sistema(teste: TesteSistemaCreate, db: Session = Depends(get_db)):
    return criar_teste(db, teste)

@router.get("/", response_model=list[TesteSistemaOut])
def listar_testes_sistema(db: Session = Depends(get_db)):
    return listar_testes(db)
