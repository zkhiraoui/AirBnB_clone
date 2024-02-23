import json
import os
from models.user import User
from models.base_model import BaseModel
# Import other models here as needed
from json.decoder import JSONDecodeError

class FileStorage:
    """A class that serializes instances to a JSON file & deserializes JSON file to instances."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Adds new object to the storage dictionary."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
            for obj_id, obj_dict in objects.items():
                cls_name = obj_dict['__class__']
                if cls_name == 'BaseModel':
                    self.__objects[obj_id] = BaseModel(**obj_dict)
                elif cls_name == 'User':
                    self.__objects[obj_id] = User(**obj_dict)
                # Add more classes here as your project expands
        except FileNotFoundError:
            pass
