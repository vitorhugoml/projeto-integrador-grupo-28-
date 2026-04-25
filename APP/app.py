import streamlit as st
import pandas as pd
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Projeto Integrador - Grupo 28",
    page_icon="🚀",  # O emoji pode ser alterado caso o grupo queira
    layout="wide"
)

# Carregar o CSV tratado
BASE_DIR = Path(__file__).resolve().parent

@st.cache_data
def load_data():
    caminho = BASE_DIR / "Data/processed/titanic_cleaned.csv"
    return pd.read_csv(caminho)

df = load_data()

# Criar a sidebar (estrutura)
st.sidebar.title("Filtros")

# ---------- BLOCO ISABELLA ---------
# Aqui entram os filtros da sidebar

# --------------------------------------

# PASSO 6 — Criar área de KPIs
st.markdown("## KPIs Gerais")
col1, col2, col3, col4 = st.columns(4)

# ---------- BLOCO DA ISABELLA ---------
# Aqui entram os KPIs

# --------------------------------------
