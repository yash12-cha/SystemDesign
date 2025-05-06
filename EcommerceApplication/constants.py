# Contains enums and constants used across the application.

from enum import Enum


class ErrorCode(Enum):
    BUYER_ALREADY_EXISTS = "Buyer already exists"
    ORDER_ALREADY_EXISTS = "Order already exists"
    PRODUCT_ALREADY_EXISTS = "Product already exists"
    DUPLICATE_PRODUCT = "Duplicate product"
    INSUFFICIENT_INVENTORY = "Insufficient inventory for the order"
    UNSERVICABLE_PINCODE = "Pincode is unserviceable"
