from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

print(soup.findAll(name="a"))
print(soup.findAll(name="li"))
all_type_tags = soup.findAll(name="a")
for tag in all_type_tags:
    print(tag.getText())
    print(tag.get("href"))
heading = soup.find(name="h1", id="name")
# ->heading = soup.find(id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
# ->section_heading = soup.find(class_="heading")
print(section_heading)
print(section_heading.name)
print(section_heading.getText())
print(section_heading.get("class"))

# select the first tag, or class or id
company_url = soup.select_one(selector="p a")
company_url2 = soup.select_one(selector=".heading")
print(company_url)
