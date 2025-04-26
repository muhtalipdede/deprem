import pandas as pd

def merge_data(df_population, df_coordinates):
    df = pd.merge(df_population, df_coordinates, on="city", how="inner", validate="many_to_many")
    return df