import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from IPython.display import display_markdown

class DataQuality:
    def __init__(self, directory:str) -> None:
        self.df = pd.read_csv(directory, encoding="latin-1")
        self.df_cat = self.df.select_dtypes(exclude=np.number)
        self.df_num = self.df.select_dtypes(include=np.number)

    def quick_info(self):
        display_markdown(f'''### Informações Gerais:''', raw=True)
        display_markdown(f'''- **Linhas:** {len(self.df)}''', raw=True)
        display_markdown(f'''- **Colunas:** {len(self.df.columns)}''',raw=True)

        display_markdown('''#### Colunas Categóricas:''', raw=True)
        for col_categ in self.df_cat.columns:
            display_markdown(f'''- {col_categ}''', raw=True)

        display_markdown('''#### Colunas Numéricas:''', raw=True)
        for col_num in self.df_num.columns:
            display_markdown(f'''- {col_num}''', raw=True)

    def firts_rows(self, n=5):
        display_markdown(f'''### Primeiras {n} linhas:''', raw=True)
        head_df = self.df.head(n).reset_index()
        print(tabulate(head_df, headers="keys", tablefmt="fancy_grid"))
    
    def last_rows(self, n=5):
        display_markdown(f'''### Últimas {n} linhas:''', raw=True)
        tail_df = self.df.tail(n)
        print(tabulate(tail_df, headers="keys", tablefmt="fancy_grid"))

    def sample_rows(self, n=5):
        display_markdown(f'''### Amostra de {n} linhas:''', raw=True)
        sample_df = self.df.sample(n, random_state=np.random.seed(42))
        print(tabulate(sample_rows, headers="keys", tablefmt="fancy_grid"))

    def count_nulls(self):
        display_markdown('''### Dados nulos''', raw=True)
        nulls_df= self.df.isnull().sum().reset_index()
        nulls_df.columns = ["Coluna", "Quantidade"]
        total = nulls_df["Quantidade"].sum()
        display_markdown(f'''#### Quantidade total de dados nulos: {total}''', raw=True)

        nulls_df["Frequência (%)"] = (nulls_df["Quantidade"] / total).mul(100).round(2)
        if nulls_df.empty:
            display_markdown(f'''- Não existem dados nulos no DataFrame.''', raw=True)
        else:
            print(tabulate(nulls_df[nulls_df["Quantidade"] > 0], headers="keys", tablefmt="fancy_grid"))

    def count_unique(self):
        display_markdown('''### Dados únicos''', raw=True)
        unique_df= self.df.nunique().reset_index()
        unique_df.columns = ["Coluna", "Quantidade"]
        total = unique_df["Quantidade"].sum()
        display_markdown(f'''#### Quantidade total de dados únicos: {total}''', raw=True)

        unique_df["Frequência (%)"] = (unique_df["Quantidade"] / total).mul(100).round(2)
        if unique_df.empty:
            display_markdown(f'''- Não existem dados únicos no DataFrame.''', raw=True)
        else:
            print(tabulate(unique_df[unique_df["Quantidade"] > 0], headers="keys", tablefmt="fancy_grid"))

    def most_commom(self):
        display_markdown('''### Dados mais comuns por coluna''', raw=True)

        for col in self.df_cat.columns:
            df_aux = self.df_cat[col].mode()
            display_markdown(f''' - **{col}:** {df_aux[0]}''', raw=True)

    def numerical_analyzes(self):
        for col in self.df_num:
            display_markdown(f'''### {col} - Coluna Numérica''', raw=True)

            df_num_descbrie = self.df_num[col].describe().round(2).reset_index()
            print(tabulate(df_num_descbrie, headers="keys", tablefmt="fancy_grid"))
            plt.hist(self.df_num[col])
            plt.show()

    def categorical_analyzes(self):
        for col in self.df_cat:
            display_markdown(f'''### {col} - Coluna Categórica''', raw=True)

            df_aux = self.df_cat[col].value_counts().reset_index()
            df_aux.columns = ["Coluna", "Quantidade"]
            print(tabulate(df_aux, headers="keys", tablefmt="fancy_grid"))

    def report(self):
        display_markdown('''# **Relatório de Análises Genéricas**''', raw=True)
        self.quick_info()

        self.firts_rows()
        self.last_rows()
        self.sample_rows()

        self.count_nulls()
        self.count_unique()
        self.most_commom()

        self.numerical_analyzes()
        self.categorical_analyzes()