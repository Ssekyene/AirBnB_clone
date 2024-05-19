# 0x00. AirBnB clone - The console

## Welcome to the AirBnB clone project description!

* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all our classes and storage engine


## How to start the command interpreter
Run the executable file for the console to start the command interpreter.
There are various commands we can prompt on our console:

* Create  - Creates a new instance of the given class and saves it.
* Show    - Prints a description of the specified object.
* Destroy - Destroys a specific object.
* All     - Prints all objects in storage, or all objects in storage of particular class.
* Update  - Updates one or more attributes on the specified object.


## How to use command interpreter
### interactive mode:

$ ./console.py
(hbnb) help

	Documented commands (type help <topic>):
	========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

### non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

	Documented commands (type help <topic>):
	========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

	Documented commands (type help <topic>):
	========================================
EOF  help  quit
(hbnb) 
$

## Authors
Project Author:
[Mithamo Beth](https://github.com/Mythamor#hi-there-)
