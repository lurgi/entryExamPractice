from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

movie = db.movies.find_one({"title": "미니언즈2"})
movies_same_month = list(db.movies.find({"open_month": movie["open_month"]}))
for movie in movies_same_month:
    print(movie["title"])

db.movies.update_one({"title": "헌트"}, {"$set": {"open_year": 1999}})
hunt = db.movies.find_one({"title": "헌트"})
print(hunt)
