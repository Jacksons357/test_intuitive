COPY operadoras(
    registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento,
    bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante,
    regiao_comercializacao, data_registro_ans
)
FROM '/full/path/to/3_database/operadoras/Relatorio_cadop.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis(
    data, registro_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final
)
FROM '/full/path/to/3_database/2024/1T2024.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';
