"""
Topic: Dictionaries
Section: Collections
Description:
Dictionary = a collection of {key:value} pairs
ordered and changeable. No duplicates
"""

# --- Creating Dictionary ---
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# --- Methods and Attributes of Dictionary ---
# print(dir(capitals))

# --- Methods and Attributes in depth Description ---
# print(help(capitals))

# --- Accessing value correspondin to key (return none if not found)---
print(capitals.get("China"))

# --- Handling none value ---
if capitals.get("Japan"):
    print("The Capital exists")
else: # none is a false value so it goes there
    print("The capital does not exist")

# --- update function (to add/update the existing key value pair) ---  
capitals.update({"Germany" : "Berlin"})

# --- pop function (remove the pair of given key) ---
capitals.pop("China")

# --- popitem function (remove the last key value pair) ---
capitals.popitem()

# --- clear function (to clear the dictionary) ---
# capitals.clear()

print(capitals)
# --- Get all the keys within the dictionary not value ---
keys = capitals.keys() # return object which resembles a list of keys
print(keys)

# --- printing keys using for loop ---
for key in capitals.keys():
    print(f"Key: {key}")
    
# --- Get all the value within the dictionary not keys ---
values = capitals.values() # returns an object which resembles a list of values
print(values)

# --- printing values using for loop ---
for value in capitals.values():
    print(f"Value: {value}")
    
# --- Get all the items in dictionary (trickier one) ---
items = capitals.items()
print(items) # returns an object which resembles a 2d list of tuple

# --- Printing items using for loop
for item in capitals.items():
    print(f"Key: {item[0]}, Value: {item[1]}")
# OR
for key, value in capitals.items():
    print(f"Key: {key}, Value: {value}")