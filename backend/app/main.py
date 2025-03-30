from scrapers.rol_procedimentos import RolProcedimentos
from scrapers.data_transform import DataTransform
from database.download_data import DownloadData
from database.run_database import RunDatabase
from database.filter_operadoras import FilterOperadoras
from database.filter_all_operadoras import FilterAllOperadoras
import os

print("\nOLÁ! SEJA BEM-VINDO AO TESTE PARA ESTÁGIO DE ENGENHEIRO DE SOFTWARE.")
print("MEU NOME É JACKSON SANTOS E VAMOS DAR INÍCIO AO TESTE.\n")
print("Caso tenha dúvidas, entre em contato comigo:\nEmail: contato@devjackson.tech")

if __name__ == "__main__":
  BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
  PATH_DIR_ROL = "backend/downloads/rol_procedimentos"

  PATH_PDF = "backend/downloads/rol_procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
  PATH_CSV = "extract_data.csv"
  PATH_ZIP = "backend/downloads/data_transform/Teste_Jackson_Santos.zip"
  PATH_DIR = "backend/downloads/data_transform"

  BASE_URL_DATA = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
  OPERADORAS_URL = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"
  BASE_DIR = "backend/downloads/data"

  print("\n1 - TESTE DE WEB SCRAPING. ")
  rol_procedimentos = RolProcedimentos(PATH_DIR_ROL, BASE_URL)
  rol_procedimentos.execute()
  print("\n✅ Download dos arquivos de Atualização do Rol de Procedimentos concluído!")

  print("\n2 - TESTE DE TRANSFORMAÇÃO DE DADOS.")
  data_transform = DataTransform(PATH_PDF, PATH_CSV, PATH_ZIP, PATH_DIR)
  data_transform.process()
  print("\n✅ Transformação dos dados concluída! Arquivos CSV e ZIP gerados com sucesso.")

  print("\n3 - TESTE DE BANCO DE DADOS.")
  download_data = DownloadData(BASE_URL_DATA, OPERADORAS_URL, BASE_DIR)
  download_data.execute()
  print("\n✅ Download dos dados concluído!")
    
  print("\n3 - INSERINDO DADOS NA TABELA.")
  database = RunDatabase()
  database.drop_table()
  database.create_table()
  database.process_csv_files()
  print("\n✅ Dados inseridos com sucesso!")
  
  print("\n3.5 Filtrando as 10 operadoras com maiores despesas no último trimestre.")
  path_file = os.path.join("backend","downloads", "data", "2024", "4T2024.csv")
  path_output = "backend/downloads/data/top10_operadoras.csv"
  process = FilterOperadoras(path_file, path_output)
  process.processar_dados()
  print("\n✅ Filtragem realizada com sucesso!")
  
  print("\n3.5 Filtrando as 10 operadoras com maiores despesas no último ano.")
  path_file = os.path.join("backend", "downloads", "data", "2024")
  path_output = "backend/downloads/data/top10_operadoras_1_ano.csv"
  process = FilterAllOperadoras(path_file, path_output)
  process.processar_dados()
  print("\n✅ Filtragem realizada com sucesso!")

