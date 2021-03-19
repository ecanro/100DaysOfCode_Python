from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get(url="https://news.ycombinator.com/news")
#print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())

##### only the first element find #####
article = soup.find(name="a", class_="storylink")
art_text = article.getText()
art_link = article.get("href")
art_points = soup.find(name="span", class_="score").getText()
# print(art_text)
# print(art_link)
# print(art_points)

articles = soup.findAll(name="a", class_="storylink")
article_text = []
article_link = []

for article in articles:
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_link.append(link)

article_score = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]
largest_points = max(article_score)
largest_index = article_score.index(largest_points)

print(article_text[largest_index])
print(article_link[largest_index])
print(largest_points)
