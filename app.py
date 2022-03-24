from scraper import Scraper
from flask import Flask, render_template, request
import jsonpickle

my_product_id = "103735237"



app = Flask(__name__, template_folder="templates")


@app.route(rule='/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route(rule='/product', methods=['GET'])
def _product():
    product_id = request.args.get('product_id')

    print(product_id)
    if product_id is None:
        return render_template('product.html')
    try:
        ceneo_scraper = Scraper(product_id)
        product_reviews = ceneo_scraper.get_all_opinions()
        with open(file='./static/data.json', mode='w') as f:
            jsonpickle.set_encoder_options('json', indent=2)
            f.write(jsonpickle.encode(product_reviews))
        json_product_reviews = jsonpickle.encode(product_reviews)

        return render_template('opinion.html', product_reviews=product_reviews, json=json_product_reviews, number_of_reviews=len(product_reviews))
    except Exception as e:
        print("Error: ", e)
        return render_template('product.html', error=e)




@app.route(rule='/about', methods=['GET'])
def about():
    return render_template('about.html')



@app.route(rule='/opinion', methods=['GET'])
def opinion():     
        return render_template('product.html', error="Aby przejść do strony opinii, wpisz id produktu.") 

if __name__ == '__main__':
    app.run()