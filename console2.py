#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        if arg:
            if arg in ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']:
                print([str(obj) for obj in storage.all().values() if type(obj).__name__ == arg])
            else:
                print("** class doesn't exist **")
        else:
            print([str(obj) for obj in storage.all().values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split(" ", 3)
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        try:
            obj = storage.all()[key]
            setattr(obj, args[2], args[3].strip('"'))
            obj.save()
        except KeyError:
            print("** no instance found **")

    def default(self, line):
        """Catch-all for commands that don't match a known command."""
        parts = line.partition(".")
        if len(parts) == 3 and parts[1] == ".":
            if parts[2] == "all()":
                self.do_all(parts[0])
            elif parts[2] == "count()":
                self.count_instances(parts[0])
            else:
                print("*** Unknown syntax:", line)
        else:
            print("*** Unknown syntax:", line)

    def count_instances(self, class_name):
        """Counts number of instances of a given class."""
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == class_name:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
