import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. High','Adj. Close','Adj. Low','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0

df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]
print(df.head())


