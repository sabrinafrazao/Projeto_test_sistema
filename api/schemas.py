# api_testes_sistema/schemas.py
from pydantic import BaseModel, Field
from datetime import date
from typing import Literal

# Modelo base para TesteSistema, contendo os campos comuns para criação e atualização
class TesteSistemaBase(BaseModel):
    id_implementacao: int = Field(..., description="ID da Implementação testada. **Esperado de outra API.**")
    resultado: Literal["Sucesso", "Falha", "Parcial"] = Field(..., description="Resultado do teste: 'Sucesso', 'Falha' ou 'Parcial'.")
    detalhes_teste: str = Field(..., description="Descrição detalhada dos testes executados.")
    data_teste: date = Field(..., description="Data da execução do teste. Formato: YYYY-MM-DD.")
    responsavel_teste: str = Field(..., description="Nome completo do testador.", max_length=100)
    status: Literal["1", "2"] = Field(..., description="Status do teste: '1' para 'Em andamento', '2' para 'Em aceite'.")

# Modelo para criar um novo registro de teste de sistema (herda de TesteSistemaBase)
class TesteSistemaCreate(TesteSistemaBase):
    """Modelo para a payload de criação de um novo teste de sistema."""
    pass

# Modelo para atualizar um registro de teste de sistema (herda de TesteSistemaBase)
class TesteSistemaUpdate(TesteSistemaBase):
    """Modelo para a payload de atualização de um teste de sistema existente."""
    pass

# Modelo de resposta para um registro de teste de sistema (inclui o ID e configura para ORM)
class TesteSistemaResponse(TesteSistemaBase):
    """Modelo de resposta que inclui o ID do teste de sistema."""
    id_teste_sistema: int = Field(..., description="ID único e primário do teste de sistema.")

    class Config:
        # Permite que o Pydantic seja compatível com modelos ORM (SQLAlchemy)
        orm_mode = True
        from_attributes = True # Para Pydantic v2+