from scrapers.rol_procedimentos import RolProcedimentos
from scrapers.data_transform import DataTransform
from database.download_data import DownloadData

print("\nOLÁ! SEJA BEM-VINDO AO TESTE PARA ESTÁGIO DE ENGENHEIRO DE SOFTWARE.")
print("MEU NOME É JACKSON SANTOS E VAMOS DAR INÍCIO AO TESTE.\n")
print("Caso tenha dúvidas, entre em contato comigo:\nEmail: contato@devjackson.tech")

def user_confirmation(message):
  return input(f"{message} (y/n): ").strip().lower() == 'y'

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

  print('\n⚠️ ATENÇÃO: É necessário estar conectado a internet e baixar todos os arquivos! ')
  if user_confirmation("\nDeseja baixar os arquivos de Atualização do Rol de Procedimentos?"):
    rol_procedimentos = RolProcedimentos(PATH_DIR_ROL, BASE_URL)
    rol_procedimentos.execute()
    print("\n✅ Download dos arquivos de Atualização do Rol de Procedimentos concluído!")

  if user_confirmation("\nAgora iremos transformar os dados em CSV e salvar em um arquivo .zip. Deseja continuar?"):
    data_transform = DataTransform(PATH_PDF, PATH_CSV, PATH_ZIP, PATH_DIR)
    data_transform.process()
    print("\n✅ Transformação dos dados concluída! Arquivos CSV e ZIP gerados com sucesso.")

  if user_confirmation("\nDeseja baixar os últimos 2 anos do repositório e os Dados Cadastrais das Operadoras Ativas na ANS?"):
    download_data = DownloadData(BASE_URL_DATA, OPERADORAS_URL, BASE_DIR)
    download_data.execute()
    print("\n✅ Download dos dados das operadoras concluído!")

  print("\n🚀 Processo finalizado! Todos os passos foram executados com sucesso. Obrigado por participar do teste!")
