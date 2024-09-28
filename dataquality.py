import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

class DataQuality:
    def __init__(self, directory:str) -> None:
        self.df = pd.read_csv(directory, encoding="latin-1")
        self.df_cat = self.df.select_dtypes(exclude=np.number)
        self.df_num = self.df.select_dtypes(include=np.number)

    def firts_rows(self, n=5):
        print(f"\n{n} primeiras linhas:")
        head_df = self.df.head(n).reset_index()
        print(tabulate(head_df, headers="keys", tablefmt="fancy_grid"))
    
    def last_rows(self, n=5):
        print(f"\n{n} últimas linhas:")
        tail_df = self.df.tail(n)
        print(tabulate(tail_df, headers="keys", tablefmt="fancy_grid"))

    def sample_rows(self, n=5):
        print(f"\nAmostra de {n} linhas:")
        sample_rows = self.df.sample(n)
        print(tabulate(sample_rows, headers="keys", tablefmt="fancy_grid"))

    def count_nulls(self):
        print("\nQuantidade de dados nulos:")
        df_nulos= self.df.isnull().sum().reset_index()
        df_nulos.columns = ["Coluna", "Quantidade"]
        print(f"Quantidade total de dados nulos: {df_nulos["Quantidade"].sum()}")
        print(tabulate(df_nulos[df_nulos["Quantidade"] > 0], headers="keys", tablefmt="fancy_grid"))

    def count_unique(self):
        print("\nQuantidade de dados únicos:")
        df_unicos= self.df.nunique().reset_index()
        df_unicos.columns = ["Coluna", "Quantidade"]
        print(f"Quantidade total de dados únicos: {df_unicos["Quantidade"].sum()}")
        print(tabulate(df_unicos, headers="keys", tablefmt="fancy_grid"))

    def most_commom(self):
        print("\nDados mais comuns:")
        for col in self.df_cat.columns:
            df_aux = self.df_cat[col].mode()
            print(f"{col}: {df_aux[0]}")

    def numerical_analyzes(self):
        for col in self.df_num:
            print(f"\n{col} - Coluna Númerica")
            df_num_descbrie = self.df_num[col].describe().round(2).reset_index()
            print(tabulate(df_num_descbrie, headers="keys", tablefmt="fancy_grid"))
            plt.hist(self.df_num[col])
            plt.show()

    def categorical_analyzes(self):
        for col in self.df_cat:
            print(f"\n{col} - Coluna Categórica")
            df_aux = self.df_cat[col].value_counts().reset_index()
            print(tabulate(df_aux, headers="keys", tablefmt="fancy_grid"))