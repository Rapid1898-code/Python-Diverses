import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv ("adult_data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = None
    race_grp = df.groupby("race")
    race_count = race_grp["race"].count().sort_values(ascending=False)

    # What is the average age of men?
    filt9 = (df["sex"] == "Male")
    average_age_men = round(df[filt9]["age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df["education"].value_counts(normalize=True).loc["Bachelors"]*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    filt1 = df["education"].isin (["Bachelors", "Masters", "Doctorate"])
    filt2 = (df["education"].isin (["Bachelors", "Masters", "Doctorate"])) & (df["salary"] == ">50K")
    higher_education = df[filt1]["education"].count()
    higher_education_grfifthy = df[filt2]["education"].count()

    filt3 = ~df["education"].isin (["Bachelors", "Masters", "Doctorate"])
    filt4 = (~df["education"].isin (["Bachelors", "Masters", "Doctorate"])) & (df["salary"] == ">50K")
    lower_education = df[filt3]["education"].count()
    lower_education_grfifthy = df[filt4]["education"].count()

    # percentage with salary >50K
    higher_education_rich = round(higher_education_grfifthy / higher_education * 100,1)
    lower_education_rich = round (lower_education_grfifthy / lower_education * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    filt5 = df["hours-per-week"] == 1
    filt6 = (df["hours-per-week"] == 1) & (df["salary"] == ">50K")
    num_min_workers = df[filt5]["education"].count()
    rich_percentage = round(df[filt6]["education"].count() / num_min_workers * 100,2)

    # What country has the highest percentage of people that earn >50K?
    filt7 = df["salary"] == ">50K"
    s_count = df.groupby ("native-country")["native-country"].count()
    s_grfifthy = df[filt7].groupby ("native-country")["native-country"].count()
    s_perc = s_grfifthy / s_count * 100
    s_perc = s_perc.sort_values(ascending=False)
    highest_earning_country = s_perc.index[0]
    highest_earning_country_percentage = round(s_perc.iloc[0],1)

    # Identify the most popular occupation for those who earn >50K in India.
    filt8 = (df["native-country"] == "India") & (df["salary"] == ">50K")
    s = df[filt8].groupby("occupation")["occupation"].count()
    s = s.sort_values(ascending=False)
    top_IN_occupation = s.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
