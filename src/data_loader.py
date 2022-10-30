import pandas as pd
import json

def get_from_csv(path):
    df = pd.read_csv(path, sep=",")
    return df

# ToDo: integration with SchedGo API
def fetch_SchedGo():
    pass

def get_from_json(j_str):
    all_courses = json.loads(j_str)
    df = pd.DataFrame(all_courses)
    return df

