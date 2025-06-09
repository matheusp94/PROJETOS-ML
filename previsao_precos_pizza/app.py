
import pandas as pd
from sklearn.linear_model import LinearRegression

import streamlit as st
import numpy as np
import pickle

# Carrega o modelo salvo
with open("modelo_treinado.pkl", "rb") as f:
    modelo = pickle.load(f)

# Título da aplicação
st.title("Previsão de Preço por Diâmetro")

# Entrada do usuário
diametro = st.number_input("Informe o diâmetro:", min_value=0.0, step=0.1)

# Previsão ao clicar no botão
if st.button("Prever preço"):
    entrada = np.array([[diametro]])
    preco_previsto = modelo.predict(entrada)
    st.success(f"Preço estimado: R$ {preco_previsto[0][0]:,.2f}")