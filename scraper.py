from bs4 import BeautifulSoup
import requests
import math

class Scraper:

    def __init__(self, product_id):
        self.product_id = product_id
        self.page_html = requests.get(self.get_product_url())
        self.soup =  BeautifulSoup(self.page_html.text, 'html.parser')

    def get_product_url(self):
        return "https://www.ceneo.pl/" + self.product_id + "#tab=reviews"

    def get_product_name(self):
        return get_value_for_element(self.soup, "h1", "product-top__product-info__name") or "Nie udało się pobrać nazwy produktu"


    def get_all_opinions(self):
        elements = self.soup.find_all("span", class_="page-tab__title js_prevent-middle-button-click")
        if(len(elements) == 0):
            raise Exception("Enter correct product id")

        num_of_opinions = elements[2].text or "0"
        try:  
            num_of_opinions = int(num_of_opinions.replace("Opinie i Recenzje (", "").replace(")", ""))
        except:
            raise Exception("This Product has no opinions")
        
        page_num = 1
        if num_of_opinions > 300:
            raise Exception("This Product has more than 100 opinions, enter a different product id")
    
        all_pages = math.ceil(num_of_opinions / 10) 
        
        all_reviews = []

        while page_num <= all_pages:
            page_html = requests.get('https://www.ceneo.pl/'+ self.product_id +'/opinie-' + str(page_num))
            soup = BeautifulSoup(page_html.text, 'html.parser')
            user_reviews = soup.find_all("div", class_="user-post__body")
            reviews = self.remove_non_opinions(user_reviews)
            all_reviews.extend(reviews)
            page_num += 1

       
        if len(all_reviews) == 0:
            raise Exception("No reviews found enter a different product id")
        return all_reviews


    def remove_non_opinions(self, user_reviews):
        reviews = []
        for review in user_reviews:
            review_details = self.get_review_details(review)
            if review_details["author"] is None or review_details[
                    "score"] is None:
                continue
            reviews.append(review_details)
        return reviews


    def get_review_details(self, review):
        review_details = {}
        review_details["author"] = get_value_for_element(
            review, "span", "user-post__author-name")
        review_details["comment_date"] = get_review_data(review)
        review_details["purchase_date"] = get_purhase_date(review) or "Brak"
        review_details["opinion"] = get_value_for_element(
            review, "div", "user-post__text")
        review_details["recomendation"] = get_value_for_element(
            review, "em", "recommended") or "Nie polecam"
        review_details["score"] = get_value_for_element(
            review, "span", "user-post__score-count")

        like_button = review.find("button", class_="js_vote-yes")
        if like_button is not None:
            review_details["likes"] = like_button.find("span").text

        dislike_button = review.find("button", class_="js_vote-no")
        if dislike_button is not None:
            review_details["dislikes"] = dislike_button.find("span").text

        review_details["props"] = 0
        review_details["cons"] = 0
        features = review.find_all("div", class_="review-feature__col")

        if (len(features) > 0):
            childrens_props = features[0].findChildren("div", recursive=False)
            review_details["props"] = len(childrens_props) - 1
        if (len(features) > 1):
            childrens_cons = features[1].findChildren("div", recursive=False)
            review_details["cons"] = len(childrens_cons) - 1

        return review_details


def get_value_for_element(review, tag, attribute):
    elemnet = review.find(tag, class_=attribute)
    if elemnet is None or elemnet.text is None:
        return None
    return elemnet.text.replace("\n", " ")


def get_size_of_element(review, tag, attribute):
    elemnet = review.find_all(tag, class_=attribute)
    if elemnet is not None:
        return len(elemnet.text)
    return 0


def get_review_data(review):
    elements = review.find_all("time")
    if len(elements) == 0:
        return None
    return elements[0].get('datetime')



def get_purhase_date(review):
    elements = review.find_all("time")
    if len(elements) < 2:
        return None
    return review.find_all("time")[1].get('datetime')
