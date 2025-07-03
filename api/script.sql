CREATE DATABASE sistema_teste;

USE sistema_teste;

CREATE TABLE teste_sistema (
    id_teste_sistema INT AUTO_INCREMENT PRIMARY KEY,
    id_implementacao INT NOT NULL,
    resultado VARCHAR(20),
    detalhes_teste TEXT,
    data_teste DATE,
    responsavel_teste VARCHAR(100),
    status VARCHAR(1)
);
