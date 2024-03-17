from pathlib import Path
import streamlit as st 
from PIL import Image 

# Configurações Estruturais
diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
arquivo_css = diretorio / "styles" / "main.css"
arquivo_pdf = diretorio / "assets" / "Curriculo.pdf"
arquivo_imagem = diretorio / "assets" / "l.png"

# Configurações gerais das informações
TITULO = "Curriculum | LAURINDO DUMBA"
NOME = "Laurindo Dumba"
DESCRIÇÃO = """
Cientista de dados, Engenheiro de Machine Learning, aprendiz de desenvolvimento WEB.
"""

EMAIL = "dumbalvd@gmail.com"
MEDIA_SOCIAL = {
   "LinkedIn": "https://www.linkedin.com/in/laurindo-vilonga-dumba-45b214102/",
   "Midium": "https://medium.com/@dumbalvd",
   "GitHub": "https://github.com/laurindodumba"
}

PROJETOS = {
    "⭐ Credit Scoring": "https://github.com/laurindodumba/Risco-de-Credito",
    "⭐ Segmentação de Cliente": "https://github.com/laurindodumba/-PROJETO-DE_CIENCIA-DE-DADOS-SEGMENTACAO",
    "⭐ Contador de plástico": "https://github.com/laurindodumba/Contator-de-pl-sticos-usando-rede-neurais-e-YOLOV8",
    "⭐ Hackaton": "https://github.com/laurindodumba/Hackaton-Ciencia-de-Dados",
    "⭐ Análise de Crédito": "https://github.com/laurindodumba/-PROJETO-DE_CIENCIA-DE-DADOS-ANALISE-DE-CREDITO",
    "⭐ ETL API BANCO MUNDIAL": "https://github.com/laurindodumba/ETL-API-BANCO-MUNDIAL",
}

# Definindo configurações da página
st.set_page_config(
    page_title=TITULO,
    page_icon=None, # Adicione o ícone do site, se desejar
    layout="wide", # Altere para "wide" para aproveitar todo o espaço horizontal
    initial_sidebar_state="collapsed", # Minimizar a barra lateral inicialmente, se desejar
)

# Carregando as Assets
with open(arquivo_css) as c:
    st.markdown("<styles>{}</styles>".format(c.read()), unsafe_allow_html=True)
with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()
imagem = Image.open(arquivo_imagem)

# Cabeçalho
st.title(TITULO)

# Informações Pessoais
col1, col2 = st.columns([1, 4])
with col1:
    st.image(imagem, width=250)
with col2:
    st.title(NOME)
    st.write(DESCRIÇÃO)
    st.download_button(
        label="Download Curriculum",
        data=pdfLeitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-stream"
    )
    st.write("✉️ E-mail: ", EMAIL)

# Mídias sociais
st.write("#")
for plataforma, link in MEDIA_SOCIAL.items():
    st.markdown(f"[{plataforma}]({link}) |", unsafe_allow_html=True)

# Experiências, Skills, Certificações, Projetos, Qualificações acadêmicas podem continuar abaixo...
