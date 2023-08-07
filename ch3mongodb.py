from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.dbjungle


def inser_all():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        "https://movie.daum.net/ranking/boxoffice/yearly?date=2022", headers)
    soup = BeautifulSoup(data.text, "html.parser")

    movies = soup.select(".list_movieranking > li")
    for movie in movies:
        movie_info = movie.select_one(".thumb_cont")
        if not movie_info:
            continue
        title = movie_info.select_one("strong > .link_txt").text
        views_info = movie_info.select_one(
            ".txt_info > .info_txt:nth-child(2)").findChild(string=True, recursive=False)
        views = "".join([c for c in views_info if c.isdigit()])
        release_date = movie_info.select_one(
            ".txt_info > .info_txt:nth-child(1) > .txt_num").text
        (release_year, release_month, release_day) = [
            int(c) for c in release_date.split(".")]
        movie_data = {
            "title": title,
            "views": views,
            "open_year": release_year + 2000,
            "open_month": release_month,
            "open_day": release_day,
        }
        db.movies.insert_one(movie_data)


if __name__ == "__main__":
    db.movies.drop()
    inser_all()
