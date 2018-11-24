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
import os
from cardealear import CarDealer

# the main code starts here
#instantiate car dealer class
carDealer = CarDealer()

keepMainLooping = True
while (keepMainLooping):
    #clean the console
    os.system('cls')
        
    #display the small header
    print("*"*80)
    print("{0:<40s}{1:>40s}".format("* CA - B8IT105 Programming for Big Data (B8IT105_1819_TME1S)", "Daniel Pereira (10391381@mydbs.ie) *"))
    print("*"*80)

    #display the program header
    print("{:^80}".format("CAR DEALER"))
    print("#"*80)

    #display the menu
    print("[1]  : Rent a car")
    print("[2]  : Return a car")
    print("[3]  : Listing rentals")
    print("[99] : Exit the program")

    try:
        menuItem = int(input("Enter your menu option: "))
    except ValueError:
        print("#### Invalid entry! ####")
    else:
        keepLoopItem = True
        while (keepLoopItem):
            if (menuItem == 1):
                # rent a car
                print("\n{:^80}".format("-* Rent a car *-"))
                print("_"*80)

                print("Available cars:", carDealer.TotalAvailableCars, "total")
                print("   Petrol -> ", carDealer.TotalAvailablePetrol, "cars")
                print("   Diesel -> ", carDealer.TotalAvailableDiesel, "cars")
                print("   Eletric -> ", carDealer.TotalAvailableEletric, "cars")
                print("   Hybrid -> ", carDealer.TotalAvailableHybrid, "cars")
                print("_"*80)

                print("[P]Petrol / [D]Diesel / [E]Eletric / [H]Hybrid")
                carToRent = input("What car would you like to rent? ")
                
                if (carToRent.upper() == carDealer.PETROL_PREFIX):
                    #petrol
                    #routine to rent a car
                    print("-* Renting a Petrol car *-")
                    
                    #get customer details
                    #TODO: Could elaborate routine to enter customer details and class/object
                    customer = input("Enter the customer Name: ")
                    
                    #call rent routine
                    if (carDealer.RentCar(carDealer.PETROL_PREFIX, customer)):
                        print("***- Car rented successfully")
                    else:
                        print("**** Some error happened to rent a car")

                elif (carToRent.upper() == carDealer.DIESEL_PREFIX):
                    #diesel
                    #routine to rent a car
                    print("-* Renting a Diesel car *-")
                    
                    #get customer details
                    #TODO: Could elaborate routine to enter customer details and class/object
                    customer = input("Enter the customer Name: ")
                    
                    #call rent routine
                    if (carDealer.RentCar(carDealer.DIESEL_PREFIX, customer)):
                        print("***- Car rented successfully")
                    else:
                        print("**** Some error happened to rent a car")

                elif (carToRent.upper() == carDealer.ELETRIC_PREFIX):
                    #eletric
                    #routine to rent a car
                    print("-* Renting an Eletric car *-")
                    
                    #get customer details
                    #TODO: Could elaborate routine to enter customer details and class/object
                    customer = input("Enter the customer Name: ")
                    
                    #call rent routine
                    if (carDealer.RentCar(carDealer.ELETRIC_PREFIX, customer)):
                        print("***- Car rented successfully")
                    else:
                        print("**** Some error happened to rent a car")

                elif (carToRent.upper() == carDealer.HYBRID_PREFIX):
                    #hybrid
                    #routine to rent a car
                    print("-* Renting a Hybrid car *-")
                    
                    #get customer details
                    #TODO: Could elaborate routine to enter customer details and class/object
                    customer = input("Enter the customer Name: ")
                    
                    #call rent routine
                    if (carDealer.RentCar(carDealer.HYBRID_PREFIX, customer)):
                        print("***- Car rented successfully")
                    else:
                        print("**** Some error happened to rent a car")

                else:
                    print("#### Invalid Car option!")
            
            elif (menuItem == 2):
                # return a car
                print("\n{:^80}".format("-* Return a car *-"))
                print("_"*80)

                print("[P]Petrol / [D]Diesel / [E]Eletric / [H]Hybrid")
                carToReturn = input("What car would you like to return? ")

                if (carToReturn.upper() == carDealer.PETROL_PREFIX):
                    #petrol
                    #routine to return a car
                    print("-* Returning a Petrol car *-")
                    
                    #get customer details
                    #TODO: Could elaborate routine to enter customer details and class/object
                    customer = input("Enter the customer Name: ")
                    
                    #call return routine
                    if (carDealer.ReturnCar(carDealer.PETROL_PREFIX, customer)):
                        print("***- Car returned successfully")
                    else:
                        print("**** Some error happened to return a car")

                elif (carToReturn.upper() == carDealer.DIESEL_PREFIX):
                    #diesel
                    #routine to return a car
                    print("-* Returning a Diesel car *-")
                    
                    #get customer details
                    #TODO: Could elaborate routine to enter customer details and class/object
                    customer = input("Enter the customer Name: ")
                    
                    #call return routine
                    if (carDealer.ReturnCar(carDealer.DIESEL_PREFIX, customer)):
                        print("***- Car returned successfully")
                    else:
                        print("**** Some error happened to return a car")

                elif (carToReturn.upper() == carDealer.ELETRIC_PREFIX):
                    #eletric
                    #routine to return a car
                    print("-* Returning a Eletric car *-")
                    
                    #get customer details
                    #TODO: Could elaborate routine to enter customer details and class/object
                    customer = input("Enter the customer Name: ")
                    
                    #call rent routine
                    if (carDealer.ReturnCar(carDealer.ELETRIC_PREFIX, customer)):
                        print("***- Car returned successfully")
                    else:
                        print("**** Some error happened to return a car")

                elif (carToReturn.upper() == carDealer.HYBRID_PREFIX):
                    #petrol
                    #routine to return a car
                    print("-* Returning a Hybrid car *-")
                    
                    #get customer details
                    #TODO: Could elaborate routine to enter customer details and class/object
                    customer = input("Enter the customer Name: ")
                    
                    #call rent routine
                    if (carDealer.ReturnCar(carDealer.HYBRID_PREFIX, customer)):
                        print("***- Car returned successfully")
                    else:
                        print("**** Some error happened to return a car")

                else:
                    print("#### Invalid Car option!")
            
            elif (menuItem == 3):
                # listing rental
                print("\n{:^80}".format("-* Listing rentals*-"))
                print("_"*80)

                print("Available cars:", carDealer.TotalAvailableCars, "total")
                print("   Petrol -> ", carDealer.TotalAvailablePetrol, "cars")
                print("   Diesel -> ", carDealer.TotalAvailableDiesel, "cars")
                print("   Eletric -> ", carDealer.TotalAvailableEletric, "cars")
                print("   Hybrid -> ", carDealer.TotalAvailableHybrid, "cars")
                print("_"*80)

                print("Car rentals")
                pcarList = carDealer.GetPetrolCarsList()
                dcarList = carDealer.GetDieselCarsList()
                ecarList = carDealer.GetEletricCarsList()
                hcarList = carDealer.GetHybridCarsList()

                print("    Petrol")
                if (len(pcarList) == 0):
                    print("    -> all cars available")
                else:
                    for i in range(len(pcarList)):
                        print("        {0} - {1}".format(i, pcarList[i]))

                print("    Diesel")
                if (len(dcarList) == 0):
                    print("    -> all cars available")
                else:
                    for i in range(len(dcarList)):
                        print("        {0} - {1}".format(i, dcarList[i]))

                print("    Eletric")
                if (len(ecarList) == 0):
                    print("    -> all cars available")
                else:
                    for i in range(len(ecarList)):
                        print("        {0} - {1}".format(i, ecarList[i]))

                print("    Hybrid")
                if (len(hcarList) == 0):
                    print("    -> all cars available")
                else:
                    for i in range(len(hcarList)):
                        print("        {0} - {1}".format(i, hcarList[i]))

            elif (menuItem == 99):
                keepMainLooping = False
                keepLoopItem = False
                print("---- Good bye!")
                continue
            else:
                keepMainLooping = True
                menuItem = None
                print("#### Invalid entry! ####")

            while True:
                tryAgain = input("\nWould you like try it again? [Y|N] : ")
                if (tryAgain.upper() == 'Y'):
                    keepLoopItem = True
                    break
                elif(tryAgain.upper() == 'N'):
                    keepLoopItem = False
                    break
                else:
                    keepLoopItem = True
                    print("#### Invalid entry! ####")
