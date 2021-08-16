import unittest
from name_function import get_formatted_name 

class NamesTestCase(unittest.TestCase):
    """ test for name_function.py """
    def test_first_last_name(self):
        """ do names like jon doe work """
        formatted_name = get_formatted_name('john', "doe")
        self.assertEqual(formatted_name, "John Doe")

    def test_first_middle_last_name(self):
        """ do names like john albert doe work """
        formatted_name1 = get_formatted_name('john', "doe", 'albert')
        self.assertEqual(formatted_name1, "John Albert Doe")


if __name__ ==  "__main__":
    unittest.main()

