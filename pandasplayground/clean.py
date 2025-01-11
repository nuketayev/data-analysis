import numpy as np
import pandas as pd

print("(passing null) Is null?:",pd.isnull(np.nan))
print("(passing null) Is not null?:",pd.notnull(np.nan))

ser = pd.Series([1,2,np.nan])
print(ser)
print()
print(pd.isnull(ser))
print()
print("How many null values in the series:",pd.isnull(ser).sum())
print()
print(ser[pd.notnull(ser)])
print()
print(ser.dropna())

print(ser)

# ser = ser.fillna(ser.mean())
ser = ser.fillna(method='ffill')

print(ser)
