import json

#path = "../pydata-book/datasets/usda_food/database.json"
path = "../pydata-book/datasets/bitly_usagov/example.txt"
records = [json.loads(line) for line in open(path)]

#print(records[0])
timezones = [rec['tz'] for rec in records if 'tz' in rec and rec['tz'] != '']
timezones.__len__()
len(timezones)

def get_counts(seq):
    counts = {}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

c = get_counts(timezones)
