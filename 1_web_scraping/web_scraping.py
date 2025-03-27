import requests
from bs4 import BeautifulSoup
import os
import zipfile
import tqdm

import requests.compat

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

download_dir = "1_web_scraping/anexos"
os.makedirs(download_dir, exist_ok=True)

print("Acessando a página web...")
response = requests.get(url)
if response.status_code != 200:
  raise Exception(f"Erro: Ao acessar a página: {response.status_code}")

soup = BeautifulSoup(response.content, "html.parser")

pdf_links = []

print("Encontrando links para os PDFs...")
for a in soup.find_all("a", href=True):
  href = a["href"]

  if ".pdf" in href.lower() and ("anexo i" in a.get_text(strip=True).lower() or "anexo ii" in a.get_text(strip=True).lower()):
    pdf_links.append(href)

if not pdf_links:
  raise Exception("Erro: Não foram encontrados os links para os anexos desejados!!")

files_downloaded = []

print("Baixando os arquivos PDF...")
for link in tqdm.tqdm(pdf_links, desc="Downloads"):
  if not link.startswith("http"):
    link = requests.compat.urljoin(url, link)
  
  pdf_response = requests.get(link)

  if pdf_response.status_code == 200:

    file_name = os.path.join(download_dir, link.split("/")[-1])
    with open(file_name, "wb") as f:
      f.write(pdf_response.content)
    
    files_downloaded.append(file_name)
    print(f"Arquivo baixado: {file_name}")
  
  else:
    print(f"Falha ao baixar: {link}")

zip_name = "1_web_scraping/anexos.zip"

print("Compactando os arquivos em ZIP...")
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
  for file in files_downloaded:
    zipf.write(file, arcname=os.path.basename(file))
print(f"Arquivos compactados em: {zip_name}")
