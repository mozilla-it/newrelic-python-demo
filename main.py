#!/usr/bin/python3

from flask import Flask
from multiprocessing import Pool
from multiprocessing import cpu_count

app = Flask(__name__)

@app.route("/")
def hello():
    return "This is a dumb flask app"

@app.route("/work")
def work():
    from math import factorial
    x = [ factorial(n) for n in range(1024) ]
    return str(x[-1])
