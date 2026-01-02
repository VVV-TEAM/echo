import json

class config:
    def __init__(self):
        with open("./config/settings.json") as file:
            self.data = json.load(file)

    def get_deepinfra_api_key(self):
        return self.data["deepinfra_api_key"]