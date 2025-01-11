import pandas as pd

ambassadors = pd.Series(['France','United Kingdom',
                         'United Kingdom','Italy',
                         'Germany','Germany','Germany'],
                         index=['Gérard Araud',
                                'Kim Darroch',
                                'Peter Westmacott',
                                'Armando Varricchio',
                                'Peter Wittig',
                                'Peter Ammon',
                                'Klaus Scharioth'])

# print(ambassadors)
# print(ambassadors.duplicated())
# print()
# print(ambassadors.duplicated(keep='last'))
# print()
# print(ambassadors.drop_duplicates(keep='last'))

df = pd.DataFrame({
    'Data': [
        '1987_M_US_1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_Italy_1',
        '1985_F_Ireland_1',
        '1992_M_US_3'
    ]
})

print(df)
print()
df = df['Data'].str.split('_',expand=True)
df.columns = ['Year', 'Sex', 'Country', 'No Children']
print(df)