""" 
Generates names
    - by stafford-m
"""
import random
import argparse

parser = argparse.ArgumentParser(
    prog="name_maker",
    description="Generates Names"
)
parser.add_argument('names',
    nargs='*',
    default=['./first_names.txt', './last_names.txt'],
    help='Input files'
)
args = parser.parse_args()

def get_name(filename):
    """gets a name from the provided file"""
    with open(filename, encoding="utf-8") as name_file:
        name_lines = name_file.readlines()
        choice_name = random.choice(name_lines).replace("\n","")
        return choice_name

def name_gen(file_args):
    """puts the get_name's together"""
    output = ''
    for name_file in file_args:
        output += get_name(name_file) + ' '
    return output

name = name_gen(args.names)
print(f"chosen name: {name}")
