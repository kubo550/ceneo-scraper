from scraper import Scraper
from flask import Flask, render_template, request

product_id = "103735237"
ceneo_scraper = Scraper(product_id)
product_reviews = ceneo_scraper.get_all_opinions()

product_reviews_as_string = ""
for review in product_reviews:
    output = ""
    output += "Autor: " + review["author"] + "<br>"
    output += "Opinia: " + review["opinion"] + "<br>"
    output += "Ocena: " + review["score"] + "<br>"
    output += "Recomendacja: " + str(review["recomendation"]) + "<br>"
    output += "Data zakupu: " + str(review["purchase_date"]) + "<br>"
    output += "Data opinii: " + str(review["comment_date"]) + "<br>"
    output += "Likes: " + review["likes"] + "<br>"
    output += "Dislikes: " + review["dislikes"] + "<br>"
    output += "Props: " + str(review["props"]) + "<br>"
    output += "Cons: " + str(review["cons"]) + "<br>"
    output += "<br>"
    product_reviews_as_string += (output + "<br> <br>")

app = Flask(__name__, template_folder="templates")


@app.route(rule='/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route(rule='/product/<product_id>', methods=['GET'])
def product(product_id):
    return '<pre> ' + product_id + ' </pre>'


@app.route(rule='/about', methods=['GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()