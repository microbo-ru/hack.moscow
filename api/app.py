import pandas as pd
from flask import Flask, escape, request, Response
from flask_cors import CORS
import flask
import json
app = Flask(__name__)
CORS(app)
df_2018 = pd.read_csv(
    "./family_summary_data_2018.csv").drop(columns=["Unnamed: 0"]).to_dict()
df_2017 = pd.read_csv(
    "./family_summary_data_2017.csv").drop(columns=["Unnamed: 0"]).to_dict()

with open("family_summ_with_reg.json", 'r') as f:
    df = json.load(f)


@app.route('/api/summary/2018')
def summ_2018():

    return Response(json.dumps(df_2018), headers={"Content-type": "application/json"})


@app.route('/api/summary/2017')
def summ_2017():

    return Response(json.dumps(df_2017), headers={"Content-type": "application/json"})


@app.route('/api/map')
def map():
    # ids = (71, 32283, 58550, 54746, 58951)
    ids = (54746, 58951)

    return Response(json.dumps([df[str(id)] for id in ids]), headers={"Content-type": "application/json"})


@app.route('/api/left/<id>')
def left(id):
    if id == 'undefined':
        id = 58550

    return Response(json.dumps(df[str(id)]), headers={"Content-type": "application/json"})


@app.route('/api/right/<id>')
def right(id):
    if id == 'undefined':
        id = 58951
    return Response(json.dumps(df[str(id)]), headers={"Content-type": "application/json"})


@app.route('/api/left=<id1>&right=<id2>')
def lr(id1, id2):
    return Response(json.dumps([df[str(id1)], df[str(id2)]]), headers={"Content-type": "application/json"})


@app.route('/api/nagl')
def nagl():
    ids = 32283
    return Response(json.dumps(df[str(ids)]), headers={"Content-type": "application/json"})
