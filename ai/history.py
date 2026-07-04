import pandas as pd
import os
from datetime import datetime

FILE = "ai/history.csv"

def save_history(car, person, bike, truck, traffic, safety, risk):

    row = {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Cars": car,
        "People": person,
        "Bikes": bike,
        "Trucks": truck,
        "Traffic": traffic,
        "Safety": safety,
        "Risk": risk
    }

    if os.path.exists(FILE):
        df = pd.read_csv(FILE)
    else:
        df = pd.DataFrame(columns=row.keys())

    df.loc[len(df)] = row
    df.to_csv(FILE, index=False)


def load_history():

    if os.path.exists(FILE):
        return pd.read_csv(FILE)

    return pd.DataFrame(columns=[
        "Time","Cars","People","Bikes","Trucks",
        "Traffic","Safety","Risk"
    ])