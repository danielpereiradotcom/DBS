"""
Dublin Business School
Student: Daniel Pereira (10391381@mydbs.ie)
ICT PROJECT
________________________________________________________________________________

Official UK Top 100 Singles Charts Spider
"""

##################################################
import os # for console
import scrapy # crawler
from scrapy.crawler import CrawlerProcess # crawler
import logging # log output
import re # for text parsing
from datetime import datetime as dt
from dateutil import parser
from officialukcharts import ChartScan
from multiprocessing import Process
from crochet import setup



##################################################
def menu():
    keep_loop = True
    while(keep_loop):
        #clean the console
        os.system('cls')

        #display a small header
        print("*"*80)
        print("{0:<40s}{1:>40s}".format("* Official UK Top 100 Singles Charts Spider", "Daniel Pereira (10391381@mydbs.ie) *"))
        print("*"*80)

        #display the program header
        print("{:^80}".format("-* Official UK Charts Website Spider *-"))
        print("#"*80)

        #display the menu
        print("[1]  : Full Scrap by year")
        print("[99]  : Exit the program")
        
        try:
            menuItem = int(input("Enter your menu option: "))
        except ValueError:
            print("#### Invalid entry! ####")
        else:
            if (menuItem == 1):
                print("\n{:^80}".format("-* Full Year Scrapping *-"))
                print("_"*80)

                #start_urls      = ['https://www.officialcharts.com/charts/'] # the initial url
                startYear = int(input("Enter the START YEAR: "))
                endYear = int(input("Enter the END YEAR: "))

                try:
                    while(startYear >= endYear):
                        chartSpider = ChartScan()
                        chartSpider.scanByYear(startYear)                             
                        print("----- Spider crawler complete")
                        startYear = startYear-1
                except Exception:
                    print("### Error ")
                    continue


            elif (menuItem == 99):
                keep_loop = False
                print("----- Goodbye")
                continue
            else:
                print("#### Invalid entry! ####")
        finally:
            input("----- Press any key")


## initial load code
## calling a function for the main minimise the code it loads in the entry point
if __name__ == '__main__':
    #menu()

    print("\n{:^80}".format("-* Full Year Scrapping *-"))
    print("_"*80)

    startYear = int(input("Enter the YEAR: "))
    try:
        chartSpider = ChartScan()
        chartSpider.scanByYear(startYear)                             
        print("----- Spider crawler complete")
    except Exception:
        print("### Error ")
