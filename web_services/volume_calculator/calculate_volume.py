# Volume Calculator
# A Webservice to calculate the volume of shapes

from flask import Flask, json

app = Flask(__name__)

shapes = {
    'cube': 'V = S ** 3'
}