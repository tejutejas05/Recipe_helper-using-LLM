from bs4 import BeautifulSoup
import requests

def search_recipe(dish_name):

    query = dish_name.replace(" ","+")

    url = f"https://www.allrecipes.com/search?q={query}"

    headers = {
        'User-Agent':'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    link = soup.select_one("a[href*='/recipe/']")

    if link:
        return link["href"]
    
    return None


#git is changed
