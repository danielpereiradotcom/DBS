"""Continuous Assessment
Dublin Business School
B8IT105 Programming for Big Data (B8IT105_1819_TME1S)
Lecturer: Darren Redmond
Student: Daniel Pereira (10391381@mydbs.ie)
________________________________________________________________________________

CA4 - Analysis of Control Log

This is the main file to run the analysis
"""
##################################################

import operator

def readFile(filename):
    '''
    This function open a file, break by line by 'r' and strip to remove the blanks
    '''
    data = [line.strip() for line in open(filename, 'r')]
    return data

def getCommits(data):
    '''
    This function clean the commit data and return an array with attributes and values
    ''' 
    sep = 72*'-'
    listOfCommits = []
    
    index = 0   
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            # based on example file each column is separated by pipe bar |. Split returns a list
            details = data[index + 1].split('|')

            commit = {  'revision': details[0].strip(),
                        'author': details[1].strip(),
                        'date_full': details[2].strip(),
                        'date': details[2].strip().split(' ')[0],
                        'time': details[2].strip().split(' ')[1],
                        'dayofweek': details[2].strip().split(' ')[3].lstrip('('),
                        'month': details[2].strip().split(' ')[5].strip(),
                        'year': details[2].strip().split(' ')[6].rstrip(')'),
                        'number_of_lines': details[3].strip().split(' ')[0]
                    }
            # add details to the list of commits.
            listOfCommits.append(commit)
            
            # move to next line
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return listOfCommits

def getAuthors(commitsList):
    '''
    This function return a list of authors and their commits
    '''
    authorsList = {}
    for commit in commitsList:
        author = commit['author']
        line = int(commit['number_of_lines'])
        if author not in authorsList:
            authorsList[author] = {'author':author, 'commits':1, 'lines':line}
        else:
            total_commits = authorsList[author]['commits']
            total_lines = authorsList[author]['lines']
            authorsList[author] = {'author':author, 'commits':total_commits + 1, 'lines':total_lines + line}
    return authorsList

def getMonths(commitsList):
    '''
    This function return a list of months and their totals
    '''
    # Working with months
    monthsList = {}
    for commit in commitsList:
        #month
        month = commit['month']
        if month not in monthsList:
            monthsList[month] = 1
        else:
            monthsList[month] = monthsList[month] +1
    # To help, just sort the lists in reverse mode
    monthsList = sorted(monthsList.items(), key=operator.itemgetter(1), reverse=True)
    return monthsList

def getDates(commitsList):
    '''
    This function return a list of dates and their totals
    '''
    # Working with dates
    datesList = {}
    for commit in commitsList:
        #dates
        date = commit['date']
        if date not in datesList:
            datesList[date] = 1
        else:
            datesList[date] = datesList[date] +1
    # To help, just sort the lists in reverse mode
    datesList = sorted(datesList.items(), key=operator.itemgetter(1), reverse=True)
    return datesList


def getTimes(commitsList):
    '''
    This function return a list of times and their totals
    '''
    # Working with times
    timesList = {}
    for commit in commitsList:
        #times
        time = commit['time']
        if time not in timesList:
            timesList[time] = 1
        else:
            timesList[time] = timesList[time] +1
    # To help, just sort the lists in reverse mode
    timesList = sorted(timesList.items(), key=operator.itemgetter(1), reverse=True)
    return timesList



# The main program starts here
if __name__ == '__main__':

    # open the file - and read all of the lines.
    log_filename = 'changes_python.log'
    log_data = readFile(log_filename)
    
    # get a list of commits    
    commitsList = getCommits(log_data)

    # The first thing is to make sure we have a clean data e found the population to work
    # How many commits
    print("(1) ===> Total number of commits: ", len(commitsList))
    # ==> result is 422


    ##################################################
    # Analise of authors
    # How many authors?
    authorsList = getAuthors(commitsList)
    print("(2) ===> Total number of unique authors: ", len(authorsList))
    # ==> 10

    # Getting some numbers from the authors list
    # Because authorsList is not sortable, we need to use a function from operator library to sort the list in reverse mode
    # cannot be done straight because it is a dictionary
    # the solution is get only the author and commit numbers and then sort it
    canSortList = {}
    for author in authorsList:        
        total_commits = authorsList[author]['commits']
        canSortList[author] = total_commits
    sortedList = sorted(canSortList.items(), key=operator.itemgetter(1), reverse=True) 

    # with the sorted list we need to bring the other attributes from author
    authorsListSorted = {}
    for item in range(len(sortedList)):
        authorsListSorted[item] = authorsList[sortedList[item][0]]


    # List authors, commits and lines changed
    print('(3) ====> List authors, commits and lines changed')
    for item in authorsListSorted:
        print(authorsListSorted[item]['author'],"has commited", authorsListSorted[item]['commits'], "and changed ", authorsListSorted[item]['lines'], "lines")

    # Finding the top and lowest committers
    # with the list sorted, just get the top and low elements
    commiterTop = authorsListSorted[0]
    commiterLowest = authorsListSorted[len(authorsListSorted)-1]
    print("(4) ===> Top commiter is ", commiterTop['author']) #Thomas
    print("(5) ===> Lowest commiter: ", commiterLowest['author']) # murari.krishnan

    # Analysing the top commiter, how many commits? 
    print("(6) ===> The top commiter ", commiterTop['author'],"has commited", commiterTop['commits'], "times")


    ##################################################
    # Analysing the dates   
    # Working with months
    monthsList = getMonths(commitsList)
    datesList = getDates(commitsList)
    timesList = getTimes(commitsList)
   
    
    # Print all months and the total
    print("(7) ===> List of months and totals")
    for month in monthsList:
        print("         ",month[0],"=",month[1],"commits")

    # Print all dates and the total
    print("(8) ===> List of dates and totals")
    for date in datesList:
        print("         ",date[0],"=",date[1],"commits")

    # Print all times and the total
    print("(9) ===> List of times and totals")
    for time in timesList:
        print("         ",time[0],"=",time[1],"commits")


    #the top dates
    print("(10) ====> The top month is:", monthsList[0][0]," with", monthsList[0][1]," commits")
    print("(11) ====> The top date is:", datesList[0][0]," with", datesList[0][1]," commits")

    # we cannot say there is a top time of the day because there are duplicates commits totals
    print("(12) ====> The top times are:")
    for time in timesList:
        if time[1] == timesList[0][1]:
            print("          ", time[0],"with", time[1],"commits")

    print("total of dates", len(datesList))
    print("total of times", len(timesList))
    