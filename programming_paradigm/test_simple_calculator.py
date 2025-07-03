import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator ( unittest.TestCase) :

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add (2,3),5)
        self.assertEqual(self.calc.add (-1,-3),-4)
        self.assertEqual(self.calc.add (-1,2),1)
        self.assertEqual(self.calc.add (0,0),0)
        self.assertEqual(self.calc.add (1.5,3.5),5)

    def test_subtract(self):
        """Test subtraction functionality."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(3.5, 1.2), 2.3)
        
    def test_multiply(self):
        """Test multiplication functionality."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 3), -9)
        self.assertEqual(self.calc.multiply(0, 1000), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_divide(self):
        """Test division functionality."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, -1), -5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        self.assertIsNone(self.calc.divide(5, 0))  # Edge case: division by zero

if __name__ == "__main__":
    unittest.main()

