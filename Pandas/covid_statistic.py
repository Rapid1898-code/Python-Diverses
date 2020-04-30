import pandas as pd
df = pd.read_excel ("C:\TEMP\COVID-19-geographic-disbtribution-worldwide (1).xlsx")
pd.set_option ("display.max_columns", 100)
pd.set_option ("display.max_rows", 100)

# Umbenennen der Titelzeilen
df.rename(columns={"countriesAndTerritories":"land","continentExp":"continent",
                   "dateRep":"date","popData2018":"einwohner"}, inplace=True)

# Einschränkung auf die zu verwendenden Spalten
df = df[["date","cases","deaths","land","einwohner"]]

# Neue Spalten anlagen
df["sum_cases"] = df["sum_deaths"] = df["inh_case"] = df["inh_death"] = 0

# read 25 top countries with most covid-cases and store in list
countries_df = df.groupby("land").sum().sort_values(by="cases",ascending=False).head(25)
countries = []
for index,row in countries_df.iterrows(): countries.append(index)
countries = ["Austria"]

# Hauptverarbeitung
for country in countries:
    df_temp = df[df["land"].isin([country])]
    for i,i_cont in df_temp.iterrows():
        sum_cases = sum_deaths = 0
        for j,j_cont in df_temp.iterrows():
            if j_cont[0] < i_cont[0]:
                sum_cases += j_cont[1]
                sum_deaths += j_cont[2]
        df_temp._set_value(i,"sum_cases",sum_cases)
        df_temp._set_value(i,"sum_deaths",sum_deaths)
        if sum_cases != 0: df_temp._set_value (i,"inh_case", i_cont[4] / sum_cases)
        else: df_temp._set_value (i,"inh_case",1,0)
        if sum_deaths != 0: df_temp._set_value (i,"inh_death", i_cont[4] / sum_deaths)
        else: df_temp._set_value (i,"inh_death",1,0)

print (df_temp)







