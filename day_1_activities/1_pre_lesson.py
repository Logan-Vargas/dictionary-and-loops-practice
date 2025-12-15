# this is what we will use for the video intro to dictionaries

#dictionary = a collection of {key: value} pairs ordered and changeable. No duplicates.

capitals = {
    "USA": "Washington, D.C.", 
    "France": "Paris",
    "Germany": "Berlin"
}   
#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("Japan"))


# print(capitals.get("USA"))

# if capitals.get("Italy") is None:
#     print("No data found for Italy")

# capitals.update({"Italy": "Rome"})
# capitals.update({"USA": "Chicago"}) 

#capitals.pop("China") # changes value for existing key
# capitals.popitem()
#capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# print(values)

# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in items:
    print(f"Key: {key} Value: {value}")

print(capitals)

