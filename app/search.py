import requests
from bs4 import BeautifulSoup


def search_recipe(dish_name):

    query = dish_name.replace(" ", "+")
    url = f"https://www.allrecipes.com/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all links
    links = soup.find_all("a", href=True)

    for link in links:
        href = link["href"]

        if "/recipe/" in href:
            return href

    return None

