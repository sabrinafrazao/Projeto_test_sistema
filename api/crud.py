from sqlalchemy.orm import Session
from models import TesteSistema
from schemas import TesteSistemaCreate

def criar_teste(db: Session, dados: TesteSistemaCreate):
    novo_teste = TesteSistema(**dados.dict())
    db.add(novo_teste)
    db.commit()
    db.refresh(novo_teste)
    return novo_teste

def listar_testes(db: Session):
    return db.query(TesteSistema).all()
