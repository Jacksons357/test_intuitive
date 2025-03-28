import os
import requests
import zipfile
import tqdm
from bs4 import BeautifulSoup
import requests.compat

class RolProcedimentos:
  def __init__(self, path_dir, base_url):
    self.PATH_DIR = path_dir
    self.BASE_URL = base_url

    os.makedirs(self.PATH_DIR, exist_ok=True)

  def acessar_pagina(self):
    print("Acessando a página web...")
    response = requests.get(self.BASE_URL)
    if response.status_code != 200:
      raise Exception(f"Erro: Ao acessar a página: {response.status_code}")
    return BeautifulSoup(response.content, "html.parser")

  def encontrar_links_pdf(self, soup):
    print("Encontrando links para os PDFs...")
    pdf_links = []
    for a in soup.find_all("a", href=True):
      href = a["href"]
      if ".pdf" in href.lower() and ("anexo i" in a.get_text(strip=True).lower() or "anexo ii" in a.get_text(strip=True).lower()):
        pdf_links.append(href)
    if not pdf_links:
      raise Exception("Erro: Não foram encontrados os links para os anexos desejados!!")
    return pdf_links

  def baixar_arquivos(self, pdf_links):
    print("Baixando os arquivos PDF...")
    files_downloaded = []
    for link in tqdm.tqdm(pdf_links, desc="Downloads"):
      if not link.startswith("http"):
        link = requests.compat.urljoin(self.BASE_URL, link)
      
      pdf_response = requests.get(link)
      if pdf_response.status_code == 200:
        file_name = os.path.join(self.PATH_DIR, link.split("/")[-1])
        with open(file_name, "wb") as f:
          f.write(pdf_response.content) 
      
        files_downloaded.append(file_name)
        print(f"Arquivo baixado: {file_name}")
      else:
        print(f"Falha ao baixar: {link}")
    return files_downloaded

  def compactar_arquivos(self, files_downloaded):
    zip_name = "backend/downloads/rol_procedimentos/anexos.zip"
    print("Compactando os arquivos em ZIP...")
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
      for file in files_downloaded:
        zipf.write(file, arcname=os.path.basename(file))
    print(f"Arquivos compactados em: {zip_name}")

  def execute(self):
    soup = self.acessar_pagina()
    pdf_links = self.encontrar_links_pdf(soup)
    files_downloaded = self.baixar_arquivos(pdf_links)
    self.compactar_arquivos(files_downloaded)