from scraper import Scraper

product_id = "103735237"
ceneo_scraper = Scraper(product_id)
product_reviews = ceneo_scraper.get_all_opinion()
print(product_reviews)

# todo recomendation with status  "Nie polecam" are not included in the result it must be fixed
