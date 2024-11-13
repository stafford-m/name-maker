""" 
Generates names
    - by stafford-m
"""
import random
import argparse
import sys

MAX_RECURSION = 300
R_COUNTER = 0
NAMES_GENERATED = 0

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
    default=[300],
    help='Charater limit of names - default is 300'
)
parser.add_argument(
    '--number', '-n',
    type=int,
    nargs=1,
    default=[1],
    help='Number of names to generate.'
)
args = parser.parse_args()

def get_name(filename):
    """gets a name from the provided file (with error handling)"""
    try:
        with open(filename, encoding="utf-8") as name_file:
            name_lines = name_file.readlines()
            choice_name = random.choice(name_lines).replace("\n","")
            return choice_name
    except FileNotFoundError:
        print(f"File {filename} not found, exiting...")
        sys.exit()
    except PermissionError:
        print(f"You do not have permissions to access {filename}")
        sys.exit()
    except Exception as exc:
        print("Error occurred: ", exc)
        sys.exit()

def name_gen(file_args, max_chars, r_count):
    """puts the get_name's together"""
    output = ''
    for name_file in file_args:
        output += get_name(name_file) + ' '
    if len(output) > max_chars + 1 and MAX_RECURSION > r_count:
        r_count += 1
        return name_gen(file_args, max_chars, r_count)
    if r_count >= MAX_RECURSION:
        print("WARNING: Maximum recursion depth reached.")
        sys.exit()
    else:
        return output.strip()

maximum_chars, = args.chars
names_to_generate, = args.number

while NAMES_GENERATED < names_to_generate:
    name = name_gen(args.names, maximum_chars, R_COUNTER)
    print(f"{name}")
    NAMES_GENERATED += 1
