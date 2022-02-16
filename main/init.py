#!/usr/bin/env python3

import json
import rdflib
from flask import Flask, send_file, jsonify, Response
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import traceback

g = rdflib.Graph()

g.load("/data/data.nt", format='n3')

for t in g:
	print(t)

parser = reqparse.RequestParser()
parser.add_argument('query')

app = Flask(__name__)
api = Api(app)
CORS(app)

API_URL = "/sparql"

class SPARQL(Resource):
	
	def get(self):
		
		data = parser.parse_args()
		print(data)
		out="{}"
		
		if 'query' in data and data['query'] != None:
			
			q = g.query(data['query'])
			out = json.dumps(json.loads(q.serialize(format='json').decode()))
			
		return Response(out, mimetype='application/sparql-results+json')
		
	def post(self):
		
		data = parser.parse_args()
		print(data)
		out="{}"
		
		if 'query' in data and data['query'] != None:
			
			query = data['query'].replace("\n", "")
			
			print("Query: ", query)
			
			try:
				res = g.query(query)
				out = json.dumps(json.loads(res.serialize(format='json').decode()))
			except:
				print("Oops")
				print(traceback.format_exc())
		
		return Response(out, mimetype='application/sparql-results+json')

api.add_resource(SPARQL, API_URL)

app.run(debug=False, host="0.0.0.0", port=5001, threaded=False, processes=5)




