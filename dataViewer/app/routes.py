from flask import render_template, redirect, request
from app import app
from app import mlSandbox
import matplotlib.pyplot as plt

covid_data = None
countryList = None
countriesToDisplay = None
@app.route('/')
def root():
    return "Hello, World!"

@app.route('/index', methods = ["GET", "POST"])
def index():
    global covid_data
    global countryList
    if covid_data is None:
        covid_data = mlSandbox.getCovidData()
        countryList = list(set(covid_data.index.values))
        countryList.sort()

        plt.plot([1, 2], [4, 5], 'ro')
        plt.show()

    if request.method == "POST":
        countryPick = request.form['country']
        return render_template("dataViewer.html", title = "Covid Data Plotter", countryList = countryList, countryPick = countryPick)

    return render_template('dataViewer.html', title = "Covid Data Plotter", countryList = countryList)

@app.route('/wiki')
def wiki():
    return redirect('https://ourworldindata.org/coronavirus-source-data')

@app.route('/index/<name>')
def printName(name):
    return name
