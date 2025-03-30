import pandas as pd

class FilterOperadoras:
  def __init__(self, file_path: str, output_path: str):
    self.file_path = file_path
    self.output_path = output_path

  def processar_dados(self):
    try:
      df = pd.read_csv(self.file_path, on_bad_lines='skip', sep=';', encoding='utf-8')
      if 'DESCRICAO' not in df.columns:
        print("Erro: A coluna 'DESCRICAO' não foi encontrada no arquivo CSV.")
        return

      df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace('.', '', regex=False)
      df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.', regex=False)
      df['VL_SALDO_INICIAL'] = pd.to_numeric(df['VL_SALDO_INICIAL'], errors='coerce')
      df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].fillna(0)

      filtro = df['DESCRICAO'].str.contains(
        'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ', case=False, na=False,
      )
      df_filtrado = df[filtro]
      df_filtrado = df_filtrado[
        ['DATA', 'REG_ANS', 'CD_CONTA_CONTABIL', 'DESCRICAO', 'VL_SALDO_INICIAL', 'VL_SALDO_FINAL']
      ]
      df_top10 = df_filtrado.nlargest(10, 'VL_SALDO_INICIAL')
      df_top10.to_csv(self.output_path, index=False)
      print(f"Arquivo gerado: {self.output_path}")

    except FileNotFoundError:
      print(f"Erro: Arquivo não encontrado em {self.file_path}")
    except pd.errors.ParserError:
      print(f"Erro: Problema ao analisar o arquivo CSV em {self.file_path}")
    except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}")