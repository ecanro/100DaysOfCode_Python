from bs4 import BeautifulSoup
import requests

URL= "https://www.afi.com/afis-100-years-100-movies/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language": "es,pt;q=0.9,es-ES;q=0.8,en;q=0.7"
}

response = requests.get(url=URL, headers=header)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
print(soup.prettify())

movie = soup.find(name="h6", class_="q_title")
movie_name = movie.getText
print(movie_name)

all_movies = soup.find_all(name="h6", class_="q_title")[:100]
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as list:
    for movie in movies:
        #print(movie.getText())
        list.write(f"{movie}\n")

