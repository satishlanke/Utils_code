import json

# Sample data to save
data = {"name": "Alice", "age": 30, "city": "New York"}

# Save data to a file with a custom extension
with open("data.customjson", "w") as file:
    json.dump(data, file)

print("Data has been saved to data.customjson")

with open("data.customjson", "r") as file:
    loaded_data = json.load(file)

print("Loaded data:", loaded_data)