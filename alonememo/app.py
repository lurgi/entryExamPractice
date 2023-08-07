
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.jungle
from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/memo",methods = ["POST"])
def memo():
    return "success"

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)