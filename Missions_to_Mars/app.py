from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# From the separate python file in this directory, we'll import the code that is used to scrape craigslist
import scrape_craigslist

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)