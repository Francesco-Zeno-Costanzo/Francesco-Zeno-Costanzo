"""
Code to clone all repo at once in case of a new pc.
You must have a file with all git@github:... in some backup
the code read this file and execute git clone.
All repo will be cloned in the current directory.
"""
import argparse
from subprocess import call

description='Code to clone all repo at once in case of a new pc.'

parser = argparse.ArgumentParser(description=description)
parser.add_argument('input_file',  help='path to the file containing the repo names')
args = parser.parse_args()

# Read file
with open(args.input_file, "r", encoding="utf-8") as file:
    lines = file.read()

# Split lines
all_lines = lines.split("\n")

for line in all_lines:
    # Lines ignored
    if line == "" or line[0] == "#" :
        pass
    # Clone
    else:
        call(f"git clone {line}", shell=True)
