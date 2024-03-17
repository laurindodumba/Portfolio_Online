from pathlib import Path
import streamlit as st 
from PIL import Image 



# Cabeçalho
st.header("Meu Portfólio")

# Barra Lateral
st.sidebar.title("Menu")
st.sidebar.markdown("Selecione uma opção abaixo:")

# opcao = st.sidebar.radio("Navegação", ["Home", "Projetos", "Sobre"])

# if opcao == "Home":
#     st.title("Página Inicial")
#     # Aqui você pode adicionar o conteúdo da página inicial
# elif opcao == "Projetos":
#     st.title("Projetos")
#     # Aqui você pode adicionar o conteúdo da página de projetos
# elif opcao == "Sobre":
#     st.title("Sobre")
#     # Aqui você pode adicionar o conteúdo da página "Sobre"




#Configurações Estruturais~
diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
arquivo_css = diretorio / "styles" / "main.css"
arquivo_pdf = diretorio / "assets" / "Curriculo.pdf"
arquivo_imagem = diretorio / "assets" / "l.png"


#Configurações gerais das informações

TITULO = "Curriculum  | LAURINDO DUMBA"
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
     
    " ⭐ Credit Scoring" : "https://github.com/laurindodumba/Risco-de-Credito",

    " ⭐ Segmentação de Cliente ": "https://github.com/laurindodumba/-PROJETO-DE_CIENCIA-DE-DADOS-SEGMENTACAO",

    " ⭐ Contador de plástico": "https://github.com/laurindodumba/Contator-de-pl-sticos-usando-rede-neurais-e-YOLOV8",
    
    " ⭐ Hackaton ": "https://github.com/laurindodumba/Hackaton-Ciencia-de-Dados",

    " ⭐ Análise de Crédito " : "https://github.com/laurindodumba/-PROJETO-DE_CIENCIA-DE-DADOS-ANALISE-DE-CREDITO",

    " ⭐  ETL API BANCO MUNDIAL ": "https://github.com/laurindodumba/ETL-API-BANCO-MUNDIAL",





}

st.set_page_config(
    page_title=TITULO
)

#Carregando as Assets
with open(arquivo_css) as c:
    st.markdown("<styles>{}</styles>".format(c.read()), unsafe_allow_html=True)
with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()
imagem = Image.open(arquivo_imagem)


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(imagem, width=250)
with col2:
    st.title(NOME)
    st.write(DESCRIÇÃO)
    st.download_button(
        label="Downlaod Curriculum",
        data= pdfLeitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-stream"
    )
    st.write("✉️ E-mail : ", EMAIL)


# Mídias sociais
    st.write("#")
    colunas = st.columns(len(MEDIA_SOCIAL))
    for indice, (plataforma, link) in enumerate(MEDIA_SOCIAL.items()):
        colunas[indice].write(f"[{plataforma}]({link})")



#Experiências
    st.write("#")
    st.subheader("Experiências")
    st.write(
    """
        	📌 +2 anos de experiências em Tecnologia da informação sobre tudo nas seguintes áreas:

            ⭐ Engenharia de Dados

            ⭐ Ciência de Dados

            ⭐ Machine Learning
    """
    )

# Skills
    st.write("#")
    st.subheader("SKILLS")
    st.write(
    """

            - 💻 Programação (Python PySpark, R, SQL)

            - ⚙️ Django, Flask, Databricks, DevOps, Databricks, Git Hub, Docker, MLFLOW

            - ☁️ Microsoft Azure, AWS
    """
    )

#Certificações
    st.write("#")
    st.subheader("CERTIFICAÇÕES")
    st.write(
        """
           - 🏅 AZ 900

           - 🏅 AI 900

           - 🏅 PL 900

           - 🏅 DP 900

           - 🏅 AZ -220 IOT Developer Specialtly
        """
    )


# Projetos
    st.write("#")
    st.subheader("PROJETOS DESENVOLVIDOS")
    st.write("-----")
    # for projeto, link in PROJETOS.items():
    #     st.write(f"[{PROJETOS}]({link})")



    
    coluna = st.columns(len(PROJETOS))
    for indi, (plataform, link) in enumerate(PROJETOS.items()):
            coluna[indi].write(f"[{plataform}]({link})")

# Qualitificações académicas
    
    st.write("#")
    st.subheader("QUALIFICAÇÕES ACADÊMICAS")
    st.write(
        """
        - 🚀 Engenheiro de Controle e Automação

        - 🚀 Pós Graduação em Ciência de Dados e Big Data

        - 🚀 Pós Graduação em Inteligência Artificial e Computacional

        - 🚀 Mestrando em Ciência da Computação
        """
    )




# Rodapé
st.footer("© 2024 Laurindo Dumba - Todos os direitos reservados.")
