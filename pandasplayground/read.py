import pandas as pd

# with open('pandasplayground/house-prices.csv', 'r') as fp:
#     print("Here is fp:",fp)

csv_url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"

df = pd.read_csv(csv_url)

print(df.head())