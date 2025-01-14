import json
import os

class ProductManager:
    def __init__(self, data_file):
        self.data_file = data_file

    def load_products(self):
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, "r") as file:
            return json.load(file)

    def save_products(self, products):
        with open(self.data_file, "w") as file:
            json.dump(products, file)

    def add_product(self, product):
        products = self.load_products()
        products.append(product)
        self.save_products(products)
        return {"message": "Produto cadastrado com sucesso!"}

    def clear_products(self):
        self.save_products([])
        return {"message": "Todos os produtos foram removidos!"}

    def get_products(self):
        return self.load_products()
