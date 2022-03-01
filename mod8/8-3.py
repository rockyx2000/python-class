import sys
import json

word = sys.argv[1]

with open("json.txt", "w") as file:
    json.dump(word, file)