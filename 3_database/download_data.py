import os
import requests
import shutil
import zipfile
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_URL = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
OPERADORAS_URL = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"
BASE_DIR = "3_database"

def download_file(url, file_name):
  try:
    response = requests.get(url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))

    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    with tqdm.wrapattr(open(file_name, 'wb'), 'write', miniters=1, total=total_size, desc=os.path.basename(file_name)) as file:
      shutil.copyfileobj(response.raw, file)

    print(f'Arquivo {file_name} baixado com sucesso!')
  except requests.exceptions.RequestException as e:
    print(f'Erro ao baixar: {url} - {e}')

def extract_zip(file_path, extract_to):
  try:
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
      zip_ref.extractall(extract_to)
    print(f'Extraído: {file_path} → {extract_to}')
    
    os.remove(file_path)
    print(f'ZIP removido: {file_path}')
  except zipfile.BadZipFile:
    print(f'Erro: Arquivo ZIP corrompido ou inválido: {file_path}')

def get_latest_years():
  response = requests.get(BASE_URL)
  soup = BeautifulSoup(response.content, 'html.parser')

  links = [link['href'].strip('/') for link in soup.find_all('a', href=True) if link['href'].endswith('/')]
  years = sorted([year for year in links if year.isdigit()], reverse=True)

  return years[:2]

def get_all_files_in_year(year):
  year_url = f"{BASE_URL}{year}/"
  response = requests.get(year_url)
  soup = BeautifulSoup(response.content, 'html.parser')

  all_files = []

  for link in soup.find_all('a', href=True):
    href = link['href']
    if href.endswith(('.csv', '.xlsx', '.pdf', '.zip')):  
      all_files.append(f"{year_url}{href}")

  return all_files

def download_files_for_year(year):
  files = get_all_files_in_year(year)
  if not files:
    print(f"Nenhum arquivo encontrado para o ano {year}.")
  
  for file_url in files:
    file_name = os.path.join(BASE_DIR, year, os.path.basename(file_url))  
    download_file(file_url, file_name)

    if file_name.endswith('.zip'):
      extract_zip(file_name, os.path.dirname(file_name))

def download_operadoras_csv():
  try:
    response = requests.get(OPERADORAS_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    csv_links = [link['href'] for link in soup.find_all('a', href=True) if link['href'].endswith('.csv')]

    os.makedirs("operadoras", exist_ok=True)

    for csv_link in csv_links:
      file_name = os.path.join(BASE_DIR, "operadoras", os.path.basename(csv_link))
      download_file(f"{OPERADORAS_URL}{csv_link}", file_name)
  
  except requests.exceptions.RequestException as e:
    print(f'Erro ao baixar operadoras: {e}')

latest_years = get_latest_years()

for year in latest_years:
  print(f"Baixando arquivos do ano {year}...")
  download_files_for_year(year)

download_operadoras_csv()
