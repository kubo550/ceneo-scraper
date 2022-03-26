from stats import Stats

class ProductStore:
    def __init__(self):
        self.store = {}

    def add_product(self, id, name, opinions):
        self.store[id] = {"id": id,"name": name, "opinions": opinions, 'stats': { }}

    def get_product(self, id):
        return self.store[id]
    
    def get_all_products(self):
        products = []
        for product in self.store.values():
            products.append(product)
        return products
    
    def get_all_opinions(self):
        opinions = []
        for product in self.store.values():
            opinions.extend(product["opinions"])
        return opinions
    
    def get_opionions_for_product(self, id):
        return self.store[id]["opinions"]

    def set_stats(self, id, stats):
        self.store[id]["stats"] = stats

    def get_stats(self, id):
        return self.store[id]["stats"]

    def get_product_name(self, id):
        return self.store[id]["name"]