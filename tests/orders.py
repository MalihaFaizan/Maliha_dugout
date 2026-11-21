import json

order = {"item": "paratha", "qty": 2,
         "paid": True, "note": None}
 
print(type(order))
text = json.dumps(order, indent =2)
print(text)
print(type(text))

import json
 
text = '{"item": "paratha", "qty": 2, "paid": true, "note": null}'
 
order = json.loads(text)
print(order)
print(type(order))
print(order["qty"] + 1)