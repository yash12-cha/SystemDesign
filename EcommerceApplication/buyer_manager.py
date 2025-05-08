import uuid
from constants import *
from sample_data import *
from sample_db_data import *


class BuyerManager:

    def __init__(self):
        pass

    def add_buyer(self, buyer_data: dict):
        email = buyer_data.get("email")
        phone_no = buyer_data.get("phone_no")

        # Check for existing email
        for buyer in buyers.values():
            if buyer["email"] == email:
                print(ErrorCode.EMAIL_ALREADY_EXISTS.value)
                return

        # Check for existing phone number
        for buyer in buyers.values():
            if buyer["phone_no"] == phone_no:
                print(ErrorCode.PHONE_ALREADY_EXISTS.value)
                return

        buyer_id = str(uuid.uuid4())
        buyers[buyer_id] = {
            "name": buyer_data.get("name"),
            "phone_no": phone_no,
            "email": email,
            "address": buyer_data.get("address"),
        }
        print(
            f"Buyer {buyer_data.get('name')} added successfully with ID {buyer_id}."
        )

    def get_buyer_by_id(self, user_id):
        return buyers.get(user_id)


buyer_manager = BuyerManager()

buyer_1_id = buyer_manager.add_buyer(buyer_1_data)
buyer_2_id = buyer_manager.add_buyer(buyer_2_data)
