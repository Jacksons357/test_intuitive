import os
import csv
import mysql.connector
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

class RunDatabase:
  def __init__(self):
    self.conn = None
    self.cursor = None

  def connect_db(self):
    self.conn = mysql.connector.connect(
      database=os.getenv("DB_NAME"),
      user=os.getenv("DB_USER"),
      password=os.getenv("DB_PASSWORD"),
      host=os.getenv("DB_HOST"),
      port=os.getenv("DB_PORT")
    )
    self.cursor = self.conn.cursor()

  def close_connection(self):
    if self.cursor:
      self.cursor.close()
    if self.conn:
      self.conn.close()

  def drop_table(self):
    self.connect_db()
    self.cursor.execute("DROP TABLE IF EXISTS operadoras;")
    self.close_connection()

  def create_table(self):
    self.connect_db()
    with open('backend/app/database/scripts/create_database.sql', 'r', encoding='utf-8') as f:
      sql = f.read()
    self.cursor.execute(sql)
    self.close_connection()

  def insert_operadoras_from_csv(self, file_path):
    self.connect_db()
    with open(file_path, 'r', encoding='utf-8') as f:
      reader = csv.reader(f, delimiter=';')
      next(reader)
      rows = list(reader)
      for row in tqdm(rows, desc=f'Inserindo dados de {file_path}', unit='registro'):
        self.cursor.execute("""
          INSERT INTO operadoras (
            registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero,
            complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, 
            representante, cargo_representante, regiao_comercializacao, data_registro_ans
          ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, row)
        self.conn.commit()
    self.close_connection()

  def insert_demonstracoes_contabeis_from_csv(self, file_path):
    self.connect_db()
    with open(file_path, 'r', encoding='utf-8') as f:
      reader = csv.reader(f, delimiter=';')
      next(reader)
      rows = list(reader)
      for row in tqdm(rows, desc=f'Inserindo dados de {file_path}', unit='registro'):
        row[4] = row[4].replace(',', '.')
        row[5] = row[5].replace(',', '.')
        self.cursor.execute("""
          INSERT INTO demonstracoes_contabeis (data, registro_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
          VALUES (%s, %s, %s, %s, %s, %s)
        """, row)
        self.conn.commit()
    self.close_connection()

  def process_csv_files(self):
      BASE_DIR = 'backend/downloads/data'
      year_dir = os.path.join(BASE_DIR, 'operadoras')
      if os.path.exists(year_dir):
        for file_name in os.listdir(year_dir):
          if file_name.endswith('.csv'):
            file_path = os.path.join(year_dir, file_name)
            print(f'Inserindo dados de {file_path} na tabela operadoras...')
            self.insert_operadoras_from_csv(file_path)
            print(f'Dados de {file_path} inseridos com sucesso na tabela operadoras!')