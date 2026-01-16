from utils import helpers as hp
import os
import csv
import pandas as pd
def ensure_csv(filepath):
    if not os.path.isfile(filepath):
        with open(filepath, mode = 'w', newline='') as file:
            headers = ['name', 'age', 'activity', 'hours', 'date', 'energy', 'focus']
            writer = csv.writer(file)
            writer.writerow(headers)
def append_csv(filepath, entry):
    row = [entry["name"], entry["age"], entry["activity"], entry["hours"], entry["date"], entry["energy"], entry["focus"]]
    try:
        with open(filepath, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
    except Exception as e:
        hp.log_error(str(e))
        return False
    else:
        return True
def read_csv_safe(filepath):
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        hp.log_error(str(e))
        df = pd.DataFrame()
    return df
