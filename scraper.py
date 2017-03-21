import requests
import pandas as pd
from bs4 import BeautifulSoup


# Get HTML
result = requests.get('https://spotthestation.nasa.gov/sightings/view.cfm?country=United_Kingdom&region=England&city=London')
content = result.content
# print result.status_code


# Beautiful Soupify
soup = BeautifulSoup(content, 'lxml')
table = soup.find('table')
# print table


# Create dictionaries
issDate = []
issDuration = []
issAppears = []

# Loop and populates dictionaries
for row in table.find_all('tr')[1:]:
    col = row.find_all('td')

    # ISS overhead date
    date = col[0].string.strip()
    issDate.append(date)

    # ISS overhead duration
    duration = col[1].string.strip()
    issDuration.append(duration)

    # ISS overhead location
    location = col[3].string.strip()
    issAppears.append(location)


# Strucure the data
column = {'Date': issDate, 'Duration': issDuration, 'Appearance': issAppears}
df = pd.DataFrame(column)
