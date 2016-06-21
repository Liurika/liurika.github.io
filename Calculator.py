### CA Program: Calculator with 10 functions and 10 tests for the functions ###

#### Laura Lorenzo 10345882 ####

'''In this module, we have created a class called Calculator which is extended as an object. This Calculator object has 13 functions; 10 of the functions
are operations of a calculator such as add, substract, multiply, divide, square, etc., the other 3 functions handle user input and let the user decide which
operation they want to execute. At the end of the module we have implemented the application of the Calculator class and an 'if' statement to make it run
repeatedly until the user ends it.'''

# This is the class for the object Calculator, and it contains 10 operations of a calculator plus the functions for user input #
class Calculator(object):
    # This function adds values of x and y arguments #
	def add(self,x,y):
		return x+y 

	# This function substracts the value of y from the value of x #
	def substract(self,x,y):
		return x-y
		
	# This function multiplies the values of x and y #
	def multip(self,x,y):
		return x*y
		
	# This function divides the value of x by the value of y #
	def divide(self,x,y):
		if y == 0:
			return None
		else:
			return x/y
			
	# This function returns the value of x to the power of 2 #
	def square(self,x):
		return x**2
		
	# This function returns the value of x to the power of 3 #
	def cube(self,x):
		return x**3
		
	# This function returns the factorial of the value of x #
	def factorial(self,x):
		x = int(x)
		if x == 0:
			return 1
		elif x < 0:
			return None	
		else:
			return x*self.factorial(x-1)
			
	# This function returns the value of x to the power of the value of y #
	def exp(self,x,y):
		return x**y
		
	# This function return the square root of the value of x #
	def sqrt(self,x):
		if x < 0:
			return None
		else:
			return x**(0.5)
			
	# This function returns the cube root of the value of x #
	def cbrt(self,x):
		if x < 0:
			return None
		else:
			return x**(1.0/3.0)
			
	# This function retrieves the user input and converts it into a float value of x so it can be used by the previous functions #
	def oneinput(self):
		try:	
			num = raw_input('Enter a number: ')
			x = float(num)
			return x
		except:
			print 'I cannot compute that. Try again'
			self.interface()
	
	# This function retrieves the user input and converts it into a float value of x and y so they can be used by the previous functions #
	def inputboth(self):
		try:
			x = float(input('Enter a number: '))
			y = float(input('Enter second number: '))
			return (x, y)
		except:
			print 'I cannot compute that. Try again'
			self.interface()
	
		# This function displays a user interface in which an operation can be chosen and values can be introduced by calling the input functions #
	def interface(self):
		menu = raw_input('Choose the operation you would like to perform:\n1 ADD\n2 SUBSTRACT\n3 MULTIPLY\n4 DIVIDE\n5 SQUARE\n6 CUBE\n7 FACTORIAL\n8 EXPONENTIAL\n9 SQUARE ROOT\n10 CUBE ROOT\n>')
		if menu == '1':
			(x,y) = self.inputboth()
			print self.add(x,y)
		elif menu == '2':
			(x,y) = self.inputboth()
			print self.substract(x,y)
		elif menu == '3':
			(x,y) = self.inputboth()
			print self.multip(x,y)
		elif menu == '4':
			(x,y) = self.inputboth()
			print self.divide(x,y)
		elif menu == '5':
			x = self.oneinput()
			print self.square(x)
		elif menu == '6':
			x = self.oneinput()
			print self.cube(x)
		elif menu == '7':
			print 'Numbers with decimals will be converted to integer.'
			x = self.oneinput()
			print self.factorial(x)
		elif menu == '8':
			(x,y) = self.inputboth()
			print self.exp(x,y)
		elif menu == '9':
			x = self.oneinput()
			print self.sqrt(x)
		elif menu == '10':
			x = self.oneinput()
			print self.cbrt(x)
		else:
			print 'Not an option'

# This is the Calculator App which allows for a continuous use of the menu and its functions until the user states otherwise #
if __name__ == '__main__':
	calc = Calculator()
	cont = 'y'		
	while cont == 'y':
		try:
			calc.interface()
		except:
			pass
		cont = raw_input('Do you wish to perform another operation? y/n\n> ')