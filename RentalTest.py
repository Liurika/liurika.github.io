
#####################################
#### Laura Lorenzo    10345882   ####
#####################################

# DBS Motorbike Rental Tests #

# Imports #
from DBSBikeRental import RentABike
import unittest

class RentalTest(unittest.TestCase):
    # This function sets up the class instance, the lists and runs the stock generator
    def setUp(self):
        self.rental = RentABike()
        self.elb = self.rental.electricbikes
        self.peb = self.rental.petrolbikes
        self.hyb = self.rental.hybridbikes
        self.dib = self.rental.dieselbikes
        self.rental.fullStock()
    
    # This test asserts that stock is generated correctly:
    # Total electric bikes = 8
    # Total petrol bikes = 24
    # Total hybrid bikes = 4
    # Total diesel bikes = 4
    def testFullStock(self):
        self.assertEqual(8, len(self.elb))
        self.assertEqual(24, len(self.peb))
        self.assertEqual(4, len(self.hyb))
        self.assertEqual(4, len(self.dib))
    
    # This test asserts that the stock display function shows stock as strings
    def testStockDisplay(self):
        self.assertEqual('8', str(len(self.elb)))
        self.assertEqual('24', str(len(self.peb)))
        self.assertEqual('4', str(len(self.hyb)))
        self.assertEqual('4', str(len(self.dib)))
     
    # This test checks that stock rentals change according to user input, and that it does not change
    # if the user enters an invalid number
    def testRent(self):
        self.rental.rent(self.peb,3)
        self.assertEqual('21', str(len(self.peb)))
        self.rental.rent(self.dib,4)
        self.assertEqual('0', str(len(self.dib)))
        self.rental.rent(self.hyb,-4)
        self.assertEqual('4', str(len(self.hyb)))
        self.rental.rent(self.hyb,0)
        self.assertEqual('4', str(len(self.hyb)))

    # This test checks that stock returns change according to user input, and that it does not change
    # if the user enters an invalid number
    def testReturnal(self):
        self.rental.returnal(self.peb, 2)
        self.assertEqual('26', str(len(self.peb)))
        self.rental.returnal(self.peb, -2)
        self.assertEqual('26', str(len(self.peb)))
        self.rental.returnal(self.elb, 0)
        self.assertEqual('8', str(len(self.elb)))
        
if __name__ == '__main__':
    unittest.main()