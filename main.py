import os  # noqa: F401
import sqlite3

import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title='Visualizador de Tabelas SQLite',
    page_icon=':bar_chart:',
    layout='wide',
    initial_sidebar_state='collapsed',
)

st.title('Visualizador de Tabelas SQLite')

# Carrega o arquivo .db
uploaded_file = st.file_uploader('Escolha um arquivo .db', type='db')

if uploaded_file is not None:
    # Salva o arquivo carregado em uma localização temporária
    db_file_path = uploaded_file.name

    with open(db_file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Obtém a lista de tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]

    if table_names:
        # Seleciona uma tabela para exibir
        selected_table = st.selectbox('Selecione uma tabela', table_names)

        if selected_table:
            # Consulta a tabela selecionada
            query = f'SELECT * FROM {selected_table}'
            df = pd.read_sql_query(query, conn)

            # Exibe a tabela
            st.write(f'Conteúdo da tabela {selected_table}:')
            st.dataframe(df)

    # Fecha a conexão
    conn.close()
