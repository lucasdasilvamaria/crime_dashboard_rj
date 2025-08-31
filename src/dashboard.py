# dashboard.py

# Importação das bibliotecas essenciais:
import pandas as pd           # Pandas: manipulação de dados tabulares (DataFrames)
import plotly.express as px  # Plotly Express: para gráficos interativos
import streamlit as st       # Streamlit: criar dashboards web interativos
from datetime import datetime  # Para manipulação de datas (não usado diretamente, mas útil para referência)

# Configuração da página do Streamlit
# page_title: define o título da aba do navegador
# layout="wide": deixa o layout da página em largura total
st.set_page_config(page_title="Crime Dashboard RJ", layout="wide")


# Função para carregar e pré-processar os dados
# @st.cache_data: indica que os dados carregados serão "cacheados", evitando recarregar toda vez que a página atualizar
@st.cache_data
def carregar_dados():
    # Lê o CSV do caminho absoluto, com separador ponto-e-vírgula
    # dtype=str garante que todas as colunas sejam lidas como strings inicialmente
    df = pd.read_csv(
        r"C:\Users\User\PycharmProjects\PythonProject\crimes_rj\data\BaseEstadoTaxaMes.csv",
        sep=";", dtype=str
    )

    # Limpeza inicial:
    # applymap aplica a função lambda a cada célula do DataFrame
    # Se for string, remove aspas e espaços extras do início/fim
    df = df.applymap(lambda x: x.strip().replace('"', '') if isinstance(x, str) else x)

    # Conversão das colunas "ano" e "mes" para números
    # errors="coerce": valores que não forem convertíveis viram NaN
    df["ano"] = pd.to_numeric(df["ano"], errors="coerce")
    df["mes"] = pd.to_numeric(df["mes"], errors="coerce")

    # Criação de coluna datetime para facilitar séries temporais
    # Concatena "ano" e "mes" em uma string no formato 'YYYY-MM-01'
    # str.zfill(2) garante que o mês tenha dois dígitos (01, 02,...,12)
    # pd.to_datetime converte a string em objeto datetime
    df["mes_ano"] = pd.to_datetime(df["ano"].astype(str) + "-" + df["mes"].astype(str).str.zfill(2) + "-01")

    # Conversão de todas as outras colunas numéricas
    # Para cada coluna que não seja "ano", "mes" ou "mes_ano":
    for c in df.columns:
        if c not in ["ano", "mes", "mes_ano"]:
            # Substitui vírgulas por pontos (padronização decimal)
            # Remove quaisquer caracteres que não sejam números, ponto ou sinal de menos
            df[c] = (
                df[c].astype(str)
                .str.replace(",", ".", regex=False)
                .str.replace(r"[^\d\.\-]", "", regex=True)
            )
            # Converte finalmente para numérico, valores inválidos viram NaN
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # Retorna o DataFrame limpo e pronto para uso
    return df


# Carrega os dados chamando a função definida acima
df = carregar_dados()


# Título principal do dashboard
st.title("Crime Dashboard - Rio de Janeiro")

# Cabeçalho da barra lateral para filtros
st.sidebar.header("Filtros")


# Slider para selecionar faixa de anos
# sorted(df["ano"].dropna().unique()): pega todos os anos distintos ordenados
anos = sorted(df["ano"].dropna().unique())
# select_slider: slider de seleção dupla para faixa inicial e final
ano_inicio, ano_fim = st.sidebar.select_slider(
    "Selecione a faixa de anos",
    options=anos,
    value=(anos[0], anos[-1])  # valores padrão: primeiro e último ano disponível
)


# Seleção de múltiplos tipos de crimes
# Lista todas as colunas que não são "ano", "mes" ou "mes_ano" (ou seja, só os crimes)
crime_cols = [c for c in df.columns if c not in ["ano", "mes", "mes_ano"]]
# multiselect: permite selecionar múltiplos crimes para análise
# default=[crime_cols[0]]: seleciona automaticamente o primeiro crime da lista
crimes_selecionados = st.sidebar.multiselect(
    "Selecione os crimes",
    options=crime_cols,
    default=[crime_cols[0]]
)


# Filtra os dados do DataFrame conforme a faixa de anos selecionada
df_filtrado = df[(df["ano"] >= ano_inicio) & (df["ano"] <= ano_fim)]


# Exibe uma tabela interativa dos dados filtrados
st.subheader(f"Tabela de crimes de {ano_inicio} a {ano_fim}")
# dataframe: mostra as colunas "mes_ano", "ano" + os crimes selecionados pelo usuário
st.dataframe(df_filtrado[["mes_ano", "ano"] + crimes_selecionados])


# Gráfico de linhas interativo
# Primeiro, verifica se o DataFrame filtrado não está vazio e se há dados válidos nas colunas selecionadas
if not df_filtrado.empty and any(df_filtrado[c].notna().any() for c in crimes_selecionados):
    # px.line: cria gráfico de linha
    fig = px.line(
        df_filtrado,
        x="mes_ano",           # eixo X: datas
        y=crimes_selecionados,  # eixo Y: valores dos crimes selecionados
        labels={"mes_ano": "Mês/Ano", "value": "Casos", "variable": "Crime"},  # nomes para legendas
        title=f"Tendência de crimes de {ano_inicio} a {ano_fim}"  # título do gráfico
    )
    # Formata o eixo X para mostrar mês/ano
    fig.update_layout(xaxis_tickformat="%b/%Y")
    # Exibe o gráfico no dashboard, ajustando à largura do container
    st.plotly_chart(fig, use_container_width=True)
else:
    # Caso não haja dados disponíveis para a seleção do usuário
    st.warning("Não há dados para a faixa de anos/crimes selecionados.")
