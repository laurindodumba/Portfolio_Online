from pathlib import Path
import streamlit as st
import base64


def show_section(title, content_function):
    st.markdown(f'<div class="section-circle">', unsafe_allow_html=True)
    st.markdown(f'<h3 class="section-title">{title}</h3>', unsafe_allow_html=True)

    content_function()

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- CONFIGURAÇÕES ----------

diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()

arquivo_css = diretorio / "styles" / "main.css"
arquivo_pdf = diretorio / "assets" / "Curriculo.pdf"
arquivo_imagem = diretorio / "assets" / "l.png"

st.set_page_config(page_title="Portfólio - Laurindo Dumba", layout="centered")

# ---------- CARREGAR CSS ----------

with open(arquivo_css) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- FUNÇÕES ----------

def show_rounded_image(path):
    encoded = base64.b64encode(path.read_bytes()).decode()
    html = f"""
    <style>
    .rounded-img {{
        border-radius: 50%;
        width: 250px;
        height: 250px;
        object-fit: cover;
        display: block;
        margin: auto;
    }}
    </style>

    <img class="rounded-img" src="data:image/png;base64,{encoded}">
    """
    st.markdown(html, unsafe_allow_html=True)

def load_pdf(path):
    if path.exists():
        with open(path, "rb") as f:
            return f.read()
    return None

def show_section(title, content_function):
    st.markdown('<div class="section-circle">', unsafe_allow_html=True)
    st.markdown(f'<h3 class="section-title">{title}</h3>', unsafe_allow_html=True)
    content_function()
    st.markdown('</div>', unsafe_allow_html=True)

pdf_data = load_pdf(arquivo_pdf)

# ---------- DADOS GERAIS ----------

MEDIA_SOCIAL = {
    "LinkedIn": "https://www.linkedin.com/in/laurindo-vilonga-dumba-45b214102/",
    "Medium": "https://medium.com/@dumbalvd",
    "GitHub": "https://github.com/laurindodumba"
}

PROJETOS = {
    "Credit Scoring": "https://github.com/laurindodumba/Risco-de-Credito",
    "Segmentação de Cliente": "https://github.com/laurindodumba/-PROJETO-DE_CIENCIA-DE-DADOS-SEGMENTACAO",
    "ETL API Banco Mundial": "https://github.com/laurindodumba/ETL-API-BANCO-MUNDIAL"
}

# CABEÇALHO
show_rounded_image(arquivo_imagem)

st.title("Laurindo Dumba")
st.write("Engenharia de Dados | Machine Learning | Desenvolvimento Mobile")
st.write("✉️ E-mail: dumbalvd@gmail.com")

if pdf_data:
    st.download_button(
        label="Download Curriculum",
        data=pdf_data,
        file_name="Curriculo_Laurindo_Dumba.pdf",
        mime="application/pdf"
    )

# ---------- CONTEÚDOS POR SEÇÃO ----------

def conteudo_social():
    cols = st.columns(len(MEDIA_SOCIAL))
    for i, (plat, link) in enumerate(MEDIA_SOCIAL.items()):
        cols[i].markdown(f"[{plat}]({link})")

def conteudo_experiencias():
    st.write("""
⭐ Mais de 4 anos atuando em TI  
⭐ Projetos de Machine Learning  
⭐ APIs com FastAPI  
⭐ Desenvolvimento Mobile com Compose  
""")

def conteudo_skills():
    st.write("""
- Python, PySpark, R, SQL, Kotlin  
- Django, Flask, FastAPI  
- Azure e AWS  
- Docker e GitHub  
""")

def conteudo_projetos():
    st.write("-----")
    cols = st.columns(len(PROJETOS))
    for i, (nome, link) in enumerate(PROJETOS.items()):
        cols[i].markdown(f"[{nome}]({link})")

def conteudo_academico():
    st.write("""
🎓 Engenheiro de Controle e Automação  
🎓 Pós em Ciência de Dados  
🎓 Pós em Inteligência Artificial  
🎓 Mestrando em Ciência da Computação  
""")

# MOSTRANDO AS SEÇÕES EM REGIÕES CIRCULARES

show_section("Mídias Sociais", conteudo_social)

show_section("Experiências", conteudo_experiencias)

show_section("Skills", conteudo_skills)

show_section("Projetos Desenvolvidos", conteudo_projetos)

show_section("Qualificações Acadêmicas", conteudo_academico)

# RODAPÉ
st.write("#")
st.caption("© 2024 - Portfólio Online de Laurindo Dumba")
