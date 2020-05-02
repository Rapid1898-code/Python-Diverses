import pandas as pd
df = pd.read_excel ("C:\TEMP\COVID-19-geographic-disbtribution-worldwide (2).xlsx")
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
countries_df = df.groupby("land").sum().sort_values(by="cases",ascending=False).head(50)
countries = []
for index,row in countries_df.iterrows(): countries.append(index)
#countries = ["Austria","Germany","Switzerland"]
#countries = ["Austria"]

# Hauptverarbeitung
df_final_cases = df_final_deaths = df_final_inh_case =  df_final_inh_death = pd.DataFrame()
for country in countries:
    print(country)
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

    df_temp_cases = df_temp[["date","land","sum_cases"]]
    df_temp_cases = df_temp_cases.pivot(index="land", columns="date", values="sum_cases")
    df_final_cases = df_final_cases.append(df_temp_cases, ignore_index=False)

    df_temp_deaths = df_temp[["date","land","sum_deaths"]]
    df_temp_deaths = df_temp_deaths.pivot(index="land", columns="date", values="sum_deaths")
    df_final_deaths = df_final_deaths.append(df_temp_deaths, ignore_index=False)

    df_temp_inh_case = df_temp[["date","land","inh_case"]]
    df_temp_inh_case = df_temp_inh_case.pivot(index="land", columns="date", values="inh_case")
    df_final_inh_case = df_final_inh_case.append(df_temp_inh_case, ignore_index=False)

    df_temp_inh_death = df_temp[["date","land","inh_death"]]
    df_temp_inh_death = df_temp_inh_death.pivot(index="land", columns="date", values="inh_death")
    df_final_inh_death = df_final_inh_death.append(df_temp_inh_death, ignore_index=False)

df_final_cases = df_final_cases.sort_index(axis=1, ascending=True)
df_final_deaths = df_final_deaths.sort_index(axis=1, ascending=True)
df_final_inh_case = df_final_inh_case.sort_index(axis=1, ascending=True)
df_final_inh_death = df_final_inh_death.sort_index(axis=1, ascending=True)

date = str(df_final_cases.columns[len(df_final_cases.columns)-1].date()).replace("-","_")

writer = pd.ExcelWriter("covid_statistic_"+date+".xlsx", engine = "openpyxl", datetime_format="DD.MM.YYYY")
df_final_cases.to_excel(writer, sheet_name="cases")
df_final_deaths.to_excel(writer, sheet_name="deaths")
df_final_inh_case.to_excel(writer, sheet_name="inh_per_case")
df_final_inh_death.to_excel(writer, sheet_name="inh_per_death")

while True:
    try:
        writer.save ()
        writer.close ()
        break
    except Exception as e:
        print ("Error: ", e)
        input ("Datei kann nicht geöffnet werden - bitte schließen und <Enter> drücken!")

