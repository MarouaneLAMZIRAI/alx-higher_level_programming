#!/usr/bin/python3
"""
Module that contains a function to insert a line of text after each line
containing a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to insert after lines with the
                         search_string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)


if __name__ == "__main__":
    pass

