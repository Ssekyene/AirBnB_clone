#!/usr/bin/python3

"""
Entry to command interpreter
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = '(hbnb)'
    classes = {"BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"}

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        "Shouldn’t execute anything"
        pass

    def do_create(self, line):
        "Creates new BaseModel instance, saves to JSON, prints id"
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        "Prints str rep of an instance, based on class and id"
        if len(line) == 0:
            print("** class name missing**")
            return
        args = parse(line)
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                class_name = f"{args[0]}.{args[1]}"
                if class_name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[class_name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        "Deletes all inst based on class name and id. Save changes to JSON"
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                class_name = f"{args[0]}.{args[1]}"
                if class_name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[class_name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        "Prints str rep of all instances based/not on class name"
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(str(objs))
            print(obj_list)
        elif args[0] in self.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(str(objs))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        "Updates inst based on class name & id;adds/updates attr; Save to JSON"
        args = parse(line)
        size = len(args)
        objs = storage.all()
        if not args:
            print("** class name missing **")
        elif not args[0] in self.classes:
            print("** class doesn't exist **")
        elif size < 2:
            print("** instance id missing **")
        elif not ".".join([args[0], args[1]]) in objs.keys():
            print("** no instance found **")
        elif size < 3:
            print("** attribute name missing **")
        elif size < 4:
            print("** value missing **")
        else:
            try:
                obj = objs[".".join([args[0], args[1]])]
                setattr(obj, args[2], args[3])
                storage.save()
            except Exception as e:
                print(e)
                print("** Update fail **")

    def do_count(self, line):
        "Display count of instances"
        if line in self.classes:

            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, args):
        "Capture User.method()"
        if "." not in args:
            print("*** Unknown syntax: {}".format(args))
            return
        args = args.split(".")
        _class = args[0]
        objs = storage.all()
        command = args[1]
        if _class not in self.classes:
            print("*** Unknown syntax: {}".format(".".join(args)))
            return
        if command[0:7] == "count()":
            count = 0
            for key in objs.keys():
                if _class == key.split(".")[0]:
                    count -= -count ** 0
            print(count)
        elif command[0:5] == "all()":
            self.do_all(_class)
        elif command[0:5] == "show(":
            _id = command.split("(")[1][0:-1]
            self.do_show(_class + " " + _id)
        elif command[0:8] == "destroy(":
            _id = command.split("(")[1][0:-1]
            self.do_destroy(_class + " " + _id[1:-1])
        elif command[0:7] == "update(":
            args = command.split("(")[1][0:-1].split(", ")
            _id = args[0][1:-1]
            if args[1][0] == "{":
                _dict = ast.literal_eval("{" + command.split("{")[1][0:-1])
                for key, va in _dict.items():
                    self.do_update(" ".join([_class, str(_id), key, str(va)]))
            else:
                _key = args[1][1:-1]
                _value = args[2][1:-1]
                self.do_update(" ".join([_class, _id, _key, _value]))
        else:
            print("*** Unknown syntax: {}".format(".".join(args)))


def parse(line):
    "Helper method that parses user input"
    return tuple(line.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
