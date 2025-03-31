DROP TABLE IF EXISTS operadoras;

CREATE TABLE operadoras (
  id SERIAL PRIMARY KEY,
  registro_ans VARCHAR(20) UNIQUE NOT NULL,
  cnpj VARCHAR(20) UNIQUE NOT NULL,
  razao_social VARCHAR(255) NOT NULL,
  nome_fantasia VARCHAR(255),
  modalidade VARCHAR(100),
  logradouro VARCHAR(255),
  numero VARCHAR(20),
  complemento VARCHAR(100),
  bairro VARCHAR(100),
  cidade VARCHAR(100),
  uf CHAR(2),
  cep VARCHAR(20),
  ddd VARCHAR(5),
  telefone VARCHAR(20),
  fax VARCHAR(20),
  endereco_eletronico VARCHAR(255),
  representante VARCHAR(255),
  cargo_representante VARCHAR(255),
  regiao_comercializacao VARCHAR(255),
  data_registro_ans DATE
);