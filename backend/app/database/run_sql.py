import os
import csv
import mysql.connector
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

def connect_db():
  return mysql.connector.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
  )

def drop_table():
  conn = connect_db()
  cursor = conn.cursor()

  cursor.execute("DROP TABLE IF EXISTS operadoras;")
  
  cursor.close()
  conn.close()

def create_table():
  conn = connect_db()
  cursor = conn.cursor()

  with open('backend/database/scripts/create_database.sql', 'r', encoding='utf-8') as f:
    sql = f.read()

  cursor.execute(sql)
  
  cursor.close()
  conn.close()

drop_table()

create_table()

def insert_operadoras_from_csv(file_path):
  conn = connect_db()
  cursor = conn.cursor()

  with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)

    rows = list(reader)

    for row in tqdm(rows, desc=f'Inserindo dados de {file_path}', unit='registro'):
      cursor.execute("""
        INSERT INTO operadoras (
          registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero,
          complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, 
          representante, cargo_representante, regiao_comercializacao, data_registro_ans
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
      """, row)
      conn.commit()
      
  cursor.close()
  conn.close()

def insert_demonstracoes_contabeis_from_csv(file_path):
  conn = connect_db()
  cursor = conn.cursor()

  with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)

    rows = list(reader)

    for row in tqdm(rows, desc=f'Inserindo dados de {file_path}', unit='registro'):
      row[4] = row[4].replace(',', '.')
      row[5] = row[5].replace(',', '.')
      
      cursor.execute("""
        INSERT INTO demonstracoes_contabeis (data, registro_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
        VALUES (%s, %s, %s, %s, %s, %s)
      """, row)
      conn.commit()


  cursor.close()
  conn.close()

def process_csv_files():
  BASE_DIR = 'backend/database/data'
    
  year_dir = os.path.join(BASE_DIR, 'operadoras')
  if os.path.exists(year_dir):
    for file_name in os.listdir(year_dir):
      if file_name.endswith('.csv'):
        file_path = os.path.join(year_dir, file_name)
        print(f'Inserindo dados de {file_path} na tabela operadoras...')
        insert_operadoras_from_csv(file_path)
        print(f'Dados de {file_path} inseridos com sucesso na tabela operadoras!')

  for year in ['2023', '2024']:
    year_dir = os.path.join(BASE_DIR, year)
    if os.path.exists(year_dir):
      for file_name in os.listdir(year_dir):
        if file_name.endswith('.csv') and 'Relatorio_cadop' not in file_name:
          file_path = os.path.join(year_dir, file_name)
          print(f'Inserindo dados de {file_path} na tabela demonstracoes_contabeis...')
          insert_demonstracoes_contabeis_from_csv(file_path)
          print(f'Dados de {file_path} inseridos com sucesso na tabela demonstracoes_contabeis!')

process_csv_files()

print('Todos os arquivos CSV foram processados e os dados foram inseridos com sucesso!')
