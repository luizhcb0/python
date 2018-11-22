import json

#path = "../pydata-book/datasets/usda_food/database.json"
path = "../pydata-book/datasets/bitly_usagov/example.txt"
records = [json.loads(line) for line in open(path)]

print(records[0])
