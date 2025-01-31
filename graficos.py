# --- Importar as bibliotecas --- #
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

# --- Importar o módulo de abrir o CSV --- #
from abrir_csv import abrir_csv


class Graficos:
    """Classe responsável por criar os gráficos."""
    def __init__(self, arquivo):
        """Função responsável por inicializar a classe."""
       # --- Abrir o CSV no site --- #
        abrir_csv(arquivo)

        # --- Carregar os dados --- #
        self.dados = pd.read_csv('csv_temp.csv')

    def histograma(self):
        """Função responsável por criar os histogramas."""
        # --- Obter as colunas --- #
        colunas = [coluna for coluna in self.dados.columns if
                   self.dados[coluna].dtype != 'object' and coluna != 'CustomerID']

        # --- Criar os histogramas --- #
        for coluna in colunas:
            # --- Criar a figura --- #
            figura = go.Figure()

            # --- Criar o histograma --- #
            figura.add_trace(
                go.Histogram(x=self.dados[coluna])
            )

            # --- Informações do gráfico --- #
            figura.update_layout(
                title=coluna,
                yaxis_title='Quantidade de clientes',
            )

            # --- Colocar os gráficos na página --- #
            st.plotly_chart(figura)

    def boxplot(self):
        """Função responsável por criar os boxplot."""
        # --- Obter as colunas --- #
        colunas = [coluna for coluna in self.dados.columns if
                   self.dados[coluna].dtype != 'object' and coluna != 'CustomerID']

        # --- Criar os boxplots --- #
        for coluna in colunas:
            # --- Criar a figura --- #
            figura = go.Figure()

            # --- Criar o boxplot --- #
            figura.add_trace(
                go.Box(
                    x=self.dados[coluna],
                    boxmean=True
                )
            )

            # --- Informações do gráfico --- #
            figura.update_layout(title=coluna)

            # --- Colocar os gráficos na página --- #
            st.plotly_chart(figura)

    def histograma_boxplot(self):
        """Função responsável por criar o histograma + boxplot."""
        # --- Obter as colunas --- #
        colunas = [coluna for coluna in self.dados.columns if
                   self.dados[coluna].dtype != 'object' and coluna != 'CustomerID']

        # --- Criar os histogramas --- #
        for coluna in colunas:
            # --- Criar os gráficos --- #
            grafico = px.histogram(
                data_frame=self.dados,
                x=coluna,
                marginal='box',
                title=coluna
            )

            # --- Colocar os gráficos na página --- #
            st.plotly_chart(grafico)

    def distribuicao(self):
        """Função responsável por o gráfico de distribuição."""
        # --- Obter as colunas --- #
        colunas = [coluna for coluna in self.dados.columns if
                   self.dados[coluna].dtype != 'object' and coluna != 'CustomerID']

        # --- Criar os gráficos de distribuição --- #
        for coluna in colunas:
            # --- Tratar os dados --- #
            dados_brutos = self.dados[coluna]
            dados = [dados_brutos]

            # --- Criar o gráfico de dispersão --- #
            grafico = ff.create_distplot(
                hist_data=dados,
                group_labels=[coluna],
                show_rug=False,
                bin_size=[10],
                curve_type='normal'
            )

            # --- Colocar os gráficos na página --- #
            st.plotly_chart(grafico)

    def pizza(self):
        """Função responsável por criar o gráfico de pizza."""
        # --- Obter as colunas --- #
        colunas = [coluna for coluna in self.dados.columns if self.dados[coluna].dtype == 'object']

        # --- Criar as pizzas --- #
        for coluna in colunas:
            # --- Criar o gráfico --- #
            grafico = px.pie(
                data_frame=self.dados,
                names=coluna
            )

            # --- Colocar os gráficos na página --- #
            st.plotly_chart(grafico)
