import streamlit as st
import altair as alt

def main_filters(df):
    """Cria os filtros na tela principal"""
    st.subheader("Filtros de Pesquisa")
    col1, col2, col3 = st.columns(3)

    with col1:
        categoria = st.selectbox("Categoria", df['categoria'].unique())
    with col2:
        nivel = st.selectbox("Nível", df['nivel'].unique())
    with col3:
        duracao_max = st.slider("Duração máxima (semanas)", 1, 20, 8)
    
    return categoria, nivel, duracao_max

def course_selector(df):
    """Adiciona um seletor de cursos com a opção 'Todos os cursos'"""
    cursos = ["Todos os cursos"] + sorted(df['titulo'].unique().tolist())
    return st.selectbox("Selecione um curso (ou deixe em 'Todos os cursos'):", cursos)

def search_bar():
    """Cria a barra de busca para cursos"""
    return st.text_input("Ou pesquise um curso pelo nome:")

def display_recommendations(df_rank):
    """Exibe as recomendações de cursos"""
    st.subheader("Cursos Encontrados")
    for _, row in df_rank.iterrows():
        st.markdown(f"""
        **{row['titulo']}**  
        Categoria: {row['categoria']}  
        Avaliação: {row['rating']}  
        Alunos: {row['alunos']}  
        Duração: {row['duracao_semanas']} semanas  
        Probabilidade de recomendação: {row['prob_recomendacao']:.2f}
        ---
        """)

def show_graphs(df):
    """Mostra gráficos de categorias e níveis"""
    st.subheader("Estatísticas dos Cursos")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("Categorias mais populares")
        chart_cat = (
            alt.Chart(df)
            .mark_bar(color="#4CAF50")
            .encode(
                x=alt.X('count()', title='Número de Cursos'),
                y=alt.Y('categoria', sort='-x', title='Categoria')
            )
        )
        st.altair_chart(chart_cat, use_container_width=True)

    with col2:
        st.markdown("Distribuição de Níveis")
        chart_nivel = (
            alt.Chart(df)
            .mark_bar(color="#2196F3")
            .encode(
                x=alt.X('count()', title='Número de Cursos'),
                y=alt.Y('nivel', sort='-x', title='Nível')
            )
        )
        st.altair_chart(chart_nivel, use_container_width=True)
