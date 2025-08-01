# Sistema Inteligente de Recomendação de Cursos Coursera

Este projeto implementa um **sistema inteligente de recomendação de cursos** usando **Random Forest** para identificar os cursos mais relevantes com base em características como **categoria, nível, duração, rating e número de alunos**.  

A aplicação possui uma **interface interativa em Streamlit**, permitindo ao usuário:
- **Pesquisar cursos pelo nome**
- **Selecionar um curso diretamente de uma lista**
- **Filtrar por categoria, nível e duração**
- **Receber recomendações personalizadas** (com cursos avaliados acima de 4.7)


## Tecnologias Utilizadas
- **Python 3.12+**
- **Pandas** – Manipulação de dados
- **Scikit-learn** – Modelo de Machine Learning (Random Forest)
- **Streamlit** – Interface web
- **Altair** – Gráficos interativos


## Estrutura do Projeto

```

/sistema_cursos
┣ data
┃ ┗ cursos_coursera.csv
┣ src
┃ ┣ app.py
┃ ┣ model.py
┃ ┗ interface.py
┣ LICENSE
┣ README.md
┗ requirements.txt

````


## Instalação e Execução

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/sistema-cursos.git
cd sistema-cursos
````

2. **Crie um ambiente virtual (opcional, mas recomendado)**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**

```bash
streamlit run src/app.py
```

## Funcionalidades

- **Busca por nome do curso**
- **Seleção de curso (dropdown)**
- **Filtros (categoria, nível, duração)**
- **Gráficos interativos mostrando categorias e níveis mais populares**
- **Recomendações com cursos de rating > 4.7**


## Dados

O dataset `cursos_coursera.csv` contém informações de cursos fictícios do Coursera nas áreas de:

- Programação
- Ciência de Dados
- Machine Learning
- Deep Learning

**Colunas do dataset:**

|Colunas|Conteúdo|
|---|---|
|`titulo`|Nome do curso|
|`categoria`|Área do curso|
|`nivel`|Básico, Intermediário, Avançado|
|`duracao_semanas`|Quantidade de semanas do curso|
|`rating`|Avaliação média do curso|
|`alunos`|Número de alunos inscritos|
|`recomendado`|Variável alvo usada para treinar o modelo (1 = recomendado, 0 = não recomendado)|


## Próximos Passos

- Melhorar o modelo (testar outros algoritmos além de Random Forest)
- Implementar recomendação personalizada com base em histórico do usuário
- Adicionar suporte para múltiplos datasets


## Licença

Este projeto está sob a licença GNU – veja o arquivo LICENSE para mais detalhes.

