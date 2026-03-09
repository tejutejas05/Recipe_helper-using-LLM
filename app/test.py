from recipe_scrapers import scrape_me

url = "https://www.allrecipes.com/recipe/16102/chicken-biryani/"

scraper = scrape_me(url)

recipe = {
    "name": scraper.title(),
    "ingredients": scraper.ingredients(),
    "instructions": scraper.instructions(),
    "servings": scraper.yields(),
    "total_time": scraper.total_time()
}

print(recipe)