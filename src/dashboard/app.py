# import
import streamlit as st
import pandas as pd
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('data/mercadolivre.db')

# Carregar os dados da tabela 'game' em um DataFrame pandas
df = pd.read_sql_query("SELECT * FROM game", conn)

# Fechar a conexão com o banco de dados
conn.close()

# Título da aplicação
st.title('🎮 Pesquisa de Mercado - Jogos Nintendo Switch')

# KPIs principais
st.subheader('📊 Indicadores Gerais')
col1, col2, col3 = st.columns(3)

# KPI 1: Total de jogos
total_games = df.shape[0]
col1.metric(label="🎮 Total de Jogos", value=total_games)

# KPI 3: Preço médio novo (em reais)
df['new_money'] = pd.to_numeric(df['new_money'], errors='coerce')
average_price = df['new_money'].mean()
col3.metric(label="💰 Preço Médio (R$)", value=f"{average_price:.2f}")

# Jogos mais vendidos por vendedor (se quiser ver isso)
st.subheader('🏪 Top vendedores por número de jogos listados')
top_sellers = df['seller'].value_counts().head(10)
col1, col2 = st.columns([4, 2])
col1.bar_chart(top_sellers)
col2.write(top_sellers)

# Preço médio por vendedor
st.subheader('💸 Preço médio por vendedor')
average_price_by_seller = df.groupby('seller')['new_money'].mean().sort_values(ascending=False).head(10)
col1, col2 = st.columns([4, 2])
col1.bar_chart(average_price_by_seller)
col2.write(average_price_by_seller)

# Satisfação média por vendedor
df['reviews_rating_number'] = pd.to_numeric(df['reviews_rating_number'], errors='coerce')
st.subheader('⭐ Satisfação média por vendedor')
avg_rating_by_seller = df.groupby('seller')['reviews_rating_number'].mean().sort_values(ascending=False).head(10)
col1, col2 = st.columns([4, 2])
col1.bar_chart(avg_rating_by_seller)
col2.write(avg_rating_by_seller)

# Última atualização
st.caption(f"📅 Dados coletados em: {df['_date_time'].max()}")
