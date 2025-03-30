import pandas as pd
import os
from tqdm import tqdm

class FilterAllOperadoras:
  def __init__(self, folder_path: str, output_path: str):
    self.folder_path = folder_path
    self.output_path = output_path

  def processar_dados(self):
    try:
      files = [f for f in os.listdir(self.folder_path) if f.endswith('.csv')]

      if not files:
        print(f"Erro: Nenhum arquivo CSV encontrado na pasta {self.folder_path}")
        return

      all_data = []

      for file in tqdm(files, desc="Processando arquivos", ncols=100):
        path_file = os.path.join(self.folder_path, file)
        df = pd.read_csv(path_file, on_bad_lines='skip', sep=';', encoding='utf-8')

        if 'DESCRICAO' not in df.columns:
          print(f"Erro: A coluna 'DESCRICAO' não foi encontrada no arquivo {file}.")
          continue

        df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace('.', '', regex=False)
        df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.', regex=False)
        df['VL_SALDO_INICIAL'] = pd.to_numeric(df['VL_SALDO_INICIAL'], errors='coerce')
        df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].fillna(0)

        filter_desc = df['DESCRICAO'].str.contains(
          'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ', 
          case=False, na=False,
        )
        df_filtred = df[filter_desc]
        df_filtred = df_filtred[
          ['DATA', 'REG_ANS', 'CD_CONTA_CONTABIL', 'DESCRICAO', 'VL_SALDO_INICIAL', 'VL_SALDO_FINAL']
        ]
        
        all_data.append(df_filtred)

      df_combined = pd.concat(all_data, ignore_index=True)

      df_top10 = df_combined.nlargest(10, 'VL_SALDO_INICIAL')

      df_top10.to_csv(self.output_path, index=False)
      print(f"Arquivo gerado: {self.output_path}")

    except FileNotFoundError:
        print(f"Erro: Pasta não encontrada em {self.folder_path}")
    except pd.errors.ParserError:
        print(f"Erro: Problema ao analisar os arquivos CSV em {self.folder_path}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
