import requests
from pprint import pprint
from functools import reduce

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
data = response.json()

def clean_metric_weight (cat):
    lowest, _, heightest= cat['weight']['metric'].split()
    return (float(lowest) + float(heightest)) / 2

weights = [clean_metric_weight(cat) for cat in data]
mean = sum(weights) / len(weights)
print(round(mean, 2))
