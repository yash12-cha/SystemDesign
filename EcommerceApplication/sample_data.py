# Contains sample data used across the application.

buyer_1_data = {
    "name": "Ram Kumar",
    "phone_no": "9271948193",
    "address": {
        "address_line_1": "Block - F",
        "address_line_2": "House No 789",
        "address_line_3": "Stanza Building Tower A",
        "landmark": "Near Acme School",
        "city": "North Delhi",
        "state": "Delhi",
        "pincode": "208020",
    },
    "email": "testw@gmail.com",
}

buyer_2_data = {
    "name": "Raju Gupta",
    "phone_no": "8871948193",
    "address": {
        "address_line_1": "Block - N",
        "address_line_2": "Flat No 765",
        "address_line_3": "Khana Residency Tower A",
        "landmark": "Near Lulu Mall",
        "city": "Bengaluru",
        "state": "Karnataka",
        "pincode": "560103",
    },
    "email": "test.c1@gmail.com",
}

product_1_data = {
    "productName": "Smart LED TV 43 inch Full HD",
    "productDescription": {
        "screenType": "LED",
        "resolution": "1920 x 1080",
        "connectivity": ["HDMI", "USB", "Wi-Fi"],
        "features": ["Smart TV with apps", "Energy efficient", "Slim design"],
    },
    "productQuantity": 30,
    "address": {
        "address_line_1": "ElectroMart",
        "address_line_2": "Sector 12",
        "address_line_3": "Malviya Nagar",
        "landmark": "Near Malviya Circle",
        "city": "Jaipur",
        "state": "Rajasthan",
        "pincode": "302017",
    },
}


product_2_data = {
    "productName": "Classic Women's Casual Denim Jacket",
    "productDescription": {
        "material": "100% Cotton",
        "features": [
            "Lightweight",
            "Breathable fabric",
            "Classic fit",
            "Machine washable",
        ],
        "careInstructions": "Wash with similar colors, do not bleach.",
    },
    "productQuantity": 50,
    "address": {
        "address_line_1": "Fashion Hub",
        "address_line_2": "Near City Mall",
        "address_line_3": "Bani Park",
        "landmark": "Opposite to Metro Station",
        "city": "Jaipur",
        "state": "Rajasthan",
        "pincode": "302016",
    },
}

order_1_data = {
    "product_id": "9a95e3ac-35e8-4acd-8687-f673a1d4795b",
    "quantity": 2,
    "buyer_id": "1a95e3ac-35e8-4acd-8687-f673a1d4795b",
    "payment_mode": "UPI",
}
