import streamlit as st

import pandas as pd

# 今回使うデータのサンプル

df = pd.read_csv('datasets/mlb_batter_stats.csv')

st.write('# ひとまずDataframeの中身を出す')

st.write(df.head())