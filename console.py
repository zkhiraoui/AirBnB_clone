#!/usr/bin/python3
"""
Module for the entry point of the command interpreter.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the AirBnB clone project.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on receiving EOF
        """
        print()  # Print newline for neatness
        return True

    def emptyline(self):
        """
        Do nothing upon receiving an empty line.
        """
        pass

    def do_help(self, arg):
        """
        Display help for commands.
        """
        super().do_help(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
