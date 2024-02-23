import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""

    prompt = "(hbnb) "

    def __init__(self):
        """Initializes HBNBCommand"""
        self.storage = FileStorage()

    def do_EOF(self, arg):
        """Quits the program"""
        print()
        return True

    def do_quit(self, arg):
        """Quits the program"""
        print("Goodbye!")
        return True

    def do_create(self, arg):
        """Creates a new object"""
        try:
            args = arg.split()
            cls_name = args[0]
            obj_id = args[1]
            if cls_name == "BaseModel":
                obj = BaseModel(id=obj_id)
            elif cls_name == "User":
                obj = User(id=obj_id, name=args[2], email=args[3])
            elif cls_name == "State":
                obj = State(id=obj_id, name=args[2])
            elif cls_name == "City":
                obj = City(id=obj_id, name=args[2], state_id=args[3])
            elif cls_name == "Amenity":
                obj = Amenity(id=obj_id, name=args[2])
            elif cls_name == "Place":
                obj = Place(id=obj_id, name=args[2], city_id=args[3], user_id=args[4],
                             description=args[5], number_rooms=int(args[6]),
                             number_bathrooms=int(args[7]), max_guests=int(args[8]),
                             price_by_night=int(args[9]), latitude=float(args[10]),
                             longitude=float(args[11]))
            elif cls_name == "Review":
                obj = Review(id=obj_id, user_id=args[2], place_id=args[3],
                              text=args[4], rating=int(args[5]))
            else:
                print("Invalid class name")
                return
            self.storage.new(obj)
            self.storage.save()
            print("Created successfully")
        except IndexError:
            print("Invalid arguments")

    def do_show(self, arg):
        """Shows an object"""
        try:
            obj_id = arg.split()[0]
            obj = self.storage.objects[f"{obj_id.__class__.__name__}.{obj_id}"]
            print(obj)
        except (IndexError, KeyError):
            print("Invalid arguments")

    def do_destroy(self, arg):
        """Deletes an object"""
        try:
            obj_id = arg.split()[0]
            obj = self.storage.objects[f"{obj_id.__class__.__name__}.{obj_id}"]
            del self.storage.objects[f"{obj_id.__class__.__name__}.{obj_id}"]
            self.storage.save()
            print("Deleted successfully")
        except (IndexError, KeyError):
            print("Invalid arguments")

def do_all(self, arg):
    """Prints all string representation of instances based or not on the class name."""
    if arg:
        for obj in self.storage.all().values():
            if obj.__class__.__name__ == arg:
                print(obj)
    else:
        for obj in self.storage.all().values():
            print(obj)
            print("Object saved!", obj)


def do_update(self, arg):
    """Updates an object"""
    try:
        args = arg.split()
        obj_id = args[0]
        obj = self.storage.objects[f"{obj_id.__class__.__name__}.{obj_id}"]
        attr_name = args[1]
        attr_value = args[2]
        setattr(obj, attr_name, attr_value)
        self.storage.save()
        print("Updated successfully")
    except (IndexError, KeyError):
        print("Invalid arguments")
