from scraper import Scraper
from flask import Flask, render_template, request
from stats import Stats
from product_store import ProductStore
import jsonpickle

store = ProductStore()


app = Flask(__name__, template_folder="templates")


@app.route(rule='/', methods=['GET'])
def index():
    return render_template('index.jinja')


@app.route(rule='/product', methods=['GET'])
def _product():
    product_id = request.args.get('product_id')

    if product_id is None:
        return render_template('product.jinja')
    try:
        ceneo_scraper = Scraper(product_id)
        product_name = ceneo_scraper.get_product_name()
        product_reviews = ceneo_scraper.get_all_opinions()
        store.add_product(product_id, product_name, product_reviews)
        
        product_stats = Stats.calculate_stats(product_reviews)
        store.set_stats(product_id, product_stats)

        with open(file='./static/' + product_id + '.json', mode='w') as f:
            jsonpickle.set_encoder_options('json', indent=2)
            f.write(jsonpickle.encode(product_reviews))
        json_product_reviews = jsonpickle.encode(product_reviews)


        return render_template('opinion.jinja', product_reviews=product_reviews, product_id=product_id, json=json_product_reviews, number_of_reviews=len(product_reviews))
    except Exception as e:
        print("Error: ", e)
        return render_template('product.jinja', error=e)


@app.route(rule='/about', methods=['GET'])
def about():
    return render_template('about.jinja')

@app.route(rule='/opinion', methods=['GET'])
def opinion():     
    return render_template('product.jinja', error="Aby przejść do strony opinii, wpisz id produktu.") 


@app.route(rule='/details/<product_id>', methods=['GET'])
def details(product_id):
    reviews = store.get_opionions_for_product(product_id)

    product_data = Stats.get_recomendations(reviews)
    rating = Stats.get_ratings(reviews)
    product_name = store.get_product_name(product_id)
    return render_template('details.jinja', id=product_id, product_data=product_data, rating=rating,product_name=product_name)

@app.route(rule='/product-list', methods=['GET'])
def product_list():
    products = store.get_all_products()
    return render_template('product-list.jinja', products=products, products_len=len(products))

if __name__ == '__main__':
    app.run()