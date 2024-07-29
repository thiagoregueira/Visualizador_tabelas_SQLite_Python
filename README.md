# Visualizador de Tabelas SQLite

Este projeto é um aplicativo web desenvolvido com Streamlit que permite aos usuários visualizar tabelas de arquivos SQLite (.db).

## Projeto em Produção

O projeto está atualmente em produção e pode ser acessado no seguinte endereço:

[https://visualizadortabelas.streamlit.app/](https://visualizadortabelas.streamlit.app/)

## Descrição

O Visualizador de Tabelas SQLite é uma ferramenta simples e eficiente que permite aos usuários carregar um arquivo de banco de dados SQLite (.db), selecionar uma tabela e visualizar seu conteúdo em formato de dataframe. Esta aplicação é útil para desenvolvedores, analistas de dados e qualquer pessoa que precise inspecionar rapidamente o conteúdo de um banco de dados SQLite.

## Funcionalidades

- Upload de arquivos de banco de dados SQLite (.db)
- Listagem de todas as tabelas presentes no banco de dados
- Seleção de uma tabela específica para visualização
- Exibição do conteúdo da tabela em formato de dataframe

## Tecnologias Utilizadas

- Python
- Streamlit
- SQLite3
- Pandas

## Instalação e Uso

Para executar este projeto localmente, siga estas etapas:

1. Clone o repositório:
  https://github.com/thiagoregueira/Visualizador_tabelas_SQLite_Python.git
  cd Visualizador_tabelas_SQLite_Python

2. Instale as dependências:
  pip install -r requirements.txt

3. Execute o aplicativo:
  streamlit run main.py

4. Abra seu navegador e acesse `http://localhost:8501`

## Exemplos de Uso

1. Clique no botão "Browse files" para selecionar um arquivo .db
2. Após o upload, selecione uma tabela do banco de dados no menu dropdown
3. O conteúdo da tabela selecionada será exibido em formato de dataframe

## Estrutura do Projeto
```
visualizador-tabelas-sqlite/
│
├── app.py          # Código principal do aplicativo
├── requirements.txt # Lista de dependências
└── README.md       # Este arquivo
```


## Dependências

- streamlit
- pandas
- sqlite3 (incluído na biblioteca padrão do Python)


