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
from multiprocessing import Process
from crochet import setup

class OfficialUKChartsSpider(scrapy.Spider):
    '''
    This class represents the Spider to UK Top 100 Charts
    '''
    # Spider attributes
    name            = "OfficialUKChartsSpider" # crawler identifier
    start_urls      = ['https://www.officialcharts.com/charts/singles-chart'] # the initial url or the current url
    #start_urls      = ['https://www.officialcharts.com/charts/singles-chart/19521114/7501/'] # the last chart (or the first page)
    #start_urls      = ['https://www.officialcharts.com/charts/singles-chart/20181228/7501/'] # the last chart (or the first page)
    
    
    download_delay  = 1 # multi thread delay

    # custom attributes
    __counter_of_weeks      = None
    __endChartDate      = None
    __startChartDate    = None
    __counter_out_of_range = 0
    
    # custom properties
    enforce_date_range  = False
    enforce_weeks_limit = False
    navigation_mode     = None

    # constants
    NAVIGATION_MODE_PREVIOUS    = "prev"
    NAVIGATION_MODE_NEXT        = "next"
    WEEKS_LIMIT                 = 52*5



    # custom constructor
    def __init__(self, enforceDateRange = False, 
                    enforceWeeksLimit = False, 
                    navigationMode = NAVIGATION_MODE_PREVIOUS, 
                    counterWeeks = 0, 
                    startYear = None,
                    endYear = None, *args, **kwargs):
        super(OfficialUKChartsSpider, self).__init__(*args, **kwargs)
        self.enforce_date_range     = enforceDateRange
        self.enforce_weeks_limit    = enforceWeeksLimit
        self.navigation_mode        = navigationMode #set the mode to look for previous page or next page
        self.setCounterWeeks(counterWeeks)     #just a simple counter 
        self.setStartDate(str(startYear)+'0101')    
        self.setEndDate(str(endYear)+'1231')
        if (startYear != None):
            self.start_urls = ['https://www.officialcharts.com/charts/singles-chart/'+str(endYear)+'1231/7501/']     
        
    # custom setters
    def setCounterWeeks(self, c):
        '''
        Define the counter of weeks
        '''
        self.__counter_of_weeks = c

    def setEndDate(self, d):
        '''
        Define the date that the crawling should finish
        '''
        self.__endChartDate = dt.date(parser.parse(str(d)))

    def setStartDate(self, d):
        '''
        Define the date that the crawling should start
        '''
        self.__startChartDate = dt.date(parser.parse(str(d)))


    # custom getters
    def getCounterWeeks(self):
        '''
        Return the counter of weeks
        '''
        return self.__counter_of_weeks

    def getEndDate(self):
        '''
        Return the date when the crawling process should finish 
        '''
        return self.__endChartDate

    def getStartDate(self):
        '''
        Return the date when the crawling process should start
        '''
        return self.__startChartDate

    # methods

    # Overwrite Scrapy built in parse function
    def parse(self, response):
        '''
        This function is part of Scrapy library.
        It is trigged when the process calls the URL and need to parse the values into JSON (defined via settings)
        The objective is to find each html/css tag and extract the values of the chart
        In the end, the function looks for the next url, this is done via capturing the link on page for the 'previous' week.
        '''
        
        try:
            self.__counter_of_weeks +=1
            
            # Recover the week date from html
            page_chart_week = re.sub(' -.*', '',
                                response.css('.article-heading+ .article-date::text').extract_first().strip())

            page_chart_week = dt.date(parser.parse(page_chart_week))
            self.logger.info('Week #%d (%s) - Scraping page: %s', self.getCounterWeeks(), page_chart_week, response.url)

            # this part of code will validate a page under date range
            # because it is a weekly chart a selected date can be outside of the range
            # for example 2017-01-01 is under 2016-12-30 week and would be considered invalid
            # to sort this case, after an invali page the process will check the previous page to confirm if is still out of range
            is_valid_page = False       
            if (self.__counter_out_of_range <=1):    
                if (self.enforce_weeks_limit):
                    # Validate whether is on allowed number of week interactions
                    if (self.getCounterWeeks() <= self.WEEKS_LIMIT): is_valid_page = True
                else:                    
                    if (self.enforce_date_range):
                        # Validate whether is on date range to extract information
                        if (page_chart_week >= self.getStartDate() and page_chart_week <= self.getEndDate()):
                            is_valid_page = True
                    else:
                        is_valid_page = True
            else:
                self.logger.info('Out of range counter exceeded') 

            if (is_valid_page):
                #response.css('#main .artist a::text').extract(),
                # Extract each tag from html and parse into a variable
                for (chart_pos, lastweek, artist, artist_num, track, label, peak_pos, weeks_on_chart) in \
                    zip(response.css('.position::text').extract(),
                        response.css('.last-week::text').extract(),
                        response.css('.track .title-artist .artist a::text').extract(),
                        response.css('#main .artist a::attr(href)').extract(),
                        response.css('.track .title-artist .title a::text').extract(),
                        response.css('.label-cat .label::text').extract(),
                        response.css('td:nth-child(4)::text').extract(),
                        response.css('td:nth-child(5)::text').extract()):
                    yield { 'counter_week': self.getCounterWeeks(),
                            'chart_week': page_chart_week, 
                            'chart_pos': chart_pos, 
                            'track': track, 
                            'artist': artist,
                            'artist_num': re.sub('/.*', '', re.sub('/artist/', '', artist_num)),
                            'label': label, 
                            'last_week': re.findall(r'\d+|$', lastweek)[0],
                            'peak_pos': re.findall(r'\d+|$', peak_pos)[0],
                            'weeks_on_chart': re.findall(r'\d+|$', weeks_on_chart)[0]}  

                # navigate to the next page
                if (self.navigation_mode == self.NAVIGATION_MODE_PREVIOUS):
                    for next_page in response.css('.charts-header-panel:nth-child(1) .chart-date-directions'):
                        if next_page.css("a::text").extract_first() == self.NAVIGATION_MODE_PREVIOUS:
                            yield response.follow(next_page, self.parse)
                elif (self.navigation_mode == self.NAVIGATION_MODE_NEXT):
                    for next_page in response.css('.charts-header-panel:nth-child(1) .chart-date-directions'):
                        if next_page.css("a::text").extract_first() == self.NAVIGATION_MODE_NEXT:
                            yield response.follow(next_page, self.parse)
                else:
                    self.logger.critical('Navigation mode is not defined: ', self.navigation_mode)  
            else:
                # outside of allowed date range
                self.logger.info('%s is outside of the allowed date range', page_chart_week)
                self.__counter_out_of_range += 1
                self.__counter_of_weeks-=1 

                if (self.__counter_out_of_range <= 1):
                    # navigate to the next page
                    if (self.navigation_mode == self.NAVIGATION_MODE_PREVIOUS):
                        for next_page in response.css('.charts-header-panel:nth-child(1) .chart-date-directions'):
                            if next_page.css("a::text").extract_first() == self.NAVIGATION_MODE_PREVIOUS:
                                yield response.follow(next_page, self.parse)
                    elif (self.navigation_mode == self.NAVIGATION_MODE_NEXT):
                        for next_page in response.css('.charts-header-panel:nth-child(1) .chart-date-directions'):
                            if next_page.css("a::text").extract_first() == self.NAVIGATION_MODE_NEXT:
                                yield response.follow(next_page, self.parse)
                    else:
                        self.logger.critical('Navigation mode is not defined: ', self.navigation_mode)  
                else:
                    self.logger.info('Exit due out of date range')
        except Exception as ex:
            self.logger.critical('Unexpected error during parsing: ', ex.__class__)
        finally:
            pass


