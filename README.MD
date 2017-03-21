# iss-notifier

## What is this?
A scraper that grabs data on when the International Space Station will pass over London [from this source](https://spotthestation.nasa.gov/sightings/view.cfm?country=United_Kingdom&region=England&city=London).
A script that will compare this data against the current time and notify when a pass is due to happen.
I'd like to explore how this information can be conveyed in a passive way, that is not intrusive.


## Installation
* `git clone git@github.com:langphil/iss-notifier.git`
* `cd iss-notifier`
* Install libraries listed below
* Get a [Pushover](https://pushover.net) account for notifications to your phone.
* Create variables for your Pushover 'user_key' & 'api_token' in a new file 'config.py'
* Install the Pushover app on your phone
* Run `python iss.py`


## Libraries
* Beautiful Soup 4
$ `pip install beautifulsoup4`

* Requests
$ `pip install requests`

* pandas
$ `pip install pandas`

* Pushover
$ `pip install python-pushover`


## ToDo
* [x] Initially build a mobile phone notification
* [ ] Mobile notifications only to happen between the hours of 19:00 - 23:00
* [ ] Consider how notifications happen - look at raspberrypi and motor device
* [ ] Remove time of ISS pass from the dictionary once it has happened
* [ ] Subtract 10 minutes from the pass time for when notifications happen
* [ ] Write proper Documentation
