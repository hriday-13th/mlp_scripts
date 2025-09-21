# Pandas is a column-oriented API for data analysis
import pandas as pd
# print(pd.__version__)

# Pandas work with 2 data structures mainly
# 1. DataFrames: Kind of like a RDBMS table, with rows and columns
# 2. Series: A single column


# Load a dummy database
from sklearn.datasets import load_diabetes
diabetes = load_diabetes(as_frame=True)
df = diabetes['data']
# print(type(diabetes['data']))

# Creating dataframes
# cities = pd.Series(['Mumbai', 'Chennai', 'Bengaluru'])
# population = pd.Series(['100', '10202', '88'])

# city_info_df = pd.DataFrame({'Cities': cities, "Population": population})

# Exploring the diabetes df
