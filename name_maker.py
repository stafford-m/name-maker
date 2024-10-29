""" 
Generates names
    - by stafford-m
"""
import random

def get_name(filename):
    """gets a name from the provided file"""
    with open(filename, encoding="utf-8") as name_file:
        name_lines = name_file.readlines()
        choice_name = random.choice(name_lines).replace("\n","")
        return choice_name

first_name = get_name("./first_names.txt")
last_name  = get_name("./last_names.txt")

print(f"{first_name} {last_name}")
