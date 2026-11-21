shop = {
    "name": "Student Biryani",
    "branches": [
        {"city": "Lahore",
         "tables": [4, 6, 6]},
        {"city": "Karachi",
         "tables": [8, 8]},
    ],
}
 
print(shop["name"])
print(shop["branches"][0]["city"])
print(shop["branches"][0]["tables"][2])

for branch in shop["branches"]:
    for seats in branch["tables"]:
        print(branch["city"], seats)
