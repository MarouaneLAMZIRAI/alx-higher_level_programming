#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then saves them to a file using JSON representation.
"""

import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the file exists, if not, create it with an empty list
if not path.exists(filename):
    save_to_json_file([], filename)

# Load the current list from the file
my_list = load_from_json_file(filename)

# Add all command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)

