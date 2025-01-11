import pandas as pd
import matplotlib.pyplot as plt

houses = pd.read_csv('pandasplayground/house-prices.csv')

print(houses.head)
print(houses.shape)
print(houses.info())

print(houses.head(3))

print(houses.tail(3))

houses.plot()
plt.show()