from flask import Blueprint, render_template, request
from .myFunctions import getData, dbFile

views = Blueprint('views', __name__)

@views.route('/')
def home():
    data = getData(dbFile)
    return render_template('index.html', jsonData=data)

@views.route('/newchart', methods = ['POST'])
def newchart():
    data = getData(dbFile, request.form['sd'], request.form['ed'])
    return render_template('index.html', jsonData=data)