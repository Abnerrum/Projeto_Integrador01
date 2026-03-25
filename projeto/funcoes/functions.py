import streamlit as st
import json

# Abrindo o arquivo de dados dos restaurantes. O 'r' significa leitura em inglês (read).
# O encoding='utf-8' garante que acentos (como ã, ç) sejam lidos corretamente.
with open('datasbank/gynRest.json', 'r', encoding='utf-8') as gRest:
    # 'json.load' transforma o texto do arquivo em uma lista/dicionário que o Python consegue entender.
    gynRest = json.load(gRest)
@st.cache_data
def push_gyn(): 
    # Como 'gynRest' tem vários restaurantes, nós usamos um "loop" (uma repetição).
    # A linha abaixo significa "Para cada item (que vamos chamar de 'i') dentro da lista completa 'gynRest', faça o seguinte:"
    for i in sorted(gynRest, key=lambda x: str(x.get('title', '')).lower()):
        with st.container(border = True):
        
        # 'st.write' é o comando do Streamlit para escrever textos na tela.
        # O 'f' antes das aspas (f"...") serve para misturar texto normal com variáveis dentro de chaves { }.
        
        # i.get('nome_da_variável', 'valor_padrão'):
        #   O '.get()' tenta pegar uma informação do restaurante (como 'title', que é o título/nome).
        #   Por que usamos isso no lugar de colocar só o N/A?
        #   Porque se algum restaurante no arquivo JSON estiver preenchido com erro e não tiver um 'title',
        #   o programa "cracharia" (daria erro e travaria). 
        #   Com o '.get()', se ele buscar e não achar o 'title', ele não dá erro, ele simplesmente usa
        #   o valor "N/A" (sigla em inglês para 'Não Disponível' / 'Não se Aplica') no lugar do nome.
            
            st.write(f"**Nome:** {i.get('title', 'N/A')}")
        
        # Pega a nota ('totalScore'). Se não achar, coloca 'N/A'.
        # Pela a quantidade de avaliações ('reviewsCount'). Se não achar, coloca '0'.
            st.write(f"**Nota:** {i.get('totalScore', 'N/A')} ({i.get('reviewsCount', '0')} avaliações)")
        
        # Pega a rua ('street'). Se não achar rua, põe 'N/A'.
            st.write(f"**Endereço:** {i.get('street', 'N/A')}")
        
        # Pega o link ('url'). O formato [Nome](link) é do Markdown para criar palavras "clicáveis".
        # Se não tiver a url, ele joga para o '#', que mantém o usuário na mesma página.
            st.page_link(f"{i.get('url', '#')}", label="Ver no Google Maps", icon = "📍")
            
            website = i.get('website')
            if website:
                st.page_link(f"{website}", label = "Ver Site", icon = "📷")
        # Escreve três tracinhos. Isso no Streamlit e no Markdown vira uma linha divisória para separar um restaurante do outro.
            
           