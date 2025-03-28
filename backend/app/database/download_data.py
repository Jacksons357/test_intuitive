import os
import requests
import shutil
import zipfile
from bs4 import BeautifulSoup
from tqdm import tqdm

class DownloadData:
    def __init__(self, base_url_data, operadoras_url, base_dir):
        self.BASE_URL_DATA = base_url_data
        self.OPERADORAS_URL = operadoras_url
        self.BASE_DIR = base_dir

    def download_file(self, url, file_name):
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

    def extract_zip(self, file_path, extract_to):
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            print(f'Extraído: {file_path} → {extract_to}')

            os.remove(file_path)
            print(f'ZIP removido: {file_path}')
        except zipfile.BadZipFile:
            print(f'Erro: Arquivo ZIP corrompido ou inválido: {file_path}')

    def get_latest_years(self):
        response = requests.get(self.BASE_URL_DATA)
        soup = BeautifulSoup(response.content, 'html.parser')

        links = [link['href'].strip('/') for link in soup.find_all('a', href=True) if link['href'].endswith('/')]
        years = sorted([year for year in links if year.isdigit()], reverse=True)

        return years[:2]

    def get_all_files_in_year(self, year):
        year_url = f"{self.BASE_URL_DATA}{year}/"
        response = requests.get(year_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        all_files = [f"{year_url}{link['href']}" for link in soup.find_all('a', href=True) if link['href'].endswith(('.csv', '.xlsx', '.pdf', '.zip'))]
        return all_files

    def download_files_for_year(self, year):
        files = self.get_all_files_in_year(year)
        if not files:
            print(f"Nenhum arquivo encontrado para o ano {year}.")
            return

        for file_url in files:
            file_name = os.path.join(self.BASE_DIR, year, os.path.basename(file_url))
            self.download_file(file_url, file_name)

            if file_name.endswith('.zip'):
                self.extract_zip(file_name, os.path.dirname(file_name))

    def download_operadoras_csv(self):
        try:
            response = requests.get(self.OPERADORAS_URL)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            csv_links = [link['href'] for link in soup.find_all('a', href=True) if link['href'].endswith('.csv')]

            for csv_link in csv_links:
                file_name = os.path.join(self.BASE_DIR, "operadoras", os.path.basename(csv_link))
                self.download_file(f"{self.OPERADORAS_URL}{csv_link}", file_name)

        except requests.exceptions.RequestException as e:
            print(f'Erro ao baixar operadoras: {e}')

    def execute(self):
        latest_years = self.get_latest_years()

        for year in latest_years:
            print(f"Baixando arquivos do ano {year}...")
            self.download_files_for_year(year)

        self.download_operadoras_csv()
