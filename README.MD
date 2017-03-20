# iss-notifier

## What is this?
A scraper that grabs data on when the International Space Station will pass over London [from this source](https://spotthestation.nasa.gov/sightings/view.cfm?country=United_Kingdom&region=England&city=London).
A script that will compare this data against the current time and notify when a pass is due to happen.
I'd like to explore how this information can be conveyed in a passive way, that is not intrusive.


## Installation
* `git clone git@github.com:langphil/iss-notifier.git`
* `cd iss-notifier`
* `python iss.py`


## Libraries
* Beautiful Soup 4
$ `pip install beautifulsoup4`

* Requests
$ `pip install requests`

* pandas
$ `pip install pandas`


## ToDo
* [ ] Consider how notifications happen - build
* [ ] Subtract 10 minutes from the pass time for when notifications happen
* [ ] Write proper Documentation
