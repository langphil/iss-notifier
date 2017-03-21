import time
import datetime
from pushover import init, Client
from scraper import *
from config import *

# Get the current time
timeNow = time.strftime("%a %b %d, %I:%M %p").lstrip("0").replace(" 0", " ")

# Initialise Pushover for notifications
client = Client(user_key, api_token=api_token)


# Loop for times of ISS passes and compare to current time
def issCheck():
    for i in column.keys():
        for x in column[i]:
            if i == 'Date':
                issNow = x
                if issNow == timeNow:
                    client.send_message("ISS is over London: " + x, title="ISS")
                else:
                    break


while True:
    issCheck()
    time.sleep(10)
