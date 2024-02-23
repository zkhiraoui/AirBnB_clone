import json
import os
from models.base_model import BaseModel
# Import other models here as needed
from json.decoder import JSONDecodeError

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Adds the object to the __objects dictionary."""
        if obj:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes the __objects dictionary to a JSON file."""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects if __file_path exists."""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    obj_dict = json.load(f)
                for obj_id, obj_data in obj_dict.items():
                    class_name = obj_data['__class__']
                    cls = eval(class_name)  # Dynamically get class
                    self.__objects[obj_id] = cls(**obj_data)
            except JSONDecodeError:
                pass  # File is empty or not valid JSON, safely ignore
