import json
def calculate_sum_of_products(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    total_sum = 0.0

    for item in data:
        if 'score' in item and 'weight' in item:
            product = item['score'] * item['weight']
            total_sum += product

    return round(total_sum, 3)

filename = 'input.json'
result = calculate_sum_of_products(filename)
print(result)