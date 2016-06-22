# Implementation of motorbike class

class Motorbike(object):
	#Implementation of motorbike object
	def __init__(self):
		self.__colour = ''
		self.__make = ''
		self.__mileage = 0
		self.engineSize = ''
		self.__engineType = ''
	
	#Implementation of getter functions
	def getColour(self):
		return self.__colour
	
	def getMake(self):
		return self.__make
	
	def getMileage(self):
		return self.__mileage
	
	def getEngineSize(self):
		return self.__engineSize
		
	def getEngineType(self):
		return self.__engineType
	
	#Implementation of setter functions
	def setColour(self, colour):
		self.__colour = colour
	
	def setMake(self, make):
		self.__make = make
	
	def setMileage(self, mileage):
		self.__mileage = mileage
	
	def setEngineSize(self, size):
		self.__engineSize = size
		
	def setEngineType(self, type):
		self.__engineType = type

	#Implementation of behavior functions
	def move(self, distance):
		self.__mileage = self.__mileage + distance
	
	def paint(self, colour):
		self.__colour = colour

# Motorbike types according to engine type
class ElectricBike(Motorbike):
	def __init__(self):
		Motorbike.__init__(self)
		self.__engineType = 'Electric'
		self.__batteryCharge = ''
	
	def charge(self):
		self.__batteryCharge = 'Full'
		
	def use(self):
		self.__batteryCharge = 'Empty'
	

class PetrolBike(Motorbike):
	def __init__(self):
		Motorbike.__init__(self)
		self.__engineType = 'Petrol'
		self.__petrolTank = ''
		
	def fillTank(self):
		self.__petrolTank = 'Full'
	
class HybridBike(Motorbike):
	def __init__(self):
		Motorbike.__init__(self)
		self.__fuel = ''
		
	def chargeAndfill(self):
		self.__fuel = 'Charged and Full'
		
class DieselBike(Motorbike):
	def __init__(self):
		Motorbike.__init__(self)
		self.__numberCylinders = 2
	
	def getNumberCylinders(self):
		return self.__numberCylinders
	
	def setNumberCylinders(self, value):
		self.__numberCylinders = value