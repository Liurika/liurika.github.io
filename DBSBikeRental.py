
#####################################
#### Laura Lorenzo    10345882   ####
#####################################

# CA 2: DBS Motorbike Rental #

'''DBS Motorbike Rental rents motorbikes to customers. They have the potential to rent either electric, petrol, hybrid or diesel motorbikes.
They have initially 40 motorbikes in their rental pool made up of 60% petrol, 20% diesel, 10% electric and 10% hybrid.
When a motorbike is not rented it is available to the customer to rent.
Once a motorbike is rented it is assigned to the customer, and removed from the rental pool.
When the motorbike is returned by the customer it is assigned back into the rental pool.
If all 40 motorbikes are rented out the rental function should return a message to the customer saying "Sorry nothing to rent, please try again"'''

# Imports #

from Motorbike import *

# Class creation for Motorbike Rental #
    
class RentABike(object):
    # This function sets up the lists for the rest of functions in the class
    def __init__(self):
        self.electricbikes = []
        self.petrolbikes = []
        self.hybridbikes = []
        self.dieselbikes = []
    
    # This function generates the original stock
    def fullStock(self):
        for bike in range(8):
            self.electricbikes.append(ElectricBike())
        for bike in range(24):
            self.petrolbikes.append(PetrolBike())
        for bike in range(4):
            self.hybridbikes.append(HybridBike())
        for bike in range(4):
            self.dieselbikes.append(DieselBike())

    # This function displays the current stock
    def stockDisplay(self):
        print '########################'
        print 'Electric motorbikes: ' + str(len(self.electricbikes))
        print 'Petrol motorbikes: ' + str(len(self.petrolbikes))
        print 'Hybrid motorbikes: ' + str(len(self.hybridbikes))
        print 'Diesel motorbikes: ' + str(len(self.dieselbikes))
        print '########################\n'

    # This function handles motorbike renting, removing the rented bike from the list
    def rent(self, motorbikelist, amount):
        total = 0
        if amount < 0:
            print 'We cannot rent negative bikes ;)'
        elif amount == 0:
            print 'OK, no bikes for you.'
        elif amount <= len(motorbikelist):
            while total < amount:
                motorbikelist.pop()
                total = total + 1
            print 'Motorbike(s) rented successfully.'
        else:
            print 'We do not have enough motorbikes in stock at the moment.'
    # This is the interface for motorbike renting, allowing the user to choose type and amount of motorbikes
    def bikeRental(self):
        type = raw_input("Which type of motorbike would you like?\nElectric 'e'\nPetrol 'p'\nHybrid 'h'\nDiesel 'd'\n> ")
        amount = int(raw_input('How many motorbikes of this type would you like?\n> '))
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
    
    # This is the function that handles returns, adding back to lists
    def returnal(self, motorbikelist, amount):
        total = 0
        if amount < 0:
            print 'We cannot return negative bikes ;)'
        elif amount == 0:
            print 'We take it you still want to ride a bit longer.'
        else:
            while total < amount:
                motorbikelist.append(1)
                total = total + 1
            print 'Motorbike(s) returned successfully.'
    
    # This is the interface for motorbike returns, allowing the user to choose type and amount of bikes
    # and limiting returns to original stock
    def bikeReturn(self):
        type = raw_input("Which type of motorbike are you returning?\nElectric 'e'\nPetrol 'p'\nHybrid 'h'\nDiesel 'd'\n> ")
        amount = int(raw_input('How many?\n> '))
        if type == 'e' and len(self.electricbikes) + amount <= 8:
            self.returnal(self.electricbikes, amount)
        elif type == 'p' and len(self.petrolbikes) + amount <= 24:
            self.returnal(self.petrolbikes, amount)
        elif type == 'h' and len(self.hybridbikes) + amount <= 4:
            self.returnal(self.hybridbikes, amount)
        elif type == 'd'and len(self.dieselbikes) + amount <= 4:
            self.returnal(self.dieselbikes, amount)
        else:
            print 'We did not have that many. Please try again.'

    # This is the main interface in which the user chooses whether to rent or return
    def interface(self):
        print 'Welcome to DBS Motorbike Rental. This is our current stock:\n'
        self.stockDisplay()
        user = raw_input("Do you wish to rent 'r' or return 't' a motorbike?\n> ")
        if user == 'r':
            self.bikeRental()
        else:
            self.bikeReturn()
  
# This is the application of the RentABike class object, it makes the previous work smoothly and handles input errors  
if __name__ == '__main__':
    rent = RentABike()
    rent.fullStock()
    cont = 'y'
    while cont == 'y':
        try:
            rent.interface()
        except:
            print 'Not a valid input. Please, try again.'
        cont = raw_input('Do you wish to continue? y/n\n> ')
    print ' Thank you for choosing DBS Motorbike Rental!'