# DBS Motorbike Rental Tests #

# Imports #
from DBSBikeRental import RentABike
import unittest

class RentalTest(unittest.TestCase):
	def setUp(self):
		self.rental = RentABike()
		self.elb = self.rental.electricbikes
		self.peb = self.rental.petrolbikes
		self.hyb = self.rental.hybridbikes
		self.dib = self.rental.dieselbikes
		self.rental.fullStock()
	
	def testFullStock(self):
		self.assertEqual(8, len(self.elb))
		self.assertEqual(24, len(self.peb))
		self.assertEqual(4, len(self.hyb))
		self.assertEqual(4, len(self.dib))
		
	def testStockDisplay(self):
		self.assertEqual('8', str(len(self.elb)))
		self.assertEqual('24', str(len(self.peb)))
		self.assertEqual('4', str(len(self.hyb)))
		self.assertEqual('4', str(len(self.dib)))
		
	def testRent(self):
		self.assertEqual(self.stockDisplay(), self.rent(9, self.elb))
		
if __name__ == '__main__':
	unittest.main()