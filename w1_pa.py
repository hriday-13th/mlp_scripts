import pandas as pd
from collections import defaultdict

df = pd.read_csv("w1pa.csv")

print(df.shape)

print(df.describe())

flights = df['Month'].value_counts().sort_index()
max_flight = flights.max()
busy_month = flights[flights == max_flight].index.to_list()

print(busy_month)


df_weekend = df[df['WeekDay'].isin(['Saturday', 'Sunday'])]
df_weekday = df[~df['WeekDay'].isin(['Saturday', 'Sunday'])]
print(df_weekend['Price'].mean())
print(df_weekday['Price'].mean())

df.loc[df['Additional_Info'] == 'No Info', 'Additional_Info'] = 'No info'
df_filtered = df[(df['Airline'] == 'IndiGo') & (df['Additional_Info'] == 'No info')]
print(df_filtered.count())

print(df[['Dep_Time', 'Arrival_Time']].head())
print(type(df['Airline']))

def convert_to_sec(t):
    h, m = 0, 0
    parts = t.split()
    for part in parts:
        if 'h' in part:
            h = int(part.replace('h', ''))
        elif 'm' in part:
            m = int(part.replace('m', ''))
    return h * 3600 + m * 60

df['secs'] = df['Duration'].apply(convert_to_sec)

print(df['secs'].mean())

def classify_hour(time):
    if 5 <= time < 12:
        return "Morning"
    elif 12 <= time < 17:
        return "Afternoon"
    elif 17 <= time < 20:
        return "Evening"
    else:
        return "Night"
    
df['Dephr'] = pd.to_datetime(df['Dep_Time'], format='%H:%M').dt.hour
df['Arrhr'] = pd.to_datetime(df['Arrival_Time'].str.split().str[0], format="%H:%M").dt.hour

df['Dephrn'] = df['Dephr'].apply(classify_hour)
df['Arrhrn'] = df['Arrhr'].apply(classify_hour)

c = df[(df['Dephrn'] == 'Morning') & (df['Arrhrn'] == 'Evening')]
print(c.count())

def classify_weekday(w):
    if w in ['Saturday', 'Sunday']:
        return 1
    else:
        return 0
    
df['eee'] = df['WeekDay'].apply(classify_weekday)
print(df['eee'].value_counts())