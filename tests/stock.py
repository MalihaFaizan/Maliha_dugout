class ShopError(Exception):
    """Base class for this shops's errors."""

class OutOfStockError(ShopError):
    """Raised when an item is finished."""

    def __init__(self, item):
        super().__init__(f"{item}is finished")
        
try:
    raise OutOfStockError("paratha")
except ShopError as error:
    print("Caught:", error)
    print("The item was:", error.item)
   