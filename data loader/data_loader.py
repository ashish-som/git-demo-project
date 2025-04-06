import pandas as pd

def load_data(path):
    if path.endswith(r'.xlsx|.xls'):
        return pd.read_excel(path)
    elif path.endswith('csv'):
        return pd.read_csv(path)
    else:
        return None