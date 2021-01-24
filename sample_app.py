import streamlit as st

# 今回使うデータのサンプル


st.write('# Stremlit Sample App :baseball:')
st.write('データは[こちらのアプリ](https://github.com/Shinichi-Nakagawa/prefect-baseball-etl)で作ったものです')

st.write('## ひとまずpandasデータフレームの中身を見る')
st.write('`st.write(df.head())`とかやればいい感じに')
st.info('''
```python
import pandas as pd

df = pd.read_csv('datasets/mlb_batter_stats.csv')
st.write(df.head())
```
''')

import pandas as pd

df = pd.read_csv('datasets/mlb_batter_stats.csv')
st.write(df.head())

# サイドバーを使ってみる

st.sidebar.markdown(
    """
    # sidebar sample
    """
)
first_name = st.sidebar.text_input('First Name', 'Shohei')
last_name = st.sidebar.text_input('Last Name', 'Ohtani')
bats = st.sidebar.multiselect(
    "打席",
    ('右', '左'),
    ('右', '左'),
)

st.write('## 打者の打席で絞る')
st.info('''
```python
query = None
if '右' in bats:
    query = 'bats=="R"'
if '左' in bats:
    query = 'bats=="L"'
if ('右', '左') == bats:
    query = 'bats=="R" or bats=="L"'
if query:
    df_bats = df.query(query)
    st.write(df_bats.head())
```
''')

query = None
if '右' in bats:
    query = 'bats=="R"'
if '左' in bats:
    query = 'bats=="L"'
if ('右', '左') == bats:
    query = 'bats=="R" or bats=="L"'
if query:
    df_bats = df.query(query)
    st.write(df_bats.head())

st.write('## 入力した名前に従って変更するサンプル')

st.info('''
```python
st.write(f'### {first_name} {last_name}の成績')
df_query = df.query(f'nameFirst=="{first_name}" and nameLast=="{last_name}"').sort_values('yearID')
st.write(df_query.head(30))
```
''')

st.write(f'### {first_name} {last_name}の成績')
df_query = df.query(f'nameFirst=="{first_name}" and nameLast=="{last_name}"').sort_values('yearID')
st.write(df_query.head(30))

st.write('## グラフを書く')
st.write('例は[plotly](https://plotly.com/python/)ですが他でもいけます')
st.info('''
```python

import plotly.graph_objects as go


# グラフレイアウト
def graph_layout(fig, x_title, y_title):
    return fig.update_layout(
        xaxis_title=x_title,
        yaxis_title=y_title,
        autosize=False,
        width=1024,
        height=768
    )


title = f'{first_name} {last_name}の成績'

fig = go.Figure(data=[
    go.Bar(name='安打', x=df_query['yearID'], y=df_query['H']),
    go.Bar(name='本塁打', x=df_query['yearID'], y=df_query['HR']),
    go.Bar(name='打点', x=df_query['yearID'], y=df_query['RBI'])
])
fig = graph_layout(fig, x_title='年度', y_title=title)
fig.update_layout(barmode='group', title=title)

st.write(fig)

```
''')

import plotly.graph_objects as go


# グラフレイアウト
def graph_layout(fig, x_title, y_title):
    return fig.update_layout(
        xaxis_title=x_title,
        yaxis_title=y_title,
        autosize=False,
        width=1024,
        height=768
    )


title = f'{first_name} {last_name}の成績'

fig = go.Figure(data=[
    go.Bar(name='安打', x=df_query['yearID'], y=df_query['H']),
    go.Bar(name='本塁打', x=df_query['yearID'], y=df_query['HR']),
    go.Bar(name='打点', x=df_query['yearID'], y=df_query['RBI'])
])
fig = graph_layout(fig, x_title='年度', y_title=title)
fig.update_layout(barmode='group', title=title)

st.write(fig)
