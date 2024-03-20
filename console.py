#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothint line"""
        pass
    
    def do_create(self, arg):
    """
    Creates a new instance of a specified class
    Args:
        arg (str): Class name and parameters in the format "<Class name> <param 1> <param 2> ..."
    """
    if not arg:
        print("** class name missing **")
        return

    args = arg.split()
    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return

    # Remove the class name from the arguments
    args = args[1:]

    # Parse parameters
    params = {}
    for arg in args:
        key_value = arg.split('=')
        if len(key_value) != 2:
            continue
        key = key_value[0]
        value = key_value[1]

        # Handle value syntax
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]  # Remove double quotes
            value = value.replace('_', ' ')  # Replace underscores with spaces
            value = value.replace('\\"', '"')  # Unescape escaped double quotes
        elif '.' in value:
            try:
                value = float(value)
            except ValueError:
                continue
        else:
            try:
                value = int(value)
            except ValueError:
                continue

        params[key] = value

    # Create object with parsed parameters
    new_obj = eval(class_name)(**params)
    new_obj.save()
    print(new_obj.id)

            
    def do_show(self, arg):
        """show a new instance of BaseModel,
        saves it (to the JSON file) """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in self.classes :
            print("** class doesn't exist **")
        elif len(arg.split()) < 2 :
            print("** instance id missing **")
        else:
            key = arg.split()[0] + ' ' + arg.split()[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
                
    def do_destroy(self, arg):
        """destroy all instance of BaseModel,
        saves it (to the JSON file) """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in self.classes :
            print("** class doesn't exist **")
        elif len(arg.split()) < 2 :
            print("** instance id missing **")
        else:
            key = arg.split()[0] + ' ' + arg.split()[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
                
    def do_all(self, arg):
        """Prints all string representation of all instances
            based or not on the class name"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items()])
            
        
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
