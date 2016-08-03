import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def test_give_custom_raise(self):
        charlie = Employee('charlie', 'bear', 50000)
        charlie.give_raise(200)
        self.assertEqual(charlie.annual_salary, 50200)

    def test_give_default_raise(self):
        charlie = Employee('charlie', 'bear', 50000)
        charlie.give_raise()
        self.assertEqual(charlie.annual_salary, 55000)

unittest.main()
