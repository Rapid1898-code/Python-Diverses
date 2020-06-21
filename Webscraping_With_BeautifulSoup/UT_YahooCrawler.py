import unittest
from YahooCrawler import read_yahoo_summary
from YahooCrawler import read_yahoo_profile
from YahooCrawler import read_yahoo_statistics
from YahooCrawler import read_yahoo_income_statement
from YahooCrawler import read_yahoo_balance_sheet
from YahooCrawler import read_yahoo_cashflow
from YahooCrawler import read_yahoo_analysis

class TestYahooCrawler(unittest.TestCase):
    # def test_summary_AAPL(self):
    #     erg = read_yahoo_summary("AAPL")
    #     self.assertEqual(erg["symbol"],"AAPL")
    #     self.assertEqual(erg["name"], "Apple Inc.")
    #     self.assertTrue(isinstance(erg["price"],float))
    #
    # def test_summary_AMZN(self):
    #     erg = read_yahoo_summary("AMZN")
    #     self.assertEqual(erg["symbol"],"AMZN")
    #     self.assertEqual(erg["name"], "Amazon.com, Inc.")
    #     self.assertTrue(isinstance(erg["price"],float))
    #
    # def test_summary_CAT(self):
    #     erg = read_yahoo_summary("CAT")
    #     self.assertEqual(erg["symbol"],"CAT")
    #     self.assertEqual(erg["name"], "Caterpillar Inc.")
    #     self.assertTrue(isinstance(erg["price"],float))
    #
    # def test_profile_AAPL(self):
    #     erg = read_yahoo_profile("AAPL")
    #     self.assertEqual(erg["sector"],"Technology")
    #     self.assertTrue(isinstance(erg["empl"], int))
    #
    # def test_profile_AMZN(self):
    #     erg = read_yahoo_profile("AMZN")
    #     self.assertEqual(erg["sector"],"Consumer Cyclical")
    #     self.assertTrue(isinstance(erg["empl"], int))
    #
    # def test_profile_CAT(self):
    #     erg = read_yahoo_profile("CAT")
    #     self.assertEqual(erg["sector"],"Industrials")
    #     self.assertTrue(isinstance(erg["empl"], int))

    # def test_statistics_AAPL(self):
    #     erg1,erg2 = read_yahoo_statistics("AAPL")
    #     self.assertTrue((erg1["Revenue (ttm)"].replace(".","").replace("B","").replace(" ","")).isdigit())
    #     self.assertTrue(erg1["Book Value Per Share (mrq)"].replace(".","").isdigit())
    #     self.assertEqual(len(erg2["Enterprise Value"]),6)
    #     self.assertTrue(erg2["PEG Ratio (5 yr expected)"][2].replace(".","").isdigit())
    #
    # def test_statistics_AMZN(self):
    #     erg1,erg2 = read_yahoo_statistics("AMZN")
    #     self.assertTrue ((erg1["Revenue (ttm)"].replace (".", "").replace ("B", "").replace (" ", "")).isdigit ())
    #     self.assertTrue (erg1["Book Value Per Share (mrq)"].replace (".", "").isdigit ())
    #     self.assertEqual (len (erg2["Enterprise Value"]), 6)
    #     self.assertTrue (erg2["PEG Ratio (5 yr expected)"][2].replace (".", "").isdigit ())
    #
    # def test_statistics_CAT(self):
    #     erg1,erg2 = read_yahoo_statistics("CAT")
    #     self.assertTrue ((erg1["Revenue (ttm)"].replace (".", "").replace ("B", "").replace (" ", "")).isdigit ())
    #     self.assertTrue (erg1["Book Value Per Share (mrq)"].replace (".", "").isdigit ())
    #     self.assertEqual (len (erg2["Enterprise Value"]), 6)
    #     self.assertTrue (erg2["PEG Ratio (5 yr expected)"][2].replace (".", "").isdigit ())

    # def test_income_statement_AAPL(self):
    #     erg = read_yahoo_income_statement("AAPL")
    #     self.assertEqual (len (erg["Cost of Revenue"]), 5)
    #     self.assertTrue((erg["Operating Expense"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())
    # 
    # def test_income_statement_AMZN(self):
    #     erg = read_yahoo_income_statement("AMZN")
    #     self.assertEqual (len (erg["Cost of Revenue"]), 5)
    #     self.assertTrue((erg["Operating Expense"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())
    # 
    # def test_income_statement_CAT(self):
    #     erg = read_yahoo_income_statement("CAT")
    #     self.assertEqual (len (erg["Cost of Revenue"]), 5)
    #     self.assertTrue((erg["Operating Expense"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())

    # def test_balance_sheet_AAPL(self):
    #      erg = read_yahoo_balance_sheet("AAPL")
    #      self.assertEqual (len (erg["Current Assets"]), 4)
    #      self.assertTrue((erg["Current Liabilities"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())

    # def test_balance_sheet_AMZN(self):
    #     erg = read_yahoo_balance_sheet("AMZN")
    #     self.assertEqual (len (erg["Current Assets"]), 4)
    #     self.assertTrue((erg["Current Liabilities"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())
    # 
    # def test_balance_sheet_CAT(self):
    #     erg = read_yahoo_balance_sheet("CAT")
    #     self.assertEqual (len (erg["Current Assets"]), 4)
    #     self.assertTrue((erg["Current Liabilities"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())

    # def test_cashflow_AAPL(self):
    #      erg = read_yahoo_cashflow("AAPL")
    #      self.assertEqual (len (erg["Operating Cash Flow"]), 5)
    #      self.assertTrue((erg["Free Cash Flow"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())
    #
    # def test_cashflow_AMZN(self):
    #      erg = read_yahoo_cashflow("AAPL")
    #      self.assertEqual (len (erg["Operating Cash Flow"]), 5)
    #      self.assertTrue((erg["Free Cash Flow"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())
    #
    # def test_cashflow_CAT(self):
    #      erg = read_yahoo_cashflow("AAPL")
    #      self.assertEqual (len (erg["Operating Cash Flow"]), 5)
    #      self.assertTrue((erg["Free Cash Flow"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())

    #def test_analysis_AAPL(self):
    #     erg = read_yahoo_analysis("AAPL")
    #     self.assertEqual (len (erg["EPS Est."]), 4)
    #     self.assertTrue((erg["Avg. Estimate"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())
    #     self.assertTrue(erg["Recommendation Rating"][0] in ["1","2","3","4","5"])

    def test_analysis_AMZN(self):
         erg = read_yahoo_analysis("AMZN")
         self.assertEqual (len (erg["EPS Est."]), 4)
         self.assertTrue((erg["Avg. Estimate"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())
         self.assertTrue(erg["Recommendation Rating"][0] in ["1","2","3","4","5"])

    # def test_analysis_CAT(self):
    #      erg = read_yahoo_analysis("CAT")
    #      self.assertEqual (len (erg["EPS Est."]), 4)
    #      self.assertTrue((erg["Avg. Estimate"][3].replace(".","").replace("B","").replace(" ","").replace(",","")).isdigit())
    #      #self.assertTrue(erg["Recommendation Rating"][0] in ["1","2","3","4","5"])

if __name__ == '__main__': unittest.main()