class ChartScan(object):
    
    def __init__(self):
        pass

    def scanByYear(self, year):
        try:
            # setting up the crawler process
            feedURI = 'Dataset/OfficialUKCharts' + str(year) +'.json'

            process = CrawlerProcess({
             'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
             'FEED_FORMAT': 'json',
             'FEED_URI': feedURI
            })
            
            # minimising the information presented on the scrapy log
            logging.getLogger('scrapy').setLevel(logging.WARNING)            

            process.crawl(OfficialUKChartsSpider, 
                            enforceDateRange = True,
                            startYear = year, 
                            endYear = year)

            print("** Spider: start for year of "+ str(year))
            process.start() # call spider and block here until is complete
            print("** Spider: finish for year of "+ str(year))
        except Exception as e:
            logging.error("** Error: %s" % e) 
        finally:
            process.stop()
            logging.info("** Finished Spider process ***")
            print("*"*80)
            print("{0:<40s}".format("* End - Charts Spider"))


# The main program starts here
def main():
    #clean the console
    os.system('cls')
    
    #display a small header
    print("*"*80)
    print("{0:<40s}{1:>40s}".format("* Charts Spider", "Daniel Pereira (10391381@mydbs.ie) *"))
    print("*"*80)



## initial load code
## calling a function for the main minimise the code it loads in the entry point
if __name__ == '__main__':
    main()