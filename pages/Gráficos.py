# --- Importar a biblioteca --- #
import streamlit as st

# --- Importar o módulo dos gráficos --- #
from graficos import Graficos

# --- Configurações da página --- #
st.set_page_config(page_title='Gráficos', layout='wide')

# --- Título da página --- #
st.title('Gráficos')

# --- Adicionar uma descrição --- #
st.write('---')
st.subheader('Nesta página é possível criar os gráficos do novo conjunto de dados.')
st.subheader('Os gráficos são totalmente interativos e criados em tempo real.')
st.write('---')

# --- Campo para enviar o arquivo --- #
upload = st.file_uploader(
    label='Escolha um arquivo CSV:',
    type='csv'
)

# --- Escolher o tipo de gráfico --- #
tipo_grafico = st.selectbox(
    label='Gráfico:',
    options=(
        'Histograma',
        'Boxplot',
        'Histograma + Boxplot',
        'Distribuição',
        'Pizza'
    ),
    index=None
)

# --- Criar as colunas para centralizar o botão --- #
colunas = st.columns(5)

# --- Criar o botão --- #
with colunas[2]:
    criar = st.button(
        label='Criar',
        use_container_width=True
    )


# --- Criar os gráficos --- #
if criar and upload and tipo_grafico:
    # --- Carregar a classe dos gráficos --- #
    criar_graficos = Graficos(upload)

    # --- Criar o histograma --- #
    if tipo_grafico == 'Histograma':
        criar_graficos.histograma()

    # --- Criar o boxplot --- #
    if tipo_grafico == 'Boxplot':
        criar_graficos.boxplot()

    # --- Criar o histograma + boxplot --- #
    if tipo_grafico == 'Histograma + Boxplot':
        criar_graficos.histograma_boxplot()

    # --- Criar o gráfico de distribuição --- #
    if tipo_grafico == 'Distribuição':
        criar_graficos.distribuicao()

    # --- Criar o gráfico de pizza --- #
    if tipo_grafico == 'Pizza':
        criar_graficos.pizza()