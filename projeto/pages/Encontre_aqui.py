import streamlit as st
from cities.goiania import pagina_goiania
from cities.aparecida import pagina_aparecida
from cities.canedo import pagina_canedo
from funcoes.functions import push_gyn

# Configura as propriedades básicas da página (título da aba, ícone e estado inicial do menu lateral)
st.set_page_config(
    page_title = f"GoParty | Search",
    page_icon = ":beer:",
    
)

# Renderiza o título do menu lateral
st.sidebar.title("Menu")

# Dicionário que mapeia o nome da cidade no menu (string) para a função que renderiza a página daquela cidade
pgs = {
    "Goiânia": pagina_goiania,  
    "Aparecida": pagina_aparecida,
    "Senador Canedo": pagina_canedo
}

# Inicializa um estado de sessão (session_state) para lembrar qual cidade o usuário selecionou.
# O padrão inicial é Goiânia
if 'selected_city' not in st.session_state:
    st.session_state.selected_city = "Goiânia"
    
st.sidebar.markdown("### Selecione uma cidade:")

# Itera sobre as cidades no dicionário 'pgs' e cria um botão no menu lateral para cada uma
# Quando clicado, atualiza a cidade selecionada no estado da sessão
for cidade in pgs.keys():
    if st.sidebar.button(cidade):
        st.session_state.selected_city = cidade
        
# Recupera a função da cidade selecionada a partir do dicionário 'pgs'
pgs_selected = pgs[st.session_state.selected_city]
pgs_selected()
# Executa a função, efetivamente renderizando o conteúdo da cidade selecionada na tela principal

   
