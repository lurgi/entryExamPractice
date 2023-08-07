import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    "https://movie.daum.net/ranking/boxoffice/yearly?date=2022", headers)
soup = BeautifulSoup(data.text, "html.parser")

movies = soup.select(
    ".list_movieranking > li > .item_poster")
for movie in movies:
    link = movie.select_one('.thumb_item > .poster_info > a').text
    title = movie.select_one('.thumb_cont > strong > a').text
    releaseDay = movie.select_one(
        '.thumb_cont > .txt_info > .info_txt:nth-child(1) > .txt_num').text
    views = movie.select_one(
        '.thumb_cont > .txt_info > .info_txt:nth-child(2)').text
    print(title, releaseDay, views)
