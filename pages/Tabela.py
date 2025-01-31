# --- Importar a biblioteca --- #
import streamlit as st

# --- Importar o módulo de criação da tabela --- #
from tabela import tabela

# --- Configurações da página --- #
st.set_page_config(page_title='Tabela', layout='wide')

# --- Título da página --- #
st.title('Tabela')

# --- Informações da página --- #
st.write('---')
st.subheader('Nesta página você terá acesso a tabela com informações estatísticas dos dados.')
st.write('---')

# --- Colocar o campo para adicionar o arquivo CSV --- #
upload = st.file_uploader(
    label='Escolha um arquivo CSV:',
    type='csv'
)

# --- Verificar se o arquivo foi adicionado ao site --- #
if upload:
    # --- Mostrar a tabela com os dados estatísticos --- #
    st.write(tabela(upload))
