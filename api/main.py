from fastapi import FastAPI
from routers import teste_sistema
from database import Base, engine

app = FastAPI(title="API de Testes de Sistema")

Base.metadata.create_all(bind=engine)
app.include_router(teste_sistema.router)

@app.get("/")
def read_root():
    return {"mensagem": "API de Testes de Sistema funcionando. Vá para /docs"}
