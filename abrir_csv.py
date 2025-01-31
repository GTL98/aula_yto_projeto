# --- Importar a biblioteca --- #
from io import StringIO


def abrir_csv(arquivo):
    """Função responsável por abrir o arquivo CSV no site."""
    # --- Carregar o arquivo --- #
    arquivo_carregado = arquivo.getvalue()

    # --- Converter de bytes para letras --- #
    arquivo_io = StringIO(arquivo_carregado.decode('utf8-'))

    # --- Lista com as linhas do documento --- #
    linhas = arquivo_io.readlines()

    # --- Criar o arquivo CSV temporário --- #
    with open('csv_temp.csv', 'w') as doc:
        for linha in linhas:
            doc.write(linha)