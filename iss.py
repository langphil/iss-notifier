from scraper import *


# Loop for times of ISS passes and compare to current time
def issCheck():
    for i in column.keys():
        for x in column[i]:
            if i == 'Date':
                issNow = x
                if issNow == timeNow:
                    print 'ISS will pass overhead in 5 minutes'
                    # Add notification function here
                else:
                    print'Not quite yet'
                    # Add timeout and pass to while loop


while True:
    issCheck()
    time.sleep(10)
