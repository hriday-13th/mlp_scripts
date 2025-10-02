import pandas as pd

df = pd.read_csv('w1ga2.csv')

# print(df.shape)

# df_even_rows = df.iloc[::2]
# df_odd_rows = df.iloc[1::2]

# df_even_cols = df.iloc[:, ::2]
# df_odd_cols = df.iloc[1:, ::2]
# print(df_even_cols.iloc[255,3])
# print(df_odd_cols.iloc[100,5])

# print(df.info())
# print(df.head)

# c = df[df['Year'] > 2019]
# d = df[(df['num_rooms'] == 3) | (df['num_bathrooms'] == 3)]
# print(d.count())

# z = df[df['Date'].apply(lambda x: int(x.split("-")[1])) == 8]
# print(z.shape)

# z = df[
#     (df['Year'] == 2022) &
#     (df['Locality'] == 'Greenwich') &
#     (df['num_rooms'] == 3) &
#     (df['Face'].isin(['North', 'East']))
# ]
# print(z.shape)

avg_prices = df.groupby('Locality')['Sale Price'].mean()
highest_avg_locality = avg_prices.idxmax()
print(highest_avg_locality)