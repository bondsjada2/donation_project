# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from datetime import datetime
# import model
# from model import address
# from model import donation
# print(donate)

import os 

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time = datetime.now())

@app.route('/why')
def why():
    return render_template('why.html', time = datetime.now())

@app.route('/results', methods = ['GET', 'POST'])
def zip_code():
    if request.method == "POST":
        zipcode = request.form["zipcode"]
        print(zipcode)
        # zip_code = address(zipcode)
        print(zip_code)
        # good_will = donation(center)
        # print(good_will)
        if int(zipcode) == 10456:
            return render_template('results.html', zipcode = 10456, time = datetime.now())
        if int(zipcode) == 29440:
            return render_template('jada.html', zipcode = 29440, time = datetime.now())
        if int(zipcode) == 10021:
            return render_template('youshra.html', zipcode = 10021, time = datetime.now())
        if int(zipcode) == 11101:
            return render_template('island.html', zipcode = 11101, time = datetime.now())
        if int(zipcode) == 11237:
            return render_template('brook.html', zipcode = 11237, time = datetime.now())
        else:
            return render_template('soon.html', time = datetime.now())    
    else:
        return "ERROR"
