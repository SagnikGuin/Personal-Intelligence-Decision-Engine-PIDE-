import pandas as pd
def get_total_hours(df):
    if df.empty:
        return 0
    total_hours = df['hours'].sum()
    return total_hours
def get_average_hours(df):
    if df.empty:
        return 0
    average_hours = df['hours'].mean()
    return average_hours
def get_hours_by_activity(df):
    if df.empty:
        return {}
    activity_series = df['activity'].str.lower()
    grouped = df.groupby(activity_series)['hours'].sum()
    return grouped.to_dict()
def get_productivity_score(df):
    if df.empty:
        return 0
    productivity = (df['hours'] * df['focus'] * df['energy']).sum()
    return productivity