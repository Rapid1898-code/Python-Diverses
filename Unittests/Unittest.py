import unittest
from full_names import get_full_name

class TestSomething(unittest.TestCase):
    def test_first_last(self):
        name1 = get_full_name('Joe', 'Doe')
        self.assertEqual(name1,"Joe Doe")

if __name__ == '__main__': unittest.main()