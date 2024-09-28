import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

class DataQuality:
    def __init__(self, directory:str) -> None:
        self.df = pd.read_csv(directory, encoding="latin-1")
        self.df_cat = self.df.select_dtypes(exclude=np.number)
        self.df_num = self.df.select_dtypes(include=np.number)

    def firts_rows(self, n=5):
        print("DataFrame Completo:")
        head_df = self.df.head(n)
        print(tabulate(head_df, headers="keys", showindex="always", tablefmt="fancy_grid"))

        print("\nDataFrame Categórico:")
        categ_df = self.df_cat.head(n)
        print(tabulate(categ_df, headers="keys", showindex="always", tablefmt="fancy_grid"))

        print("\nDataFrame Numérico:")
        num_df = self.df_num.head(n)
        print(tabulate(num_df, headers="keys", showindex="always", tablefmt="fancy_grid"))
    
    def last_rows(self, n=5):
        print("\nDataFrame Completo:")
        tail_df = self.df.tail(n)
        print(tabulate(tail_df, headers="keys", showindex="always", tablefmt="fancy_grid"))

        print("\nDataFrame Categórico:")
        categ_df = self.df_cat.tail(n)
        print(tabulate(categ_df, headers="keys", showindex="always", tablefmt="fancy_grid"))

        print("\nDataFrame Numérico:")
        num_df = self.df_num.tail(n)
        print(tabulate(num_df, headers="keys", showindex="always", tablefmt="fancy_grid"))

    def count_nulls(self):
        print("\nQuantidade de Nulos:")
        df_nulos= self.df.isnull().sum().reset_index()
        df_nulos.columns = ["Coluna", "Quantidade"]
        print(tabulate(df_nulos, headers="keys", showindex="always", tablefmt="fancy_grid"))

    def count_unique(self):
        print("\nQuantidade de Dados Únicos:")
        df_unicos= self.df.nunique().reset_index()
        df_unicos.columns = ["Coluna", "Quantidade"]
        print(tabulate(df_unicos, headers="keys", showindex="always", tablefmt="fancy_grid"))

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
            self.df_num[col].plot(subplots=True, kind='bar', figsize=(25,10), fontsize=5)
            plt.show()

    def categorical_analyzes(self):
        for col in self.df_cat:
            print(f"\n{col} - Coluna Categórica")
            df_aux = self.df_cat[col].value_counts().reset_index()
            print(tabulate(df_aux, headers="keys", tablefmt="fancy_grid"))