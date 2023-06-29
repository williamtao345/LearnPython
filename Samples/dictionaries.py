user = {
    "name": "William Tao",
    "age": 18,
    "is_verified": True
}

# Get value (it will return an error if value does not exist)
print(user["name"])

# Get value (it will NOT return an error)
print(user.get("age", "default_value"))
