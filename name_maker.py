""" 
Generates names
    - by stafford-m
"""
import random
import argparse
import sys

MAX_RECURSION = 300

parser = argparse.ArgumentParser(
    prog="name_maker",
    description="Generates Names"
)
parser.add_argument(
    'names',
    nargs='*',
    default=['./first_names.txt', './last_names.txt'],
    help='Input files'
)
parser.add_argument(
    '--chars', '-c',
    type=int,
    nargs=1,
    default=300,
    help='Charater limit of names - default is 300'
)
args = parser.parse_args()

def get_name(filename):
    """gets a name from the provided file"""
    with open(filename, encoding="utf-8") as name_file:
        name_lines = name_file.readlines()
        choice_name = random.choice(name_lines).replace("\n","")
        return choice_name

def name_gen(file_args, max_chars, r_count):
    """puts the get_name's together"""
    output = ''
    for name_file in file_args:
        output += get_name(name_file) + ' '
    if len(output) > max_chars and MAX_RECURSION > r_count:
        print(r_count)
        return name_gen(file_args, max_chars, r_count)
    if r_count >= MAX_RECURSION:
        print("WARNING: Maximum recursion depth reached, exiting...")
        sys.exit()
    else:
        return output.strip()

R_COUNTER = 0
maximum_chars, = args.chars
name = name_gen(args.names, maximum_chars, R_COUNTER)
print(f"{name}")
