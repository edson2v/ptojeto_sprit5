import streamlit as st
import pandas as pd
import plotly.express as px

# Ler o arquivo CSV do conjunto de dados
car_data = pd.read_csv('vehicles.csv')

# Cabeçalho do aplicativo
st.header('Análise Exploratório de Dados')

# Texto explicativo ou instruções para o usuário
st.write('Este é um exemplo de um aplicativo Streamlit para análise de dados')

# Botão para criar o histograma
if st.button('Exibir Histograma'):
    # Criar histograma com Plotly Express
    fig = px.histogram(car_data, x='price', title="Distribuição de Preços")

    # Exibir o gráfico no aplicativo
    st.plotly_chart(fig)

# Botão para exibir o gráfico de dispersão
if st.button("Exibir Gráfico de dispersão"):
    # Criar gráfico de dispersão usando Plotly Express
    fig = px.scatter(car_data, x='model', y="price", title="Gráfico de Dispersão")

    # Exibir o gráfico no aplicativo
    st.plotly_chart(fig)

# Exibir a tabela de dados
st.write('Aqui está uma prévia do conjunto de dados')
st.dataframe(car_data.head())


