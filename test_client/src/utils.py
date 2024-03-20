import json


def load_capabilities():
    with open('appium.json') as f:
        config = json.load(f)
    return config['capabilities']
