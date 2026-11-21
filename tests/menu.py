def price_of(prices,item):
    try:
        return prices[item]
    except KeyError:
        return "not on the menu"
prices={ "chai": 80, "coffee":150}
print(price_of(prices, "chai"))  
print(price_of(prices, "lassi"))  
print(price_of(prices, "coffee"))  
print(price_of(prices, "paratha"))  
