import pandas as pd

data = pd.DataFrame({
    "Continent": ["America", "Asia", "Europe", "Asia", "America", "America", "Oceania"],
    "Population (millions)": [331, 1403, 84, 125, 214, 38, 26],
    "GDP (trillions USD)": [23.3, 3.73, 4.23, 4.94, 1.88, 2.2, 1.8],
    "Crime Rate (per 100k)": [398, 379, 62, 24, 392, 82, 43],
    "Number of Presidents": [46, 14, 12, 0, 38, 0, 0],
}, index=[
    'USA',
    'India',
    'Germany',
    'Japan',
    'Brazil',
    'Canada',
    'Australia'
])

langs = pd.Series(['English', 'Hindi', 'German', 'Japanese', 'Portuguese', 'English', 'English'], index=[
    'USA',
    'India',
    'Germany',
    'Japan',
    'Brazil',
    'Canada',
    'Australia'
])

# print(data['Population (millions)'] > 100)
# print(data.loc[data['Population (millions)'] > 100, 'Number of Presidents'])
print(data.loc[data['Population (millions)'] > 100, ['Number of Presidents', 'Crime Rate (per 100k)']])


crisis = pd.Series([0.8, 1.18], index=['GDP (trillions USD)', 'Crime Rate (per 100k)'])
print(crisis)

data = data[['GDP (trillions USD)', 'Crime Rate (per 100k)']] * crisis
print("Data after crisis:")
print(data[['GDP (trillions USD)']])

print(data.drop('USA'))

data['Language'] = langs

print(data)

data = data.rename(
    columns={
        'GDP (trillions USD)':"GDP"
    }
)
print(data)