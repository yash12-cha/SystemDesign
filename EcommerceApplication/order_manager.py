import uuid
from buyer_manager import *
from product_manager import *


class OrderManager():
    order = {}

    def __init__(self, productId, quantity, buyerId, paymentMode):
        self.product_id = productId
        self.quantity = quantity
        self.buyer_id = buyerId
        self.payment_mode = paymentMode

    def create_order(self):
        buyer_manager = BuyerManager()
        buyerDetails = buyer_manager.get_buyer_by_id(self.buyer_id)
        product_manager = ProductManager()
        productDetails = product_manager.get_product_by_id(self.product_id)
        self.order = {
            "orderId": str(uuid.uuid4()),
            "buyerDetails": buyerDetails,
            "productDetails": productDetails,
            "orderQuantity": self.quantity,
            "paymentMode": self.payment_mode,
        }
        print(f"Order created successfully with ID {self.order['orderId']}.")


order_manager = OrderManager(
    order_1_data.get("product_id"),
    order_1_data.get("quantity"),
    order_1_data.get("buyer_id"),
    order_1_data.get("payment_mode"),
)

order_manager.create_order()

print(order_manager.order)
