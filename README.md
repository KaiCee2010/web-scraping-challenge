# Web Scraping Challenge

During this homework assignment, a jupyter notebook, python scripts and flask app were created.

## Jupyter Notebook
A jupyter notebook was created to contain code to scrape websites using splinter and BeautifulSoup.

The jupyter notebook contains four parts:
* NASA Mars News
    * Gather the latest news title and teaser
* JPL Mars Space Images - Featured Image
    * Gather the featured Mars image from the JPL space images site
* Mars Facts
    * Gather the table of Mars facts from the space facts site
* Mars Hemispheres
    * Gather the names and image urls from the USGS astrogeology site


## App.py
The app.py is a Flask app.  The Flask app performs the following functions:
* Calls scrape function from scrape_mars.py and returns mars_data dictionary
* Updates the mars_app (mongo database) with the mars_data dictionary
* Updates the HTML template with data from the mars_app

## Scrape_Mars.py
The scrape_mars.py is basically a copy of the jupyter notebook.  The code is formatted to work in a function in a standalone script.  All variables created are added to a python dictionary called mars_data. The mars_data dictionary is returned to the app.py script.

## Index.html
The index.html is a template for the flask app.  It contains formatting and loads the data from the mongodb into a particular format.

