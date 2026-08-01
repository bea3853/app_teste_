import streamlit as st

# 1. Configuração da página (Deve ser o primeiro comando Streamlit)
st.set_page_config(
    page_title="Processamento de Dados & Automação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Estilização CSS personalizada para Design Minimalista
st.markdown("""
    <style>
        /* Oculta elementos do menu padrão do Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Ajuste do espaçamento topo/laterais */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 900px;
        }
        
        /* Estilização de Títulos e Cartões */
        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
            color: #1E293B;
            font-weight: 600;
        }
        
        .service-card {
            background-color: #F8FAFC;
            border-left: 4px solid #0284C7;
            padding: 1.2rem;
            margin-bottom: 1rem;
            border-radius: 4px;
        }
        
        .contact-box {
            background-color: #F1F5F9;
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO HERO ---
st.title("Transforme Dados Brutos em Decisões Inteligentes")
st.write("""
Ajudamos pequenas e médias empresas a automatizar tarefas repetitivas, organizar grandes volumes de dados e criar relatórios claros para impulsionar seus resultados.
""")

st.divider()

# --- SEÇÃO DE SERVIÇOS E IMAGENS ---
st.header("Nossos Serviços")

col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    # Imagem 1: Tamanho adaptável via use_container_width
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80", 
        caption="Análise e Visualização de Dados",
        use_container_width=True
    )
    st.markdown("""
    <div class="service-card">
        <h3>1. Estruturação & Limpeza de Dados</h3>
        <p>Organização de planilhas complexas, integração de bases de dados e eliminação de processos manuais.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Imagem 2: Tamanho adaptável via use_container_width
    st.image(
        "https://images.unsplash.com/photo-1518186285589-2f7649de83e0?auto=format&fit=crop&w=800&q=80", 
        caption="Automação de Processos",
        use_container_width=True
    )
    st.markdown("""
    <div class="service-card">
        <h3>2. Automação de Rotinas</h3>
        <p>Criação de fluxos automáticos para extração de dados, geração de relatórios e integração entre sistemas.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- DIFERENCIAIS ---
st.header("Por que Automatizar Conosco?")

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.subheader("⚡ Eficiência")
    st.caption("Reduza o tempo gasto em tarefas manuais repetitivas.")
with col_b:
    st.subheader("🎯 Precisão")
    st.caption("Elimine erros humanos na digitação e consolidação de dados.")
with col_c:
    st.subheader("📈 Escalabilidade")
    st.caption("Prepare sua empresa para crescer sem gargalos operacionais.")

# --- CONTATO & CHAMADA PARA AÇÃO ---
st.markdown("""
<div class="contact-box">
    <h2>Pronto para otimizar a sua operação?</h2>
    <p>Fale conosco para uma avaliação gratuita das necessidades da sua empresa.</p>
</div>
""", unsafe_allow_html=True)

# Formulário de contato direto
with st.form("contact_form", clear_on_submit=True):
    nome = st.text_input("Nome da empresa / Responsável")
    email = st.text_input("E-mail")
    mensagem = st.text_area("Como podemos ajudar?")
    submitted = st.form_submit_button("Enviar Mensagem")
    
    if submitted:
        if nome and email and mensagem:
            st.success("Obrigado pelo contato! Retornaremos em breve.")
        else:
            st.error("Por favor, preencha todos os campos.")

st.markdown("<br>", unsafe_allow_html=True)
st.caption("© 2026 Processamento de Dados - Todos os direitos reservados.")