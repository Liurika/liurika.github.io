# DBS Motorbike Rental #

'''DBS Motorbike Rental will rent cars to their customer. They have the potential to rent either petrol, diesel, electric, or hybrid motorbikes.
They have initially 40 motorbikes in their rental pool made up of 60% petrol, 20% diesel, 10% electric and 10% hybrid.
When a motorbike is not rented it is available to the customer to rent.
Once a motorbike is rented it is assigned to the customer, and removed from the rental pool.
When the motorbike is returned by the customer it is assigned back into the rental pool.
If all 40 motorbikes are rented out the rental function should return a message to the customer saying "Sorry nothing to rent, please try again"'''

# Imports #

from Motorbike import *

# Class creation for Motorbike Rental #
	
class RentABike(object):

    def __init__(self):
		self.electricbikes = []
		self.petrolbikes = []
		self.hybridbikes = []
		self.dieselbikes = []
		self.totalbikes = []
		
    def fullStock(self):
		for bike in range(8):
			self.electricbikes.append(ElectricBike())
		for bike in range(24):
			self.petrolbikes.append(PetrolBike())
		for bike in range(4):
			self.hybridbikes.append(HybridBike())
		for bike in range(4):
			self.dieselbikes.append(DieselBike())

    def stockDisplay(self):
		print 'Electric motorbikes available: ' + str(len(self.electricbikes))
		print 'Petrol motorbikes available: ' + str(len(self.petrolbikes))
		print 'Hybrid motorbikes available: ' + str(len(self.hybridbikes))
		print 'Diesel motorbikes available: ' + str(len(self.dieselbikes))

    def rent(self, motorbikelist, amount):
        total = 0
        if amount < len(motorbikelist):
            while total < amount:
                motorbikelist.pop()
                total = total + 1
            print 'Motorbike(s) rented successfully.'
            return self.stockDisplay()
        else:
            print 'We do not have enough motorbikes in stock at the moment.'

    def bikeRental(self):
        user = raw_input('Would you like to rent a motorbike? y/n\n> ')
        if user == 'y':
            type = raw_input("Which type of motorbike would you like?\nElectric 'e'\nPetrol 'p'\nHybrid 'h'\nDiesel 'd'\n> ")
            try:
                amount = int(raw_input('How many motorbikes of this type would you like?\n> '))
            except:
                print 'Please, enter a number'
                self.bikeRental()
            if type == 'e':
                self.rent(self.electricbikes, amount)
            elif type == 'p':
                self.rent(self.petrolbikes, amount)
            elif type == 'h':
                self.rent(self.hybridbikes, amount)
            elif type == 'd':
                self.rent(self.dieselbikes, amount)
            else:
                print 'That is not a valid option. Please try again.'

if __name__ == '__main__':
	rent = RentABike()
	rent.fullStock()
	cont = 'y'
	while cont == 'y':
        try:
            rent.bikeRental()
        except:
            pass
        cont = raw_input('Do you wish to continue? y/n\n> ')
	'''do a test for each function you write, not at the end'''
	'''pass lists as parameters of functions'''
	'''amount, total to control how many bikes'''
	'''return bikes so you don't run out of them'''