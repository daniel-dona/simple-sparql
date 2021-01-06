#!/usr/bin/env python3

import json
import rdflib
from flask import Flask, send_file, jsonify, Response
from flask_restful import Resource, Api, reqparse

g = rdflib.Graph()

g.load("/data/data.nt", format='nt')

parser = reqparse.RequestParser()
parser.add_argument('query')

app = Flask(__name__)
api = Api(app)

API_URL = "/sparql"

class SPARQL(Resource):
    def get(self):
        data = parser.parse_args()
        print(data)
        q = g.query(data['query'])
        print(len(q))
        out = json.dumps(json.loads(q.serialize(format='json').decode()))
        return Response(out, mimetype='application/sparql-results+json')

api.add_resource(SPARQL, API_URL)

app.run(debug=False, host="0.0.0.0", port=5001, threaded=False, processes=5)




