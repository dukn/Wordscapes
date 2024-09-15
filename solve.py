import os
import json
from itertools import permutations

def load_json_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


data = load_json_from_file('data/words_dictionary.json')
print("Dictionary:", len(data))

def generate_words(chars):
    words = set()
    for i in range(1, len(chars) + 1):
        for perm in permutations(chars, i):
            words.add(''.join(perm))
    return list(words)

while True:
    word = input('Enter a word: ')
    chars = list(word)
    words = generate_words(chars)
    results = []
    for word in words:
        if len(word) < 3:
            continue
        if word in data:
            results.append(word)
    results.sort()
    print(results)
    print()

