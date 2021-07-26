# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import model
from model import address
# from model import donation
# print(donate)
# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['GET', 'POST'])
def zip_code():
    if request.method == "POST":
        zipcode = request.form["zipcode"]
        print(zipcode)
        zip_code = address(zipcode)
        print(zip_code)
        # good_will = donation(center)
        # print(good_will)
        return render_template('results.html', zipcode = zipcode, zip_code = zip_code)
    else:
        return "ERROR"
