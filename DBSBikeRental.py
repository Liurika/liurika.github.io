# Rent a Bike #

# Imports #

from Motorbike import Motorbike
from Motorbike import ElectricBike
from Motorbike import PetrolBike
from Motorbike import DieselBike

#class BikeFleet
motorbikelist = ()
electricbikes = ()
petrolbikes = ()
dieselbikes = ()
	
def stockMgm()

def rent():
	motorbikelist.pop()
	
class RentABike(object):

    def __init__(self):
        self.electricbikes = []
        self.petrolbikes = []
		self.dieselbikes = []

    def originalStock(self):
        for bike in range(20):
			self.electricbikes.append(ElectricBike())
        for bike in range(15):
			self.petrolbikes.append(PetrolBike())
		for bike in range(5):
			self.dieselbikes.append(DieselBike())

    def stockDisplay(self):
        print 'Electric motorbikes available: ' + str(len(self.electricbikes))
        print 'Petrol motorbikes available: ' + str(len(self.petrolbikes))
		print 'Diesel motorbikes available: ' + str(len(self.dieselbikes))

    def rent(self, motorbikelist, amount):
        if len(car_list) < amount:
            print 'Not enough cars in stock'
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1

    def process_rental(self):
        answer = raw_input('would you like to rent a car? y/n')
        if answer == 'y':
            answer = raw_input('what type would you like? p/d')
            amount = int(raw_input('how many would you like?'))
            if answer == 'p':
                self.rent(self.petrol_cars, amount)
            else:
                self.rent(self.electric_cars, amount)
        self.stock_count()

dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('continue? y/n')
	
answer = raw_input('Would you like to rent a bike?')
if answer == 'yes':
	
	
	EMBRACE YOURSELF
	'''do a test for each function you write, not at the end'''
	'''pass lists as parameters of functions'''
	'''amount, total to control how many bikes'''
	'''return bikes so you don't run out of them'''