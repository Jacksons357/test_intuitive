from scrapers.rol_procedimentos import RolProcedimentos
from scrapers.data_transform import DataTransform

if __name__ == "__main__":
  BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
  PATH_DIR_ROL = "backend/downloads/rol_procedimentos"

  PATH_PDF = "backend/downloads/rol_procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
  PATH_CSV = "extract_data.csv"
  PATH_ZIP = "backend/downloads/data_transform/Teste_Jackson_Santos.zip"
  PATH_DIR = "backend/downloads/data_transform"
  
  rol_procedimentos = RolProcedimentos(PATH_DIR_ROL, BASE_URL)
  rol_procedimentos.executar()

  data_transform = DataTransform(PATH_PDF, PATH_CSV, PATH_ZIP, PATH_DIR)
  data_transform.process()