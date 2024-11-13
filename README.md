# Name Maker
Script for generating names
## Requirements
python version >= 3.2 
    for [argparse](https://docs.python.org/3/library/argparse.html)
## Quick usage guide
Simply include the file names as positional commandline arguments while running the script
```
python3 name_maker.py ./first_names.txt ./last_names.txt
```
default behavior is to use 2 files named `./first_names.txt` and `./last_names.txt` so `python3 name_maker.py` will do the same as shown above


There are options for number of names to generate `-n #` and maximum letter count for generated names `-c #`
```
python3 name_maker.py ./first_names.txt ./last_names.txt -n 2 -c 14 
```test
