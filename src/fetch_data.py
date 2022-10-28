import pandas as pd

def get_from_csv(path):
    df = pd.read_csv(path, sep=",")
    return df

# ToDo: integration with SchedGo API
def fetch_SchedGo():
    pass

