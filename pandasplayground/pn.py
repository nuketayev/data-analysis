import pandas as pd

prices = pd.Series([149.5, 123.0,145,199])

prices.name = "Prices for the food"

prices.index = [
    'BigMac',
    'RegCont',
    'SpecCont',
    'IndChi'
]
prices.sort_index
print(prices)
print("BigMac('BigMac') and IndChi('IndChi'): ", prices[['BigMac', 'IndChi']])
print("BigMac(.iloc) and IndChi(.iloc): ", prices.iloc[[0, -1]])


print()

print(prices['BigMac':'SpecCont'])
print(prices.iloc[0:3]) # stop argument is inclusive, printing from 0 up to 3rd element

print("inflation",prices * 1.031)

print(prices < 150)

prices['BigMac'] = 145
print(prices)

prices[prices < 150] = 99

print(prices)