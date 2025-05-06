import uuid
from constants import *
from sample_data import *


class BuyerManager:
    buyers = {}

    def __init__(self, name: str, phone_no: str, address: dict, email: str):
        self.buyer_id = str(uuid.uuid4())
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.email = email

    def add_buyer(self):
        # Check for existing email
        for buyer in BuyerManager.buyers.values():
            if buyer["email"] == self.email:
                print(ErrorCode.EMAIL_ALREADY_EXISTS.value)
                return

        # Check for existing phone number
        for buyer in BuyerManager.buyers.values():
            if buyer["phone_no"] == self.phone_no:
                print(ErrorCode.PHONE_ALREADY_EXISTS.value)
                return

        # Add new buyer
        BuyerManager.buyers[self.buyer_id] = {
            "name": self.name,
            "phone_no": self.phone_no,
            "email": self.email,
            "address": self.address,
        }
        print(f"Buyer {self.name} added successfully with ID {self.buyer_id}.")


buyer_manager = BuyerManager(
    buyer_1_data.get("name"),
    buyer_1_data.get("phone_no"),
    buyer_1_data.get("address"),
    buyer_1_data.get("email"),
)
buyer_manager.add_buyer()

buyer_manager = BuyerManager(
    buyer_2_data.get("name"),
    buyer_2_data.get("phone_no"),
    buyer_2_data.get("address"),
    buyer_2_data.get("email"),
)
buyer_manager.add_buyer()