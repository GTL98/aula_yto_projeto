# --- Importar o módulo de abrir o CSV --- #
import pandas as pd
from abrir_csv import abrir_csv


def tabela(arquivo):
    """Função responsável por retornar a tabela com as informações estatísticas."""
    # --- Abrir o CSV --- #
    abrir_csv(arquivo)

    # --- Obter os dados --- #
    dados = pd.read_csv('csv_temp.csv')

    # --- Criar uma tabela com os dados estatísticos --- #
    info_estatisticas = dados.describe().T

    # --- Excluir a linha do ID di cliente --- #
    info_estatisticas.drop('CustomerID', axis=0, inplace=True)

    # --- Renomear as colunas --- #
    info_estatisticas.rename(
        columns={
            'count': 'Quantidade de clientes',
            'mean': 'Média',
            'std': 'Desvio padrão',
            'min': 'Mínimo',
            'max': 'Máximo'
        },
        inplace=True
    )

    return info_estatisticas