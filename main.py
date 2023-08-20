import requests
from bs4 import BeautifulSoup


URL = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"


response = requests.get(URL)
website_html = response.content


soup = BeautifulSoup(website_html, "html.parser")

all_books = soup.find_all(name="h3")
book_titles = []
for book in all_books:
    book_titles.append(book.getText())


with open("books.txt", mode="w") as file:
    for book in book_titles:
        file.write(f"{book}\n")
