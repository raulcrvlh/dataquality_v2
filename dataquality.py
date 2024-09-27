import pandas as pd
import numpy as np
from tabulate import tabulate

class DataQuality:
    def __init__(self, directory:str) -> None:
        self.df = pd.read_csv(directory, encoding="latin-1")
        self.df_cat = self.df.select_dtypes(exclude=np.number)
        self.df_num = self.df.select_dtypes(include=np.number)

    def header(self, n=5):
        print("DataFrame Completo:")
        head_df = self.df.head(n)
        print(tabulate(head_df, headers="keys", showindex="always", tablefmt="fancy_grid"))

        print("\nDataFrame Categórico:")
        categ_df = self.df_cat.head(n)
        print(tabulate(categ_df, headers="keys", showindex="always", tablefmt="fancy_grid"))

        print("\nDataFrame Numérico:")
        num_df = self.df_num.head(n)
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
