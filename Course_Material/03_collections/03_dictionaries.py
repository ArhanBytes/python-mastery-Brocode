"""
=========================================
Topic: Dictionaries
Section: Collections
Description:
Dictionary = a collection of {key: value} pairs
- Ordered 
- Changeable (Mutable)
- No duplicate keys allowed
=========================================
"""

# ==================================================
# 1️⃣ Creating a Dictionary
# ==================================================
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# ==================================================
# 2️⃣ Exploring Dictionary Methods
# ==================================================

# print(dir(capitals))   # Shows all available attributes & methods
# print(help(capitals))  # Detailed explanation of dictionary methods


# ==================================================
# 3️⃣ Accessing Values
# ==================================================

# Using .get() → Returns None if key not found (no error)
print("\n--- Accessing Value ---")
print("Capital of China:", capitals.get("China"))


# ==================================================
# 4️⃣ Handling None Value
# ==================================================

print("\n--- Checking if Key Exists ---")
if capitals.get("Japan"):
    print("The capital exists.")
else:
    # None is treated as False
    print("The capital does not exist.")


# ==================================================
# 5️⃣ Updating Dictionary
# ==================================================

# .update() → Add new key or update existing key
print("\n--- Updating Dictionary ---")
capitals.update({"Germany": "Berlin"})
print("After adding Germany:", capitals)


# ==================================================
# 6️⃣ Removing Elements
# ==================================================

# .pop() → Removes specific key
print("\n--- Removing Specific Key (China) ---")
capitals.pop("China")
print("After pop:", capitals)

# .popitem() → Removes last inserted key-value pair
print("\n--- Removing Last Inserted Pair ---")
capitals.popitem()
print("After popitem:", capitals)

# .clear() → Removes everything
# capitals.clear()


# ==================================================
# 7️⃣ Working with Keys
# ==================================================

print("\n--- Dictionary Keys ---")
keys = capitals.keys()   # Returns a dict_keys object
print("Keys object:", keys)

for key in capitals.keys():
    print(f"Key: {key}")


# ==================================================
# 8️⃣ Working with Values
# ==================================================

print("\n--- Dictionary Values ---")
values = capitals.values()   # Returns a dict_values object
print("Values object:", values)

for value in capitals.values():
    print(f"Value: {value}")


# ==================================================
# 9️⃣ Working with Items (Key + Value)
# ==================================================

print("\n--- Dictionary Items ---")
items = capitals.items()   # Returns dict_items object (like 2D tuples)
print("Items object:", items)

# Method 1
for item in capitals.items():
    print(f"Key: {item[0]}, Value: {item[1]}")

# Method 2 (Better way)
for key, value in capitals.items():
    print(f"Key: {key}, Value: {value}")