import json
from termcolor import colored

def json_to_dict(json_file):
    try:
        with open(json_file,'r') as file:
            return json.load(file)
    except Exception as e:
        print(colored(e,'red'))

def dict_to_json(dict,json_file):
    try:
        with open(json_file,'w') as file:
            json.dump(dict,file)
    except Exception as e:
        print(colored(e,'red'))