import random

fn_file = open("./first_names.txt")
ln_file = open("./last_names.txt")
fn_lines = fn_file.readlines()
ln_lines = ln_file.readlines()
fn_file.close()
ln_file.close()

first_name = random.choice(fn_lines).replace("\n","")
last_name  = random.choice(ln_lines).replace("\n","")

print(f"{first_name} {last_name}")