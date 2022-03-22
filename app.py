from scraper import Scraper
import json

product_id = "103735237"
ceneo_scraper = Scraper(product_id)
product_reviews = ceneo_scraper.get_all_opinions()
