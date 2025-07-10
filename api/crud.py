from sqlalchemy.orm import Session
from . import models, schemas

def get_all_tests(db: Session):
    return db.query(models.TesteSistema).all()

def get_test_by_id(db: Session, test_id: int):
    return db.query(models.TesteSistema).filter(models.TesteSistema.id_teste_sistema == test_id).first()

def create_test(db: Session, test: schemas.TesteSistemaCreate):
    db_test = models.TesteSistema(**test.dict())
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

def update_test(db: Session, test_id: int, test_data: schemas.TesteSistemaUpdate):
    test = get_test_by_id(db, test_id)
    if not test:
        return None
    for key, value in test_data.dict().items():
        setattr(test, key, value)
    db.commit()
    db.refresh(test)
    return test

def delete_test(db: Session, test_id: int):
    test = get_test_by_id(db, test_id)
    if not test:
        return None
    db.delete(test)
    db.commit()
    return test
