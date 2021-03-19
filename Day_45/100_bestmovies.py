from bs4 import BeautifulSoup
import requests

URL= "https://www.afi.com/afis-100-years-100-movies/"

response = requests.get(url=URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
#print(soup.prettify())

movie = soup.find(name="h6", class_="q_title")
movie_name = movie.getText()
#print(movie_name)

all_movies = soup.find_all(name="h6", class_="q_title")[:100]
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as list:
    for movie in movies:
        #print(movie.getText())
        list.write(f"{movie}\n")

