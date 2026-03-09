from recipe_scrapers import scrape_me

urls = [
    "https://www.allrecipes.com/recipe/16102/chicken-biryani/",
    "https://www.allrecipes.com/recipe/46822/indian-chicken-curry/",
    "https://www.allrecipes.com/recipe/24706/gulab-jamun/"
]

recipes = []

for url in urls:

    scraper = scrape_me(url)

    recipe = {
        "name": scraper.title(),
        "ingredients": scraper.ingredients(),
        "instructions": scraper.instructions(),
        "servings": scraper.yields(),
        "total_time": scraper.total_time()
    }

    recipes.append(recipe)

print(recipes)