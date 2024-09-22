from bs4 import BeautifulSoup
import requests
from hydra import initialize, compose
import re

with initialize(version_base=None, config_path="conf"):
    cfg = compose(config_name="config")


def get_list_title_from_url(url):
    titles = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    soup = soup.find_all(class_='wikitable')[0]
    soup = soup.find_all(["tr"])
    for row in soup[1:]:
        title, article_type = row.find_all("td")[1: 3]
        article_type = article_type.select("img")[0].parent.get("title")
        title = title.text
        if article_type != "List-Class article":
            titles.append(title)
    return titles


def scrape_articles(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    soup = soup.find_all("p")
    articles = []
    for article in soup[1:]:
        article = article.text.strip()
        article = re.sub("\[[0-9]+\]", '', article)  # noqa
        print(article)
        articles.append(article)
    return articles


if __name__ == "__main__":
    titles = get_list_title_from_url(cfg["scrape"]["link1"])
    titles.extend(get_list_title_from_url(cfg["scrape"]["link2"]))
    titles = list(dict.fromkeys(titles))
    for index in range(len(titles)):
        title = titles[index].replace("\n", "").replace(" ", "_")
        url = "https://en.wikipedia.org/wiki/" + title
        with open(f"data/{index + 1} - {titles[index]}.txt", mode="a") as f:
            for article in scrape_articles(url):
                f.write(article)
