
from elasticsearch import Elasticsearch
import requests
import json
from flask import Flask,render_template
from flask import request
import ast

from sys import getsizeof
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
r = requests.get('http://localhost:9200')
full_data=[]
text_list=[]

if not es.indices.exists(index="scraped_data"):

    with open("..\\tutorial\stories_data.json","r") as json_file:
        stories=json.load(json_file)
        i=1
        for story in stories:
            es.index(index='scraped_data', doc_type='stories', id=i, body=story)
            i=i+1


#     a=es.get(index='scraped_data',doc_type='stories',id=i)


print(es.search(index="scraped_data", body={"from":0,"size":30,"query": {"match_all": {}}}))
# # print(json.dumps(stories))
# stories=stories1["hits"]["hits"]
# print(stories)

def getAllStories():
    stories1 = es.search(index="scraped_data", body={"from": 0, "size": 30, "query": {"match_all": {}}})
    # print(json.dumps(stories))
    all_stories = stories1["hits"]["hits"]
    return all_stories
def getStoryByKeyWord(key_word):

    # print(json.dumps(stories))
    # print(stories1)
    # stories2=es.search(index="scraped_data", body={"from": 0, "size": 30, "query": {"match": {"page_title":key_word}}})
    # if stories2["hits"]["total"]>0:
    #
    #     stories1=es.search(index="scraped_data", body={"from": 0, "size": 30, "query": {"query_string": {"query":key_word}}})
    # else:
    stories1 = es.search(index="scraped_data",
                             body={"from": 0, "size": 100, "query": {"query_string": {"query": key_word}}})
    stories_by_keyword = stories1["hits"]["hits"]
    return stories_by_keyword

def getStoryByUrl(url):
    stories1 = es.search(index="scraped_data",
                         body={"from": 0, "size": 100, "query": {"match_phrase": {"link": url}}})
    stories_by_url = stories1["hits"]["hits"]
    return stories_by_url

# print(getStoryByKeyWord("bharti"))
app = Flask(__name__)



@app.route("/")
def home():
    #pass
    return render_template('home.html',stories=getAllStories())

@app.route("/search",methods=['GET'])
def search():
    list_of_text=[]
    text_list=[]
    #stories=getStoryByKeyWord(key_word)
    key_word=request.args.get('keyword')
    print((key_word))
    if not key_word.startswith("https"):
        stories=getStoryByKeyWord(key_word)
        print(stories)
        i=0
        while i<len(stories):
            text_list.append(ast.literal_eval(stories[i]["_source"]["text"]))
            i=i+1
        list_of_text=text_list
        print("hi",(list_of_text))
        return render_template('search.html',stories=stories,keyword=key_word,text_list=list_of_text)
    else:
        stories=getStoryByUrl(key_word)
        print("Hello",stories)
        return render_template('search.html',stories=stories,keyword=key_word,text_list=[])

if __name__ == "__main__":
    app.run(debug=True)