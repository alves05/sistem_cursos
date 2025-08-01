import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class CourseRecommender:
    def __init__(self, csv_path="data/cursos_coursera.csv"):
        self.df = pd.read_csv(csv_path)
        self._encode_features()
        self._train_model()

    def _encode_features(self):
        """Codifica variáveis categóricas"""
        self.le_categoria = LabelEncoder()
        self.le_nivel = LabelEncoder()

        self.df['categoria_encoded'] = self.le_categoria.fit_transform(self.df['categoria'])
        self.df['nivel_encoded'] = self.le_nivel.fit_transform(self.df['nivel'])

        self.X = self.df[['categoria_encoded', 'avaliacoes', 'rating', 'nivel_encoded', 'alunos', 'duracao_semanas']]
        self.y = self.df['recomendado']

    def _train_model(self):
        """Treina o modelo Random Forest"""
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

    def recommend(self, categoria, nivel, duracao_max):
        """Gera recomendações de cursos"""
        categoria_enc = self.le_categoria.transform([categoria])[0]
        nivel_enc = self.le_nivel.transform([nivel])[0]

        df_filtrado = self.df[self.df['duracao_semanas'] <= duracao_max]
        df_filtrado['prob_recomendacao'] = self.model.predict_proba(
            df_filtrado[['categoria_encoded', 'avaliacoes', 'rating', 'nivel_encoded', 'alunos', 'duracao_semanas']]
        )[:, 1]

        return df_filtrado.sort_values('prob_recomendacao', ascending=False).head(5)
