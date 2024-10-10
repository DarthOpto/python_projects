from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
# print(article_upvotes)
# print(article_texts)




