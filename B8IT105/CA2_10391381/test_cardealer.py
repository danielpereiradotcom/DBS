"""Continuous Assessment
Dublin Business School
B8IT105 Programming for Big Data (B8IT105_1819_TME1S)
Lecturer: Darren Redmond
Student: Daniel Pereira (10391381@mydbs.ie)
________________________________________________________________________________

CA2 - Car Dealership - 10%:

This is the main file to run the car dealer class
"""
##################################################
import unittest
from cardealear import CarDealer

#test class
class TestCarDealer(unittest.TestCase):
    '''
    This is the test class for the car dealer
    Args: (unittest.TestCase) : receives the unit test case class
    '''
    #  50% petrol=20, 20% diesel=8, 10% electric=4 and 20% hybrid=8.
    def setUp(self):
        self.carDealer = CarDealer()

    #test the total number of available cars
    def testTotalAvailableCarsCorrectResult(self):
        self.assertEqual(40, self.carDealer.TotalAvailableCars)

    def testAvailablePetrolCorrectResult(self):
        self.assertEqual(20, self.carDealer.TotalAvailablePetrol)

    def testAvailableDieselCorrectResult(self):
        self.assertEqual(8, self.carDealer.TotalAvailableDiesel)

    def testAvailableEletricCorrectResult(self):
        self.assertEqual(4, self.carDealer.TotalAvailableEletric)

    def testAvailableHybridCorrectResult(self):
        self.assertEqual(8, self.carDealer.TotalAvailableHybrid)

    def testCarsPrefixCorrectResult(self):
        self.assertEqual("P", self.carDealer.PETROL_PREFIX)
        self.assertEqual("D", self.carDealer.DIESEL_PREFIX)
        self.assertEqual("E", self.carDealer.ELETRIC_PREFIX)
        self.assertEqual("H", self.carDealer.HYBRID_PREFIX)

    def testRentCarCorrectResult(self):
        self.assertTrue(self.carDealer.RentCar(self.carDealer.PETROL_PREFIX, "Daniel"))
        self.assertEqual(39, self.carDealer.TotalAvailableCars)
        self.assertEqual(19, self.carDealer.TotalAvailablePetrol)
        self.assertTrue(self.carDealer.RentCar(self.carDealer.PETROL_PREFIX, "Matthew"))
        self.assertEqual(38, self.carDealer.TotalAvailableCars)
        self.assertEqual(18, self.carDealer.TotalAvailablePetrol)
        self.assertTrue(self.carDealer.RentCar(self.carDealer.PETROL_PREFIX, "David"))
        self.assertEqual(37, self.carDealer.TotalAvailableCars)
        self.assertEqual(17, self.carDealer.TotalAvailablePetrol)
        
        self.assertTrue(self.carDealer.RentCar(self.carDealer.DIESEL_PREFIX, "Mark"))
        self.assertEqual(36, self.carDealer.TotalAvailableCars)
        self.assertEqual(7, self.carDealer.TotalAvailableDiesel)
        
        self.assertTrue(self.carDealer.RentCar(self.carDealer.ELETRIC_PREFIX, "Patricia"))
        self.assertEqual(35, self.carDealer.TotalAvailableCars)
        self.assertEqual(3, self.carDealer.TotalAvailableEletric)

        self.assertTrue(self.carDealer.RentCar(self.carDealer.HYBRID_PREFIX, "Holly"))
        self.assertEqual(34, self.carDealer.TotalAvailableCars)
        self.assertEqual(7, self.carDealer.TotalAvailableHybrid)

        self.assertFalse(self.carDealer.RentCar("Z", "Zoe"))
        self.assertFalse(self.carDealer.RentCar(123, "John"))

    def testReturnCarCorrectResult(self):
        #first, rent cars
        self.assertTrue(self.carDealer.RentCar(self.carDealer.PETROL_PREFIX, "Daniel"))
        self.assertTrue(self.carDealer.RentCar(self.carDealer.PETROL_PREFIX, "Matthew"))
        self.assertTrue(self.carDealer.RentCar(self.carDealer.PETROL_PREFIX, "David"))        
        self.assertTrue(self.carDealer.RentCar(self.carDealer.DIESEL_PREFIX, "Mark"))
        self.assertTrue(self.carDealer.RentCar(self.carDealer.ELETRIC_PREFIX, "Patricia"))
        self.assertTrue(self.carDealer.RentCar(self.carDealer.HYBRID_PREFIX, "Holly"))

        #last, return cars
        self.assertTrue(self.carDealer.ReturnCar(self.carDealer.PETROL_PREFIX, "Daniel"))
        self.assertEqual(35, self.carDealer.TotalAvailableCars)
        self.assertEqual(18, self.carDealer.TotalAvailablePetrol)
        self.assertTrue(self.carDealer.ReturnCar(self.carDealer.PETROL_PREFIX, "Matthew"))
        self.assertEqual(36, self.carDealer.TotalAvailableCars)
        self.assertEqual(19, self.carDealer.TotalAvailablePetrol)
        self.assertTrue(self.carDealer.ReturnCar(self.carDealer.PETROL_PREFIX, "David"))
        self.assertEqual(37, self.carDealer.TotalAvailableCars)
        self.assertEqual(20, self.carDealer.TotalAvailablePetrol)
        
        self.assertTrue(self.carDealer.ReturnCar(self.carDealer.DIESEL_PREFIX, "Mark"))
        self.assertEqual(38, self.carDealer.TotalAvailableCars)
        self.assertEqual(8, self.carDealer.TotalAvailableDiesel)
        
        self.assertTrue(self.carDealer.ReturnCar(self.carDealer.ELETRIC_PREFIX, "Patricia"))
        self.assertEqual(39, self.carDealer.TotalAvailableCars)
        self.assertEqual(4, self.carDealer.TotalAvailableEletric)

        self.assertTrue(self.carDealer.ReturnCar(self.carDealer.HYBRID_PREFIX, "Holly"))
        self.assertEqual(40, self.carDealer.TotalAvailableCars)
        self.assertEqual(8, self.carDealer.TotalAvailableHybrid)

        self.assertFalse(self.carDealer.ReturnCar("Z", "Zoe"))
        self.assertFalse(self.carDealer.ReturnCar(123, "John"))

# execute the unit test
unittest.main()