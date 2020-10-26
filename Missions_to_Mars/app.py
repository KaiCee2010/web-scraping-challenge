from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# From the separate python file in this directory, we'll import the code that is used to scrape mars information
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"

mongo = PyMongo(app)

mars = mongo.db.mars
mars.drop()

@app.route('/')
def home():
    results = list(mars.find())
    return render_template('index.html', mars_results = results)


@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape()
    mars.insert_many(mars_data)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)