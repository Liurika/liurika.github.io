### Tests for Calculator.py ###

################################
#### Laura Lorenzo 10345882 ####
################################

'''This tests ensure that our imported object from another module, in this case, Calculator from Calculator.py, runs as it is expected.'''


# Importing class from another module and necessary package #
from Calculator import Calculator
import unittest

class CalcTest(unittest.TestCase):
	# This function references the Calculator object so the subsequent tests can run properly #
	def setUp(self):
		self.calc = Calculator()
	
	# This tests the add function:
	# 2 + 2 = 4
	# 2 + 6 = 8
	# 8.5 + 6.5 = 15
	# 6 + (-2) = 4
	def testadd(self):
		operation = self.calc.add(2,2)
		self.assertEqual(4, operation)
		operation = self.calc.add(2,6)
		self.assertEqual(8, operation)
		operation = self.calc.add(8.5,6.5)
		self.assertEqual(15, operation)
		operation = self.calc.add(6,-2)
		self.assertEqual(4, operation)

	# This tests the substract function:
	# 4 - 2 = 2
	# 2 - 2 = 0
	# 10 - 5 = 5
	# 4 - 0 = 4
	# 5 - (-5) = 10
	# 6.5 - 3.5 = 3
	def testsubstract(self):
		operation = self.calc.substract(4,2)
		self.assertEqual(2, operation)
		operation = self.calc.substract(2,2)
		self.assertEqual(0, operation)
		operation = self.calc.substract(10,5)
		self.assertEqual(5, operation)
		operation = self.calc.substract(4,0)
		self.assertEqual(4, operation)
		operation = self.calc.substract(5,-5)
		self.assertEqual(10, operation)
		operation = self.calc.substract(6.5,3.5)
		self.assertEqual(3, operation)
	
	# This tests the multiply function:
	# 2 x 2 = 4
	# 9 x 2 = 18
	# 3 x 0 = 0
	# 12 x 0.5 = 6
	# 2 x (-4) = -8
	def testmultip(self):
		operation = self.calc.multip(2,2)
		self.assertEqual(4, operation)
		operation = self.calc.multip(9,2)
		self.assertEqual(18, operation)
		operation = self.calc.multip(3,0)
		self.assertEqual(0, operation)
		operation = self.calc.multip(12,0.5)
		self.assertEqual(6, operation)
		operation = self.calc.multip(2,-4)
		self.assertEqual(-8, operation)
	
	# This tests the divide function:
	# 4 / 2 = 2 
	# 15 / 2.0 = 7.5
	# 5 / 0 = None
	# 7 / (-7) = -1
	def testdivide(self):
		operation = self.calc.divide(4,2)
		self.assertEqual(2, operation)
		operation = self.calc.divide(15,2.0)
		self.assertEqual(7.5, operation)
		operation = self.calc.divide(5,0)
		self.assertEqual(None, operation)
		operation = self.calc.divide(7,-7)
		self.assertEqual(-1, operation)
	
	# This tests the square function:
	# 2^2 = 4 
	# 3^2 = 9
	# 0^2 = 0
	# -1^2 = 1 
	# 5.5^2 = 30.25
	# 1^2 = 1
	def testsquare(self):
		self.assertEqual(4, self.calc.square(2))
		self.assertEqual(9, self.calc.square(3))
		self.assertEqual(0, self.calc.square(0))
		self.assertEqual(1, self.calc.square(-1))
		self.assertEqual(100, self.calc.square(10))
		self.assertEqual(30.25, self.calc.square(5.5))
		self.assertEqual(1, self.calc.square(1))
	
	# This tests the cube function:
	# 2^3 = 8 
	# 3^3 = 27
	# 0^3 = 0
	# -1^3 = -1 
	# 5.5^3 = 166.375
	# 1^3 = 1
	def testcube(self):
		self.assertEqual(8, self.calc.cube(2))
		self.assertEqual(27, self.calc.cube(3))
		self.assertEqual(0, self.calc.cube(0))
		self.assertEqual(-1, self.calc.cube(-1))
		self.assertEqual(1000, self.calc.cube(10))
		self.assertEqual(166.375, self.calc.cube(5.5))
		self.assertEqual(1, self.calc.cube(1))
	
	# This tests the exponential function:
	# 2^2 = 4
	# 2^0 = 1 
	# 2^-1 = 0.5
	# -8^5 = -32768
	# -8^4 = 4096 
	def testexp(self):
		operation = self.calc.exp(2,2)
		self.assertEqual(4, operation)
		operation = self.calc.exp(2,0)
		self.assertEqual(1, operation)
		operation = self.calc.exp(2,-1)
		self.assertEqual(0.5, operation)
		operation = self.calc.exp(-8,5)
		self.assertEqual(-32768, operation)
		operation = self.calc.exp(-8,4)
		self.assertEqual(4096, operation)
	
	# This tests the factorial function:
	# 2! = 2 
	# 3! = 6
	# 0! = 1
	# -1! = None 
	# 10! = 3628800
	# 5.5! = 120 (it is converted to 5 integer)
	# 1! = 1
	def testfactorial(self):
		self.assertEqual(2, self.calc.factorial(2))
		self.assertEqual(6, self.calc.factorial(3))
		self.assertEqual(1, self.calc.factorial(0))
		self.assertEqual(None, self.calc.factorial(-1))
		self.assertEqual(3628800, self.calc.factorial(10))
		self.assertEqual(120, self.calc.factorial(5.5))
		self.assertEqual(1, self.calc.factorial(1))
	
	# This tests the square root function:
	# sqrt(4) = 2 
	# sqrt(9) = 3 
	# sqrt(0) = 0
	# sqrt(1) = 1 
	# sqrt(100) = 10 
	# sqrt(30.25) = 5.5 
	# sqrt(-1) = None
	def testsqrt(self):
		self.assertEqual(2, self.calc.sqrt(4))
		self.assertEqual(3, self.calc.sqrt(9))
		self.assertEqual(0, self.calc.sqrt(0))
		self.assertEqual(1, self.calc.sqrt(1))
		self.assertEqual(10, self.calc.sqrt(100))
		self.assertEqual(5.5, self.calc.sqrt(30.25))
		self.assertEqual(None, self.calc.sqrt(-1))
	
	# This tests the cube root function:
	# cbrt(8) = 2 
	# cbrt(27) = 3 
	# cbrt(0) = 0
	# cbrt(-1) = None
	# cbrt(166.375) = 5.5 
	# cbrt(1) = 1
	def testcbrt(self):
		self.assertEqual(2, self.calc.cbrt(8))
		self.assertEqual(3, self.calc.cbrt(27))
		self.assertEqual(0, self.calc.cbrt(0))
		self.assertEqual(None, self.calc.cbrt(-1))
		self.assertEqual(5.5, self.calc.cbrt(166.375))
		self.assertEqual(1, self.calc.cbrt(1))
	
# Initialize test #
if __name__ == '__main__':
	unittest.main()