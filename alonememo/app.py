
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.jungle
from flask import Flask, render_template, request, jsonify
app=Flask(__name__)
import requests
from bs4 import BeautifulSoup



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/memo",methods = ["POST"])
def postMemo():
    get_url = request.form['url']
    get_comment = request.form['comment']

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(get_url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    article_title = soup.select_one("meta[property='og:title']")['content']
    article_image = soup.select_one("meta[property='og:image']")['content']
    article_description = soup.select_one("meta[property='og:description']")['content']

    # db.articles.insert_one({})
    article = {
        "title" : article_title,
        "image_url" : article_image,
        "description" : article_description,
        "user_comment" : get_comment
    }
    db.articles.insert_one(article)
    return jsonify({'ok':True})

@app.route("/memo",methods=["GET"])
def getMemo():
    articles = list(db.articles.find({},{'_id':False}))
    return jsonify({'ok':True,"articles" : articles})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)