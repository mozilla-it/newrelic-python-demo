#!/usr/bin/python3

from flask import Flask
from multiprocessing import Pool
from multiprocessing import cpu_count
import googlecloudprofiler

googlecloudprofiler.start(service='newrelic-python-demo',service_version='0.0.1',verbose=3)

app = Flask(__name__)

def f(l, i):
    l.acquire()
    print('worker ', i)
    x = 0
    while x < 1000:
        print(x)
        x += 1
    l.release()

@app.route("/")
def hello():
    return "This is a dumb flask app"

@app.route("/work")
def work():
    from math import factorial
    x = [ factorial(n) for n in range(1024) ]
    return str(x[-1])

@app.route("/more/work/<count>")
def morework(count):
    from multiprocessing import Process, Lock
    lock = Lock()
    for num in range(int(count)):
        Process(target=f, args=(lock, num)).start()
    return "ok."
