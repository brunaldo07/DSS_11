import random
import json

# Generate 1000 random numbers over the range 0-100 and save them in a JSON file.

numbers = []
for i in range(1000):
	a = random.randint(0,100)
	numbers.append(a)
json_numbers=json.dumps(numbers)

with open('numbers.json', 'w') as outfile:
    json.dump(json_numbers, outfile)

