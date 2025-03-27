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

path_pdf = "1_web_scraping/anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
path_csv = "extract_data.csv"
path_zip = f"2_data_transform/Teste_Jackson_Santos.zip"

if not os.path.exists(path_pdf):
  print(f'---------------------------------------')
  print(f'Erro: Arquivo PDF não encontrado em: {path_pdf}')
  print(f'---------------------------------------')
  print(f'Para resolver este erro, gere o arquivo em 1_web_scraping!')
  exit()

def extract_data_pdf(path_pdf):
  print("Extraindo dados do PDF...")
  data = []
  with pdfplumber.open(path_pdf) as pdf:
    for page in tqdm.tqdm(pdf.pages, desc='Páginas'):
      text = page.extract_table()
      if text:
        for line in text:
          data.append(line)
  return data

def save_in_csv(data, path_csv):
  print("Salvando dados em CSV...")
  with open(path_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

def replace_shortening(path_csv):
  print("Substituindo abreviações...")
  df = pd.read_csv(path_csv)
  df.replace(shortening, inplace=True)
  df.to_csv(path_csv, index=False)

def compact_csv_in_zip(path_csv, path_zip):
  print("Compactando CSV em ZIP...")
  with zipfile.ZipFile(path_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(path_csv, os.path.basename(path_csv))

data_extracts = extract_data_pdf(path_pdf)
save_in_csv(data_extracts, path_csv)
replace_shortening(path_csv)
compact_csv_in_zip(path_csv, path_zip)

os.remove(path_csv)

print(f'Arquivo zipado criado com sucesso: {path_zip}')