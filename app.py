# Flask Dashboard setup

from flask import Flask,render_template
from scraper import scrape_quotes, quotes_to_df

app = Flask(__name__) # tells FLASK to create the app - object - so it knows where to find the templates, static files,etc.

""" @app.route("/")
def hello():
    return "Hello, World!" """

@app.route("/")
def dashboard():
    quotes = scrape_quotes(limit=6) 
    df =quotes_to_df(quotes)
    #return "Hello World!"
    return render_template("dashboard.html",tables=[df.to_html (classes='data')],titles=df.columns.values)
    # converts the Dataframe DF into an html table
    # jinja2 -> flask template engine. it is what we use to work with python code inside the html
    # enhacenemnts - add more decorators like /about and put your description

""" @app.route("/about")
def about():
    # put your code here """

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5500, debug=True) # use 5000 as port in your deployment unless you have anything running on that port.
    #0.0.0.0 --> instead of localhost we are giving comp localnetwork

    