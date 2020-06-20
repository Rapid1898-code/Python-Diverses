import unittest
from YahooCrawler import read_yahoo_summary
from YahooCrawler import read_yahoo_profile
from YahooCrawler import read_yahoo_statistics

class TestYahooCrawler(unittest.TestCase):
    def test_summary_AAPL(self):
        erg = read_yahoo_summary("AAPL")
        self.assertEqual(erg["symbol"],"AAPL")
        self.assertEqual(erg["name"], "Apple Inc.")
        self.assertTrue(isinstance(erg["price"],float))

    def test_summary_AMZN(self):
        erg = read_yahoo_summary("AMZN")
        self.assertEqual(erg["symbol"],"AMZN")
        self.assertEqual(erg["name"], "Amazon.com, Inc.")
        self.assertTrue(isinstance(erg["price"],float))

    def test_summary_CAT(self):
        erg = read_yahoo_summary("CAT")
        self.assertEqual(erg["symbol"],"CAT")
        self.assertEqual(erg["name"], "Caterpillar Inc.")
        self.assertTrue(isinstance(erg["price"],float))

    def test_profile_AAPL(self):
        erg = read_yahoo_profile("AAPL")
        self.assertEqual(erg["sector"],"Technology")
        self.assertTrue(isinstance(erg["empl"], int))

    def test_profile_AMZN(self):
        erg = read_yahoo_profile("AMZN")
        self.assertEqual(erg["sector"],"Consumer Cyclical")
        self.assertTrue(isinstance(erg["empl"], int))

    def test_profile_CAT(self):
        erg = read_yahoo_profile("CAT")
        self.assertEqual(erg["sector"],"Industrials")
        self.assertTrue(isinstance(erg["empl"], int))

    def test_statistics_AAPL(self):
        erg = read_yahoo_statistics("AAPL")
        self.assertTrue((erg["EBITDA"].replace(".","").replace("B","").replace(" ","")).isdigit())

    def test_statistics_AMZN(self):
        erg = read_yahoo_statistics("AMZN")
        self.assertTrue((erg["EBITDA"].replace(".","").replace("B","").replace(" ","")).isdigit())

    def test_statistics_CAT(self):
        erg = read_yahoo_statistics("CAT")
        self.assertTrue((erg["EBITDA"].replace(".","").replace("B","").replace(" ","")).isdigit())


if __name__ == '__main__': unittest.main()
