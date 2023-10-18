import pandas as pd

def read_csv(path):
    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError:
        print(f'The file {path} does not exist.')
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f'The file {path} is empty.')
        return pd.DataFrame()
    except Exception as e:
        print(f'Error reading the file {path}: {e}')
        return pd.DataFrame()
