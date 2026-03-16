import streamlit as st
from funcoes.functions import push_gyn

def pagina_goiania():
   st.title("Goiânia")
   st.write("Hub da maior cidade do estado de Goiás, encontre aqui os melhores pontos da cidade!")    
   
   push_gyn()
