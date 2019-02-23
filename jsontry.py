
from elasticsearch import Elasticsearch
import requests
import json
from flask import Flask
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
r = requests.get('http://localhost:9200')
#
#
#
# if not es.indices.exists(index="scraped_data"):
#     with open("tutorial\stories_data.json","r") as json_file:
#         stories=json.load(json_file)
#         i=1
#         for story in stories:
#             es.index(index='scraped_data', doc_type='stories', id=i, body=story)
#             i=i+1
#
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello!"
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
#
#
#
#
#
# # print(es.get(index='scraped_data',doc_type='stories',id=26))
# print(json.dumps(es.search(index="scraped_data", body={"from": 0, "size": 30, "query": {"match_all": {}}})))
#



es.indices.delete(index='scraped_data')



