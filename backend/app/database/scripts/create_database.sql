DROP TABLE IF EXISTS operadoras;
DROP TABLE IF EXISTS demonstracoes_contabeis;

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

CREATE TABLE demonstracoes_contabeis (
  id SERIAL PRIMARY KEY,
  data DATE NOT NULL,
  registro_ans VARCHAR(20) NOT NULL,
  cd_conta_contabil VARCHAR(20) NOT NULL,
  descricao VARCHAR(255),
  vl_saldo_inicial DECIMAL(15,2),
  vl_saldo_final DECIMAL(15,2)
);
