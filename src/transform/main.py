import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json('data/data.jsonl', lines = True)

pd.options.display.max_columns = None

df['_source'] = 'https://lista.mercadolivre.com.br/jogo-nintendo-switch#D[A:jogo%20nintendo%20switch]'

df['_date_time'] = datetime.now()

df['old_money'] = df['old_money'].fillna('0')
df['new_money'] = df['new_money'].fillna('0')
df['seller'] = df['seller'].fillna('Sem vendedor explícito')
df['reviews_amount'] = df['reviews_amount'].fillna('(0)')
df['seller'] = df['seller'].fillna('0')

df['old_money'] = df['old_money'].astype(str).str.replace('.', '', regex=False)
df['new_money'] = df['new_money'].astype(str).str.replace('.', '', regex=False)
df['reviews_amount'] = df['reviews_amount'].astype(str).str.replace('[\(\)]', '', regex=True)

df = df[
    (df['brand'] == "NINTENDO")
]

conn = sqlite3.connect('data/mercadolivre.db')

df.to_sql('game', conn, if_exists='replace', index=False)

conn.close()