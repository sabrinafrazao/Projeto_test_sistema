# api_testes_sistema/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Substitua com suas credenciais MySQL se forem diferentes das padrões do XAMPP
# Certifique-se de que o nome do banco de dados (banco_testes) corresponda ao que você criou no phpMyAdmin
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/3306"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
