import streamlit as st
import requests
from datetime import datetime

def obter_cotaçoes_simples(par):
    url= f"https://economia.awesomeapi.com.br/json/last/{par}"
    resposta= requests.get(url)
    if resposta.status_code == 200:
        dados= resposta.json()
        chave= par.replace("-", "")
        return float(dados[chave]["bid"])
    return 0.0

st.subheader("Cotação em destaque")

col1, col2, col3 = st.columns(3)

cotaçao_eua= obter_cotaçoes_simples("USD-BRL")
cotaçao_eur= obter_cotaçoes_simples("EUR-BRL")
cotaçao_btc= obter_cotaçoes_simples("BTC-BRL")

with col1:
    st.metric("Dolar (USD)", f"R$ {cotaçao_eua:.4f}")

with col2:
    st.metric("Euro (EUR)", f"R$ {cotaçao_eur:.4f}")

with col3:
    st.metric("Bitcoin (BTC)", f"R$ {cotaçao_btc:.4f}")

def get_cotaçao_bid(par):
    url= f"https://economia.awesomeapi.com.br/json/last/{par}"
    resposta= requests.get(url)
    if resposta.status_code == 200:
        dados= resposta.json()
        return dados[par.replace("-", "")]["bid"]
    return None

st.title("Menu financeiro V2")

tabcotaçao, tabconversor, tabhistorico = st.tabs([
    "Cotação atual", "Conversor", "Histórico"
])

with tabcotaçao:
    st.header("Cotação em tempo real")
    cotaçao= get_cotaçao_bid("USD-BRL")

    if cotaçao:
        st.success(f"1 USD = R$ {float(cotaçao):.4f}")
    else:
        st.warning("Falha ao obter dados da API")

with tabconversor:
    st.header("Conversor de moedas")
    valor= st.number_input("Valor em USD", min_value= 0.0, value= 100.0, step= 10.0)
    if st.button("Converter"):
        cotaçao= get_cotaçao_bid("USD-BRL")
        if cotaçao:
            resultado= float(valor)*float(cotaçao)
            st.success(f"{resultado:.4f}")

st.divider()

def data_completa(par):
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = par.replace("-", "")
        return dados[chave]
    return None

st.header("Dados de referência")
st.divider()

dados_usd= data_completa("USD-BRL")

if dados_usd:
    st.subheader(f"Cotação {dados_usd['name']}")

    col3, col4= st.columns(2)

    with col3:
        st.metric("Máximo (High)", dados_usd['high'])

    with col4:
        st.metric("Mínimo (Low)", dados_usd['low'])

st.divider()
st.info(f"Dados atualizados na API em: {dados_usd['create_date']}")

