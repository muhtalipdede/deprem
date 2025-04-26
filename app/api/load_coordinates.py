import pandas as pd

def load_coordinates():
    csv_data = pd.read_csv("datas/coordinates.csv")
    csv_data = csv_data.dropna()
    return csv_data