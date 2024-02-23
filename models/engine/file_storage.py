import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
                objs = json.load(f)
            for obj_id, obj_dict in objs.items():
                cls_name = obj_dict['__class__']
                cls = globals()[cls_name]
                self.__objects[obj_id] = cls(**obj_dict)
        except FileNotFoundError:
            pass
