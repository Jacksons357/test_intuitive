import mysql.connector
import os

class OperatorService:
  def __init__(self):
    self.conn = mysql.connector.connect(
      database=os.getenv("DB_NAME"),
      user=os.getenv("DB_USER"),
      password=os.getenv("DB_PASSWORD"),
      host=os.getenv("DB_HOST"),
      port=os.getenv("DB_PORT")
    )
    self.cursor = self.conn.cursor(dictionary=True)

  def list_operators(self):
    query = "SELECT * FROM operadoras"
    self.cursor.execute(query)
    return self.cursor.fetchall()

  def search_operators(self, search_term):
    query = """
      SELECT * FROM operadoras
      WHERE registro_ans LIKE %s
      OR cnpj LIKE %s
      OR razao_social LIKE %s
      OR nome_fantasia LIKE %s
      OR modalidade LIKE %s
      OR logradouro LIKE %s
      OR numero LIKE %s
      OR complemento LIKE %s
      OR bairro LIKE %s
      OR cidade LIKE %s
      OR uf LIKE %s
      OR cep LIKE %s
      OR telefone LIKE %s
      OR endereco_eletronico LIKE %s
      OR representante LIKE %s
      OR cargo_representante LIKE %s
      OR regiao_comercializacao LIKE %s
      OR data_registro_ans LIKE %s
    """
    params = tuple('%' + search_term + '%' for _ in range(18))
    self.cursor.execute(query, params)
    return self.cursor.fetchall()