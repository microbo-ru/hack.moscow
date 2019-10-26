import pandas as pd
from flask import Flask, escape, request, Response
from flask_cors import CORS
import flask
import json
app = Flask(__name__)
CORS(app)


@app.route('/api/summary/2018')
def summ_2018():
    df = pd.read_csv(
        "./family_summary_data_2018.csv").drop(columns=["Unnamed: 0"]).to_dict()

    return Response(json.dumps(df), headers={"Content-type": "application/json"})


@app.route('/api/summary/2017')
def summ_2017():
    df = pd.read_csv(
        "./family_summary_data_2017.csv").drop(columns=["Unnamed: 0"]).to_dict()

    return Response(json.dumps(df), headers={"Content-type": "application/json"})
