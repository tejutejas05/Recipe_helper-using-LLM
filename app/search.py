import requests
from bs4 import BeautifulSoup


def search_recipe(dish_name):

    query = f"site:allrecipes.com {dish_name}"
    url = f"https://www.google.com/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    for link in soup.find_all("a"):

        href = link.get("href")

        if href and "allrecipes.com/recipe" in href:

            start = href.find("https://")
            end = href.find("&")

            return href[start:end]

    return None