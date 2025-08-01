import streamlit as st
from model import CourseRecommender
from interface import main_filters, course_selector, display_recommendations, show_graphs, search_bar

# Configuração inicial
st.set_page_config(page_title="Recomendador de Cursos Coursera", layout="wide")
st.title("Recomendador de Cursos Coursera")
st.markdown("Este sistema usa Machine Learning (Random Forest) para sugerir cursos relevantes com base em suas preferências.")

# Carregar modelo
recommender = CourseRecommender("data/cursos_coursera.csv")

# Mostrar gráficos informativos
show_graphs(recommender.df)

# Filtros principais
categoria, nivel, duracao_max = main_filters(recommender.df)

# Novo seletor de curso
curso_selecionado = course_selector(recommender.df)

# Campo de busca
busca = search_bar()

# Botão para disparar pesquisa
if st.button("Pesquisar"):
    if curso_selecionado != "Todos os cursos":
        # Se o usuário escolher um curso específico, mostra apenas ele
        st.subheader(f"Curso selecionado: {curso_selecionado}")
        resultado = recommender.df[recommender.df['titulo'] == curso_selecionado]

        for _, row in resultado.iterrows():
            st.markdown(f"""
            **{row['titulo']}**  
            Categoria: {row['categoria']}  
            Avaliação: {row['rating']}  
            Alunos: {row['alunos']}  
            Duração: {row['duracao_semanas']} semanas  
            """)
    
    elif busca:
        # Caso o usuário digite algo, busca pelo nome
        st.subheader(f"Resultados para: '{busca}'")
        resultados = recommender.df[recommender.df['titulo'].str.contains(busca, case=False, na=False)]
        
        if not resultados.empty:
            for _, row in resultados.iterrows():
                st.markdown(f"""
                **{row['titulo']}**  
                Categoria: {row['categoria']}  
                Avaliação: {row['rating']}  
                Alunos: {row['alunos']}  
                Duração: {row['duracao_semanas']} semanas  
                """)
        else:
            st.warning("Nenhum curso encontrado com esse nome.")
    
    else:
        # Caso o usuário não selecione um curso nem digite nada -> recomenda cursos
        df_rank = recommender.recommend(categoria, nivel, duracao_max)

        # Filtrar apenas cursos com rating > 4.7
        df_rank = df_rank[df_rank['rating'] > 4.7]

        if not df_rank.empty:
            display_recommendations(df_rank)
        else:
            st.warning("Nenhum curso com avaliação acima de 4.7 foi encontrado para os filtros selecionados.")
else:
    st.info("Use os filtros acima, escolha um curso ou digite o nome e clique em 'Pesquisar'.")
