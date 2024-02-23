#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModelInitialization(unittest.TestCase):
    """Test the initialization of BaseModel instances."""

    def test_new_instance(self):
        """Test creation of a new instance without kwargs."""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(isinstance(model.created_at, datetime))

    def test_instance_from_dict(self):
        """Test creation of an instance from a dictionary."""
        my_model_json = {
            'id': 'some-unique-id',
            'created_at': '2021-02-11T09:25:24.582122',
            'updated_at': '2021-02-11T09:25:24.582122',
            'name': 'My First Model',
            'my_number': 89
        }
        model = BaseModel(**my_model_json)
        self.assertEqual(model.id, 'some-unique-id')
        self.assertEqual(model.name, 'My First Model')
        self.assertEqual(model.my_number, 89)
        self.assertTrue(isinstance(model.created_at, datetime))
        self.assertTrue(isinstance(model.updated_at, datetime))

if __name__ == '__main__':
    unittest.main()

