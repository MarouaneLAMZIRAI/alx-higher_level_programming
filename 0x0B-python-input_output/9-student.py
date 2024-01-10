#!/usr/bin/python3
"""
Module that contains a class Student that defines a student
with public instance attributes and a public method.
"""


class Student:
    """
    Student class with public instance attributes: first_name,
    last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return self.__dict__


if __name__ == "__main__":
    pass

