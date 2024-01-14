#!/usr/bin/python3
"""Unit tests for models.base module."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id(self):
        """Check if id is not None."""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertIsNotNone(id(b1))

    def test_init(self):
        """Check if instance is of Base."""
        Base._Base__nb_objects = 0
        b2 = Base()
        self.assertIsInstance(b2, Base)

    def test_num_objects(self):
        """Check the number of objects created."""
        Base._Base__nb_objects = 0
        b3 = Base()
        self.assertEqual(b3.id, 1)

    def test_to_json_string(self):
        """Check to_json_string method."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        a_dict = r1.to_dictionary()
        json_string = json.dumps([a_dict])
        json_list_dict = r1.to_json_string([a_dict])
        self.assertEqual(json_string, json_list_dict)

    def test_save_to_file(self):
        """Check save_to_file method."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        a_dict = [r1.to_dictionary(), r2.to_dictionary()]
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            list_dict = json.loads(file.read())
        self.assertEqual(a_dict, list_dict)

    def test_from_json_string(self):
        """Check from_json_string method."""
        Base._Base__nb_objects = 0
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_create(self):
        """Check create method."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_load_from_file(self):
        """Check load_from_file method."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertIsInstance(list_rectangles_output, list)
        for rect in list_rectangles_input:
            self.assertIsInstance(rect, Rectangle)
        for rect in list_rectangles_output:
            self.assertIsInstance(rect, Rectangle)

    def test_pep8_model(self):
        """Check PEP8 compliance for models/base.py."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_pep8_test(self):
        """Check PEP8 compliance for tests."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")


if __name__ == "__main__":
    unittest.main()

