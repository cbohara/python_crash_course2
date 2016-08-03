import unittest
from name_function import get_formatted_name

# this subclass must inherit from unittest.TestCase superclass
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    # single method that tests one aspect of the function
    def test_first_last_name(self):
        """Do names with only a first and last name work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        # assert methods verify that the result you received matches the result expected
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """Do names with first middle and last name work?"""
        formatted_name = get_formatted_name('billy', 'thorton', 'bob')
        self.assertEqual(formatted_name, 'Billy Bob Thorton')

unittest.main()
