### 1 - Gettings started with Data Analysis
import pandas as pd

df = pd.read_excel ("C:\TEMP\COVID-19-geographic-disbtribution-worldwide (1).xlsx")
#print(df)   # Ausgabe Dataframe
# print(df.shape)     # Ausgabe Zeilenanzahl und Spalten
# print(df.info())    # zusätzliche Infos zum Dataframe (Datentypen, Anzahl, usw.)
pd.set_option ("display.max_columns", 100)  # dadurch werden alle Spalten ausgegeben
pd.set_option ("display.max_rows", 100)  # dadurch werden alle Zeilen ausgegeben
# print(df.head())   # ersten 5 Zeilen
# print(df.head(1000))    # ersten 1000 Zeilen werden ausgegeben
# print(df.tail())   # letzten 5 Zeilen
# print(df.tail(1000))    # letzten 1000 Zeilen


### 2 - DataFrme
# print(df["day"])
# print(df.day)
# print(type(df))
# print(type(df.day))
# print(df[['day','year']])
#print(df.columns)
# print(df.countriesAndTerritories.value_counts())


### 3 - Row Output
# print(df)
#print (df.columns)
# print(df.iloc[[0,1,2],6])
#print(df.loc[0:10,"month":"cases"])
#print(df)   # Ausgabe Dataframe
#df.set_index("cases", inplace=True)
#print(df.sort_index(ascending=False))

countries =  ["Austria","Germany","Switzerland"]
filt = (df["countriesAndTerritories"] == "Austria")
#print(df[filt])
print(df.loc[filt,["cases","countriesAndTerritories"]])


