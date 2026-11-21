prices = {"chai":80, "coffee": 150,
          "paratha": 120}
try:
    print(prices["lassi"])
except KeyError:
    print("Sorry, we do not sell lassi")
    print("Thank you, come again")
