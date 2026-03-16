import streamlit as st
from cities.goiania import pagina_goiania
from cities.aparecida import pagina_aparecida
from cities.canedo import pagina_canedo
from pages import Encontre_aqui

st.set_page_config(
    page_title ="GoParty",
    page_icon=":beer:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("## GoParty: Localizador de Bares & Restaurantes")
st.markdown("###### Um Party Locator que encontra o entretenimento perfeito para você, com o preço certo! 😉")

