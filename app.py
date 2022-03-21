from bs4 import BeautifulSoup
import requests

product_id = "99105003"

def get_product_url(product_id):
    return "https://www.ceneo.pl/"+ product_id + "#tab=reviews" 
    


page_html = requests.get(get_product_url(product_id))


soup = BeautifulSoup(page_html.text, 'lxml')


user_reviews = soup.find_all("div", class_="user-post__content")


for review in user_reviews:
    print(review.text)


