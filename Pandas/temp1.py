import pandas as pd

df = pd.read_excel ("C:\TEMP\COVID-19-geographic-disbtribution-worldwide (2).xlsx")
pd.set_option ("display.max_columns", 100)
pd.set_option ("display.max_rows", 100)

# Umbenennen der Titelzeilen
df.rename(columns={"countriesAndTerritories":"land","continentExp":"continent",
                   "dateRep":"date","popData2018":"einwohner"}, inplace=True)

# Einschränkung auf die zu verwendenden Spalten
#df = df[["date","cases","deaths","land","einwohner"]]

print(df)

