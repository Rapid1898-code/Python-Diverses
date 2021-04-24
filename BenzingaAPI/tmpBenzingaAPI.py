# Doku: https://docs.benzinga.io/benzinga-python/index.html

from benzinga import news_data
api_key = "510b80dd35734372b807c4ea88773e3e"
paper = news_data.News(api_key)
stories = paper.news(company_tickers="AAPL", pagesize=30, date_from="2021-04-19", date_to="2021-04-23")

for idx, elem in enumerate(stories):
    print(f"\n\nStory {idx}:")
    for key, val in elem.items ():
        print (f"{key} => {val} {type(val)}")

print(len(stories))