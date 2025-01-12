import sqlite3
import pandas as pd

conn = sqlite3.connect('pandasplayground/chinook.db')
 
cur = conn.cursor()

cur.execute('SELECT * FROM employees LIMIT 5;')

result = cur.fetchall()

df = pd.DataFrame(result)
print(df)

conn.close()
cur.close()
