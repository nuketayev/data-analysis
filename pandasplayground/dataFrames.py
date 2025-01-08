import pandas as pd

data = pd.DataFrame({
    "Continent": ["America", "Asia", "Europe", "Asia", "America", "America", "Oceania"],
    "Population (millions)": [331, 1403, 84, 125, 214, 38, 26],
    "GDP (trillions USD)": [23.3, 3.73, 4.23, 4.94, 1.88, 2.2, 1.8],
    "Crime Rate (per 100k)": [398, 379, 62, 24, 392, 82, 43],
    "Number of Presidents": [46, 14, 12, 0, 38, 0, 0],
})

data.index = [
    'USA',
    'India',
    'Germany',
    'Japan',
    'Brazil',
    'Canada',
    'Australia'
]

print(data.shape)
print(data)
print()
print(data.iloc[4:,2:4]) # stop is exclusive
print(data.loc["Brazil":"Australia", 'GDP (trillions USD)':'Crime Rate (per 100k)']) # stop is inclusive