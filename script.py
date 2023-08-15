import pandas as pd


def get_number_passengers(df: pd.DataFrame, sex: str, p_class: int):
    return df[(df['Sex'] == sex) & (df['Pclass'] == p_class)].size


def is_passenger_id_even(passenger_id: int):
    return passenger_id % 2 == 0


def get_passenger_surname(name: str):
    return name.split(',')[0]
def get_passenger_first_name(name: str):
    return name.split('.')[1]
