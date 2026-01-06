from pathlib import Path
import streamlit as st
import base64

# ---------- CONFIGURAÇÕES E CAMINHOS ----------

diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()

arquivo_css = diretorio / "styles" / "main.css"
arquivo_pdf = diretorio / "assets" / "Curriculo.pdf"
arquivo_imagem = diretorio / "assets" / "l.png"

st.set_page_config(page_title="Portfólio - Laurindo Dumba", layout="centered")

# ---------- FUNÇÕES REUTILIZÁVEIS ----------

def load_css(path):
    if path.exists():
        with open(path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_rounded_image(path, size=250):
    if not path.exists():
        st.error("Imagem não encontrada no diretório assets.")
        return

    encoded = base64.b64encode(path.read_bytes()).decode()

    html = f"""
    <style>
    .rounded-img {{
        border-radius: 50%;
        width: {size}px;
        height: {size}px;
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

# ---------- CARREGANDO ARQUIVOS ----------

load_css(arquivo_css)
pdf_data = load_pdf(arquivo_pdf)

# ---------- CONTEÚDO DA PÁGINA ----------

# CABEÇALHO COM IMAGEM
show_rounded_image(arquivo_imagem)

st.title("Laurindo Dumba")

st.write("""
Engenharia de Dados | Machine Learning | Desenvolvimento Mobile
""")

st.write("✉️ E-mail: dumbalvd@gmail.com")

if pdf_data:
    st.download_button(
        label="Download Curriculum",
        data=pdf_data,
        file_name="Curriculo_Laurindo_Dumba.pdf",
        mime="application/pdf"
    )

# MÍDIAS SOCIAIS
st.write("#")
st.subheader("Mídias Sociais")

MEDIA_SOCIAL = {
    "LinkedIn": "https://www.linkedin.com/in/laurindo-vilonga-dumba-45b214102/",
    "Medium": "https://medium.com/@dumbalvd",
    "GitHub": "https://github.com/laurindodumba"
}

cols = st.columns(len(MEDIA_SOCIAL))
for i, (plat, link) in enumerate(MEDIA_SOCIAL.items()):
    cols[i].markdown(f"[{plat}]({link})")

# EXPERIÊNCIAS
st.write("#")
st.subheader("Experiências")

st.write("""
+4 anos de experiência em TI, com foco em:

⭐ Engenharia de Dados  
⭐ Machine Learning  
⭐ Desenvolvimento Mobile  
⭐ Cloud Computing (Azure & AWS)
""")

# SKILLS
st.write("#")
st.subheader("Skills Técnicas")

st.write("""
- 💻 Linguagens: Python, PySpark, R, SQL, Kotlin  
- ⚙️ Frameworks: Django, Flask, FastAPI, Jetpack Compose  
- ☁️ Cloud: Azure, AWS  
- 🐳 DevOps: Docker, GitHub, Databricks  
""")

# PROJETOS COM SCROLL LATERAL
st.write("#")
st.subheader("Projetos Desenvolvidos")

PROJETOS = {
    "Credit Scoring": "https://github.com/laurindodumba/Risco-de-Credito",
    "Segmentação de Cliente": "https://github.com/laurindodumba/-PROJETO-DE_CIENCIA-DE-DADOS-SEGMENTACAO",
    "ETL API Banco Mundial": "https://github.com/laurindodumba/ETL-API-BANCO-MUNDIAL",
    "Análise de Crédito": "https://github.com/laurindodumba/-PROJETO-DE_CIENCIA-DE-DADOS-ANALISE-DE-CREDITO",
}

scroll_html = """
<style>
.scrolling-wrapper {
    overflow-x: auto;
    white-space: nowrap;
}
.scrolling-wrapper button {
    display: inline-block;
    margin-right: 10px;
}
</style>
"""

st.markdown(scroll_html, unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="scrolling-wrapper">', unsafe_allow_html=True)
    for nome, link in PROJETOS.items():
        st.markdown(f'<a href="{link}" target="_blank"><button>{nome}</button></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# QUALIFICAÇÕES ACADÊMICAS
st.write("#")
st.subheader("Qualificações Acadêmicas")

st.write("""
🎓 Engenheiro de Controle e Automação  
🎓 Pós em Ciência de Dados e Big Data  
🎓 Pós em Inteligência Artificial  
🎓 Mestrando em Ciência da Computação  
""")

# RODAPÉ
st.write("#")
st.caption("© 2024 - Portfólio Online de Laurindo Dumba")
