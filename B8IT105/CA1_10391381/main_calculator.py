"""Continuous Assessment
Dublin Business School
B8IT105 Programming for Big Data (B8IT105_1819_TME1S)
Lecturer: Darren Redmond
Student: Daniel Pereira (10391381@mydbs.ie)
________________________________________________________________________________

Assignment 1 - A 10 Function Calculator (10%):

This is the main file to run the calculator class
"""
import os
from calculator import Calculator

##################################################
# the main code starts here
keepMainLooping = True
while (keepMainLooping):
    #clean the console
    os.system('cls')
        
    #display the small header
    print("*"*80)
    print("{0:<40s}{1:>40s}".format("* CA - B8IT105 Programming for Big Data (B8IT105_1819_TME1S)", "Daniel Pereira (10391381@mydbs.ie) *"))
    print("*"*80)

    #display the program header
    print("{:^80}".format("CALCULATOR"))
    print("#"*80)
    
    calc = Calculator()

    #display the menu
    print("[1]  : Sum")
    print("[2]  : Subtract")
    print("[3]  : Multiply")
    print("[4]  : Divide")
    print("[5]  : Power (Exponent)")
    print("[6]  : Square Root")
    print("[7]  : Sine")
    print("[8]  : Cosine")
    print("[9]  : Tangent")
    print("[10] : Logarithm base-10")
    print("[99] : Exit the program")

    try:
        menuItem = int(input("Enter your menu option: "))
    except ValueError:
        print("#### Invalid entry! ####")
    else:
        keepLoopItem = True
        while (keepLoopItem):
            if (menuItem == 1):
                # sum
                print("\n{:^80}".format("-* Sum of two numbers *-"))
                print("_"*80)

                num1 = input("Enter the first number: ")
                num2 = input("Enter the second number: ")
            
                try:
                    print("\n{0} + {1} = {2}".format(num1, num2, calc.Add(num1,num2)))
                except Exception as e:
                    print("#### An error happened")

            elif (menuItem == 2):
                # subtract
                print("\n{:^80}".format("-* Subtraction of two numbers *-"))
                print("_"*80)

                num1 = input("Enter the first number: ")
                num2 = input("Enter the second number: ")
            
                try:
                    print("\n{0} - {1} = {2}".format(num1, num2, calc.Subtract(num1,num2)))
                except Exception as e:
                    print("#### An error happened")
            
            elif (menuItem == 3):
                # multiply
                print("\n{:^80}".format("-* Multiplication of two numbers *-"))
                print("_"*80)

                num1 = input("Enter the first number: ")
                num2 = input("Enter the second number: ")
            
                try:
                    print("\n{0} * {1} = {2}".format(num1, num2, calc.Multiply(num1,num2)))
                except Exception as e:
                    print("#### An error happened")
            
            elif (menuItem == 4):
                # divide
                print("\n{:^80}".format("-* Division of two numbers *-"))
                print("_"*80)

                num1 = input("Enter the first number: ")
                num2 = input("Enter the divisor number: ")
            
                try:
                    if (int(num2) == 0):
                        print("#### Second number is invalid. Can't divide by 0")
                    else:
                        print("\n{0} / {1} = {2}".format(num1, num2, calc.Divide(num1,num2)))
                except Exception as e:
                    print("#### An error happened")
            
            elif (menuItem == 5):
                # power
                print("\n{:^80}".format("-* Power of a number *-"))
                print("_"*80)

                num1 = input("Enter the number: ")
                num2 = input("Enter the exponent number: ")
            
                try:
                    print("\n{0} ** {1} = {2}".format(num1, num2, calc.Power(num1,num2)))
                except Exception as e:
                    print("#### An error happened")
            
            elif (menuItem == 6):
                # square root
                print("\n{:^80}".format("-* Square root of a number *-"))
                print("_"*80)

                num = input("Enter the number: ")
            
                try:
                    print("\nSquare root of {0} is {1}".format(num, calc.SquareRoot(num)))
                except Exception as e:
                    print("#### An error happened")
                
            elif (menuItem == 7):
                # sine
                print("\n{:^80}".format("-* Sine of radians *-"))
                print("_"*80)

                num = input("Enter the radiant: ")
            
                try:
                    print("\nSine of {0} is {1}".format(num, calc.Sine(num)))
                except Exception as e:
                    print("#### An error happened")
                
            elif (menuItem == 8):
                # cosine
                print("\n{:^80}".format("-* Cosine of radians *-"))
                print("_"*80)

                num = input("Enter the radiant: ")
            
                try:
                    print("\nCosine of {0} is {1}".format(num, calc.Cosine(num)))
                except Exception as e:
                    print("#### An error happened")
                
            elif (menuItem == 9):
                # tangent
                print("\n{:^80}".format("-* Tangent of radians *-"))
                print("_"*80)

                num = input("Enter the radiant: ")
            
                try:
                    print("\nTangent of {0} is {1}".format(num, calc.Tangent(num)))
                except Exception as e:
                    print("#### An error happened")
                
            elif (menuItem == 10):
                # tangent
                print("\n{:^80}".format("-* Logarithm Base-10 *-"))
                print("_"*80)

                num = input("Enter a number: ")
            
                try:
                    print("\nLog base-10 of {0} is {1}".format(num, calc.LogBase10(num)))
                except Exception as e:
                    print("#### An error happened")
                
            elif (menuItem == 99):
                keepMainLooping = False
                keepLoopItem = False
                print("---- Good bye!")
                continue
            else:
                print("#### Invalid entry! ####")

            tryAgain = 'Y'
            while tryAgain == 'Y':
                tryAgain = input("\nWould you like try it again? [Y|N] : ")
                if (tryAgain.upper() == 'Y'):
                    keepLoopItem = True
                elif(tryAgain.upper() == 'N'):
                    keepLoopItem = False
                else:
                    tryAgain = 'Y'
                    print("#### Invalid entry! ####")




