from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from database import Base

class TesteSistema(Base):
    __tablename__ = "teste_sistema"

    id_teste_sistema = Column(Integer, primary_key=True, index=True)
    id_implementacao = Column(Integer, nullable=False)  # FK de outra API
    resultado = Column(String(20))
    detalhes_teste = Column(Text)
    data_teste = Column(Date)
    responsavel_teste = Column(String(100))
    status = Column(String(1))  # [1] - Em andamento, [2] - Em aceite
