#!/usr/bin/python3
from models.user import User
from models import storage

json = storage.all()
print("---Reloading objects---")
for obj_k in json.keys():
    obj = json[obj_k]
    print(obj)

"""print("---Create user---")
user = User()
user.first_name = "Robert"
user.last_name = "foo"
user.email = "me@gmail.com"
user.password = "root4"
user.save()
print(user)"""

