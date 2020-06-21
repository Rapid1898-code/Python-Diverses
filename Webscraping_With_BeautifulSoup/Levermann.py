import YahooCrawler

#stat1,stat2 = YahooCrawler.read_yahoo_statistics("AAPL")
#roe = float(stat1["Return on Equity (ttm)"].replace("%",""))
#print(roe)

insstat = YahooCrawler.read_yahoo_income_statement("AAPL")
ebit = float(insstat["EBIT"][0].replace(",",""))
revenue = float(insstat["Total Revenue"][0].replace(",",""))
ebit_marge = round(ebit / revenue * 100,2)
eps_list = insstat["Basic EPS"]
print(ebit_marge)
print(insstat["Breakdown"])
print(eps_list)

# bal_sheet = YahooCrawler.read_yahoo_balance_sheet("AAPL")
# equity = float(bal_sheet["Stockholders' Equity"][0].replace(",",""))
# total_assets = float(bal_sheet["Total Assets"][0].replace(",",""))
# eq_ratio = round(equity / total_assets * 100,2)
# print(eq_ratio)

# summary = YahooCrawler.read_yahoo_summary("AAPL")
# pe_ratio = float(summary["pe_ratio"])
# print(pe_ratio)

