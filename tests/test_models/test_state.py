#!/usr/bin/python3
import unittest
from models.state import State
from datetime import datetime

class TestState(unittest.TestCase):
    """Test the State class"""
    
    def test_instance_creation(self):
        """Test creation of State instance"""
        my_state = State()
        self.assertTrue(isinstance(my_state, State))
        self.assertIsInstance(my_state.created_at, datetime)
        self.assertIsInstance(my_state.updated_at, datetime)

    def test_attribute_types(self):
        """Test the types of attributes"""
        my_state = State()
        my_state.name = "California"
        self.assertEqual(my_state.name, "California")

if __name__ == '__main__':
    unittest.main()
