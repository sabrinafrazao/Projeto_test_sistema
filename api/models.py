# api_testes_sistema/models.py
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from .database import Base

class TesteSistema(Base):
    __tablename__ = "testes_sistema" # Nome da tabela no banco de dados

    id_teste_sistema = Column(Integer, primary_key=True, index=True)
    # Assumindo que 'implementacoes' é a tabela onde os IDs de implementação residem.
    # Se esta tabela não existe ou se a lógica da FK é diferente, ajuste conforme necessário.
    id_implementacao = Column(Integer, ForeignKey("implementacoes.id_implementacao"), nullable=False)
    resultado = Column(String(20))
    detalhes_teste = Column(Text)
    data_teste = Column(Date)
    responsavel_teste = Column(String(100))
    status = Column(String(1)) # [1] - Em andamento, [2] - Em aceite.

    def __repr__(self):
        return f"<TesteSistema(id_teste_sistema={self.id_teste_sistema}, id_implementacao={self.id_implementacao}, resultado='{self.resultado}')>"