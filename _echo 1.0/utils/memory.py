# eeeeeeeeeeee working okay okay
import json

def rember(prompt):
    with open("./memory.json") as file:
        data = json.load(file)
        data.append(prompt)