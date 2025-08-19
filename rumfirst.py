import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Carregar os dados e adicionar coluna 'Empresa'
path = r"C:\Users\pedro\.cache\kagglehub\datasets\azharsaleem\us-stock-market-giants-top-companies-stocks-data\versions\1\US_Stocks"
arquivos_csv = [f for f in os.listdir(path) if f.endswith('.csv')]
dfs = []
for arquivo in arquivos_csv:
    df = pd.read_csv(os.path.join(path, arquivo))
    empresa = arquivo.replace('.csv', '')
    df['Empresa'] = empresa
    dfs.append(df)
df_total = pd.concat(dfs, ignore_index=True)
df_total['Date'] = pd.to_datetime(df_total['Date'], errors='coerce', utc=True)
df_total = df_total.dropna(subset=['Date'])
df_total['Ano'] = df_total['Date'].dt.year
df_total['Mes'] = df_total['Date'].dt.month
df_total['Decada'] = (df_total['Ano'] // 10) * 10

# Filtro de empresa
empresas = df_total['Empresa'].unique()
empresa_selecionada = st.sidebar.selectbox('Selecione a empresa:', sorted(empresas))

# Filtra o DataFrame pela empresa escolhida
df_empresa = df_total[df_total['Empresa'] == empresa_selecionada]

# Agrupa por ano e mês
tabela_mensal = df_empresa.groupby(['Ano', 'Mes']).mean(numeric_only=True).reset_index()

# Sidebar para seleção de ano ou década
opcao = st.sidebar.radio('Selecione:', ['Ano', 'Década'])

if opcao == 'Ano':
    anos = tabela_mensal['Ano'].unique()
    ano_selecionado = st.sidebar.selectbox('Selecione o ano:', sorted(anos))
    dados_filtrados = tabela_mensal[tabela_mensal['Ano'] == ano_selecionado]
    fig = px.line(dados_filtrados, x='Mes', y='Close', title=f'Preço Médio Mensal de Fechamento - {empresa_selecionada} - {ano_selecionado}')
    st.plotly_chart(fig)
else:
    decadas = df_empresa['Decada'].unique()
    decada_selecionada = st.sidebar.selectbox('Selecione a década:', sorted(decadas))
    dados_decada = tabela_mensal[tabela_mensal['Ano'].between(decada_selecionada, decada_selecionada + 9)]
    dados_decada['Ano-Mes'] = dados_decada['Ano'].astype(str) + '-' + dados_decada['Mes'].astype(str)
    fig = px.line(dados_decada, x='Ano-Mes', y='Close', title=f'Preço Médio Mensal de Fechamento - {empresa_selecionada} - Década {decada_selecionada}')
    st.plotly_chart(fig)