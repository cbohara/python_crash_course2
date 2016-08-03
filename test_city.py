import unittest
from city_functions import city_info

class TestCityFunctions(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_info(self):
        """Does city info like Santiago, Chile work?"""
        info = city_info('santiago', 'chile')
        self.assertEqual(info, 'Santiago, Chile')

    def test_info_with_population(self):
        """In the population info added with Santiago, Chile?"""
        info = city_info('santiago', 'chile', 50000)
        self.assertEqual(info, 'Santiago, Chile - 50000')

unittest.main()
