import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        """setup create survey set of response"""
        self.Employee = Employee('Bob', 'Evans', 10000)

    def test(self):
        self.assertIn('Bob', self.Employee.first)
        self.assertIn('Evans', self.Employee.last)
        self.assertEqual(10000, self.Employee.salary)

    def test_give_standard_raise(self):
        self.Employee.give_standard()
        self.assertEqual(15000, self.Employee.salary)
        
    
    def test_give_custom_raise(self):
        self.Employee.give_custom(2000)
        self.assertEqual(7000, self.Employee.salary)
        
    

if __name__ == "__main__":
    unittest.main()