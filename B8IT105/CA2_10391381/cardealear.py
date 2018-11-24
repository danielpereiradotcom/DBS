"""Continuous Assessment
Dublin Business School
B8IT105 Programming for Big Data (B8IT105_1819_TME1S)
Lecturer: Darren Redmond
Student: Daniel Pereira (10391381@mydbs.ie)
________________________________________________________________________________

CA2 - Car Dealership - 10%
Assignment 2 is based around the Car Dealership example use to demonstrate Object Oriented Programming - (see lecture notes below).
However this assignment is based on a brand new venture called Aungier Car Rental.
Aungier Car Rental will rent cars to their customer. They have the potential to rent either petrol, diesel, electric, or hybrid cars.
They have initially 40 cars in their rental pool made up of 50% petrol, 20% diesel, 10% electric and 20% hybrid.
When a car is not rented it is available to the customer to rent.
Once a car is rented the car is assigned to the customer, and removed from the rental pool.
When the car is returned by the customer it is assigned back into the rental pool.
If all 40 cars are rented out the rental function should return a message to the customer saying "Sorry nothing to rent, please try again"
All classes developed should be documented and accompanied by an associated test suite for the classes written.
"""

class CarDealer(object):
    '''
    This class represents the car dealer
    '''
    #  50% petrol=20, 20% diesel=8, 10% electric=4 and 20% hybrid=8.
    #member variables
    __totalCars = None
    __totalPetrol = None
    __totalDiesel = None
    __totalEletric = None
    __totalHybrid = None

    __petrolCarsList = None
    __dieselCarsList = None
    __eletricCarsList = None
    __hybridCarsList = None

    #constants
    PETROL_PREFIX  = "P"
    DIESEL_PREFIX  = "D"
    ELETRIC_PREFIX = "E"
    HYBRID_PREFIX  = "H"

    #constructor
    def __init__(self):
        '''
        Constructor of CarDealer class
        Cars are available in types of Petrol, Diesel, Eletric and Hybrid
        '''
        #initialize the limit of cars
        self.__totalCars = 40
        self.__totalPetrol = 20
        self.__totalDiesel = 8
        self.__totalEletric = 4
        self.__totalHybrid = 8

        #initialize array of cars
        self.__petrolCarsList = []
        self.__dieselCarsList = []
        self.__eletricCarsList = []
        self.__hybridCarsList = []

    #setters
    
    #getters
    def GetPetrolCarsList(self):
        return self.__petrolCarsList

    def GetDieselCarsList(self):
        return self.__dieselCarsList

    def GetEletricCarsList(self):
        return self.__eletricCarsList

    def GetHybridCarsList(self):
        return self.__hybridCarsList    
    
    #methods
    @property
    def TotalAvailableCars(self):
        '''int: Returns the total number of available cars'''
        return self.__totalCars

    @property
    def TotalAvailablePetrol(self):
        '''int: Returns the total number of available petrol cars'''
        return self.__totalPetrol

    @property
    def TotalAvailableDiesel(self):
        '''int: Returns the total number of available diesel cars'''
        return self.__totalDiesel

    @property
    def TotalAvailableEletric(self):
        '''int: Returns the total number of available eletric cars'''
        return self.__totalEletric

    @property
    def TotalAvailableHybrid(self):
        '''int: Returns the total number of available hybrid cars'''
        return self.__totalHybrid

    def RentCar(self, prefix, customer):
        '''
        This method rent to given customer
        E.g. RentCar("P", Daniel)
        Args:
            prefix (str): the constant for the car prefix
            customer (str): the name of customer
        Returns:
            (bool): True when success or False when fail
        Exceptions:
        
        @TODO: Customer could be an Id from another class
        '''
        try:
            if (prefix.upper() == self.PETROL_PREFIX):
                self.__petrolCarsList.append(customer)
                self.__totalPetrol = self.__totalPetrol-1
                self.__totalCars = self.__totalCars-1
            elif (prefix.upper() == self.DIESEL_PREFIX):
                self.__dieselCarsList.append(customer)
                self.__totalDiesel = self.__totalDiesel-1
                self.__totalCars = self.__totalCars-1
            elif (prefix.upper() == self.ELETRIC_PREFIX):
                self.__eletricCarsList.append(customer)
                self.__totalEletric = self.__totalEletric-1
                self.__totalCars = self.__totalCars-1
            elif (prefix.upper() == self.HYBRID_PREFIX):
                self.__hybridCarsList.append(customer)
                self.__totalHybrid = self.__totalHybrid-1
                self.__totalCars = self.__totalCars-1
            else:
                raise Exception("Not found the informed prefix.")

            return True
        except Exception:
            return False

    def ReturnCar(self, prefix, customer):
        '''
        This method return a car from a customer
        E.g. ReturnCar("P", Daniel)
        Args:
            prefix (str): the constant for the car prefix
            customer (str): the name of customer
        Returns:
            (bool): True when success or False when fail
        Exceptions:
        @TODO: Customer could be an Id from another class
        '''
        try:
            if (prefix.upper() == self.PETROL_PREFIX):
                if (len(self.__petrolCarsList)>0):
                    carIndex = self.__petrolCarsList.index(customer)
                    self.__petrolCarsList.pop(carIndex)
                    self.__totalPetrol += 1
                    self.__totalCars += 1
                else:
                    raise Exception("Petrol list is empty")
            elif (prefix.upper() == self.DIESEL_PREFIX):
                if (len(self.__dieselCarsList)>0):
                    carIndex = self.__dieselCarsList.index(customer)
                    self.__dieselCarsList.pop(carIndex)
                    self.__totalDiesel += 1
                    self.__totalCars += 1
                else:
                    raise Exception("Diesel list is empty")
            elif (prefix.upper() == self.ELETRIC_PREFIX):
                if (len(self.__eletricCarsList)>0):
                    carIndex = self.__eletricCarsList.index(customer)
                    self.__eletricCarsList.pop(carIndex)
                    self.__totalEletric += 1
                    self.__totalCars += 1
                else:
                    raise Exception("Eletric list is empty")
            elif (prefix.upper() == self.HYBRID_PREFIX):
                if (len(self.__hybridCarsList)>0):
                    carIndex = self.__hybridCarsList.index(customer)
                    self.__hybridCarsList.pop(carIndex)
                    self.__totalHybrid += 1
                    self.__totalCars += 1
                else:
                    raise Exception("Hybrid list is empty")
            else:
                raise Exception("Not found the informed prefix.")

            return True
        except Exception:
            return False
