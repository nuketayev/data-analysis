import pandas as pd

html_url = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"

nba_tables = pd.read_html(html_url)

len = len(nba_tables)
print(len)

nba = nba_tables[0]
print(nba.head())