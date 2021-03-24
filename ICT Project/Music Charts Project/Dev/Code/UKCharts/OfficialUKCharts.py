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


class OfficialUKChartsSpider(scrapy.Spider):
    '''
    This class represents the Spider to UK Top 100 Charts
    '''
    # Spider attributes
    name            = "OfficialUKChartsSpiderSun" # crawler identifier
    start_urls      = ['https://www.officialcharts.com/charts/singles-chart'] # the initial url or the current url
    #start_urls      = ['https://www.officialcharts.com/charts/singles-chart/19521114/7501/'] # the last chart (or the first page)
    
    
    download_delay  = 1 # multi thread delay

    # custom attributes
    __counterWeeks = None
    __endChartDate = None
    __startChartDate = None
    
    # custom properties
    enforce_date_range = False



    # custom constructor
    def __init__(self):
        self.enforce_date_range = False
        self.setCounterWeeks(1) #just a simple counter 
        #self.setEndDate("")
        #self.setStartDate("")

    # custom setters
    def setCounterWeeks(self, c):
        '''
        Define the counter of weeks
        '''
        self.__counterWeeks = c

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
        return self.__counterWeeks

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
    def addCounterWeeks(self):
        '''
        Increase the number of weeks in 1
        Return the new counter of weeks
        '''
        self.__counterWeeks = self.__counterWeeks + 1
        return self.__counterWeeks

    # Overwrite Scrapy built in parse function
    def parse(self, response):
        '''
        This function is part of Scrapy library.
        It is trigged when the process calls the URL and need to parse the values into JSON (defined via settings)
        The objective is to find each html/css tag and extract the values of the chart
        In the end, the function looks for the next url, this is done via capturing the link on page for the 'previous' week.
        '''
        
        try:
            self.addCounterWeeks()

            # Recover the week date from html
            page_chart_week = re.sub(' -.*', '',
                                response.css('.article-heading+ .article-date::text').extract_first().strip())

            page_chart_week = dt.date(parser.parse(page_chart_week))
            self.logger.info('#%d (%s) - Scraping page: %s', self.getCounterWeeks(), page_chart_week, response.url)

            is_valid_page = False
            if (self.enforce_date_range):
                # Validate whether is on date range to extract information
                if (page_chart_week >= self.getStartDate() and page_chart_week <= self.getEndDate()):
                    is_valid_page = True
            else:
                is_valid_page = True

            if (is_valid_page):
                self.logger.info('** page is valid')
                # Extract each tag from html and parse into a variable
                for (artist, chart_pos, artist_num, track, label, lastweek, peak_pos, weeks_on_chart) in \
                    zip(response.css('#main .artist a::text').extract(),
                        response.css('.position::text').extract(),
                        response.css('#main .artist a::attr(href)').extract(),
                        response.css('.track .title a::text').extract(),
                        response.css('.label-cat .label::text').extract(),
                        response.css('.last-week::text').extract(),
                        response.css('td:nth-child(4)::text').extract(),
                        response.css('td:nth-child(5)::text').extract()):
                    yield { 'counter_week': self.getCounterWeeks(),
                            'chart_week': page_chart_week, 
                            'chart_pos': chart_pos, 
                            'track': track, 
                            'artist': artist,
                            'artist_num': re.sub('/.*', '', re.sub('/artist/', '', artist_num)),
                            'label': label, 
                            'last_week': re.findall('\d+|$', lastweek)[0],
                            'peak_pos': re.findall('\d+|$', peak_pos)[0],
                            'weeks_on_chart': re.findall('\d+|$', weeks_on_chart)[0]}  
            else:
                # outside of allowed date range
                self.logger.info('%s is outside of the allowed date range', page_chart_week)


            # Look for next page and call the process (if it exists)
            for next_page in response.css('.charts-header-panel:nth-child(1) .chart-date-directions'):
                if next_page.css("a::text").extract_first() == 'next':
                    yield response.follow(next_page, self.parse)              
        except Exception as ex:
            self.logger.critical('Unexpected error during parsing: ', ex.__class__)
        finally:
            pass
    

# The main program starts here
def main():
    #clean the console
    os.system('cls')
    
    #display a small header
    print("*"*80)
    print("{0:<40s}{1:>40s}".format("* Official UK Top 100 Singles Charts Spider", "Daniel Pereira (10391381@mydbs.ie) *"))
    print("*"*80)

    try:
        # setting up the crawler process
        process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'Dataset/OfficialUKCharts.json'
        })
        
        # minimising the information presented on the scrapy log
        logging.getLogger('scrapy').setLevel(logging.WARNING)
        process.crawl(OfficialUKChartsSpider)
        print("** Spider: start **")
        process.start() # call spider and block here until is complete
        print("** Spider: finish **")
    except Exception as e:
        logging.error("** Error: %s" % e) 
    finally:
        process.stop()
        logging.info("** Finished Spider process ***")

    print("*"*80)
    print("{0:<40s}".format("* End - Official UK Top 100 Singles Charts Spider"))


## initial load code
## calling a function for the main minimise the code it loads in the entry point
if __name__ == '__main__':
    main()