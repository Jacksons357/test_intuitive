import pdfplumber
import pandas as pd
import csv
import zipfile
import os
import tqdm

shortening = {
  "OD": "Odontológica",
  "AMB": "Ambulatorial"
}

class DataTransform:
  def __init__(self, path_pdf, path_csv, path_zip, path_dir):
    self.PATH_PDF = path_pdf
    self.PATH_CSV = path_csv
    self.PATH_ZIP = path_zip
    self.PATH_DIR = path_dir

    os.makedirs(self.PATH_DIR, exist_ok=True)

    if not os.path.exists(self.PATH_PDF):
      print(f'---------------------------------------')
      print(f'Erro: Arquivo PDF não encontrado em: {self.PATH_PDF}')
      print(f'---------------------------------------')
      print(f'É necessário fazer o download dos arquivos de Atualizacao do Rol de Procedimentos primeiro!')
      print(f'---------------------------------------')
      exit()

  def extract_data_pdf(self):
    print("Extraindo dados do PDF...")
    data = []
    with pdfplumber.open(self.PATH_PDF) as pdf:
      for page in tqdm.tqdm(pdf.pages, desc='Páginas'):
        text = page.extract_table()
        if text:
          for line in text:
            data.append(line)
    return data

  def save_in_csv(self, data):
    print("Salvando dados em CSV...")
    with open(self.PATH_CSV, mode='w', newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerows(data)

  def replace_shortening(self):
    print("Substituindo abreviações...")
    df = pd.read_csv(self.PATH_CSV)
    df.replace(shortening, inplace=True)
    df.to_csv(self.PATH_CSV, index=False)

  def compact_csv_in_zip(self):
    print("Compactando CSV em ZIP...")
    with zipfile.ZipFile(self.PATH_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
      zipf.write(self.PATH_CSV, os.path.basename(self.PATH_CSV))

  def process(self):
    data_extracts = self.extract_data_pdf()
    self.save_in_csv(data_extracts)
    self.replace_shortening()
    self.compact_csv_in_zip()

    os.remove(self.PATH_CSV)

    print(f'Arquivo zipado criado com sucesso: {self.PATH_ZIP}')