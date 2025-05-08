import uuid
from sample_data import *
from sample_db_data import *


class ProductManager:

    def __init__(self):
        pass

    def add_product(self, product_data: dict):
        product_id = str(uuid.uuid4())
        products[product_id] = {
            "productName": product_data.get("productName"),
            "productDescription": product_data.get("productDescription"),
            "productQuantity": product_data.get("productQuantity"),
            "address": product_data.get("address"),
        }
        print(
            f"Product {product_data.get('productName')} added successfully with ID {product_id}."
        )

    def get_product_by_id(self, product_id):
        return products.get(product_id)


product_manager = ProductManager()

product_manager.add_product(product_1_data)
product_manager.add_product(product_2_data)
