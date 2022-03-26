from bs4 import BeautifulSoup
import requests


class Scraper:

    def __init__(self, product_id):
        self.product_id = product_id


    def get_product_url(self):
        return "https://www.ceneo.pl/" + self.product_id + "#tab=reviews"


    def get_all_opinions(self):
        page_html = requests.get(self.get_product_url())
        soup = BeautifulSoup(page_html.text, 'html.parser')
        user_reviews = soup.find_all("div", class_="user-post__body")
        reviews = self.remove_non_opinions(user_reviews)
        if len(reviews) == 0:
            raise Exception("No reviews found")
        return reviews


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

        review_details["props"] = None
        review_details["cons"] = None
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
