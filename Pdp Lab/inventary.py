"""
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

# D inherits from both B and C
class D(B, C):
    pass

# Creating an instance of D
d_instance = D()

# Calling the show method
d_instance.show()
"""

import json

# Sample Python dictionary
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "grades": [95, 89, 88]
}
data1 = {
    "name": "Arun",
    "age": 35,
    "city": "New Jersey",
    "is_student": True,
    "grades": [85, 80, 98]
}

# Serialize the Python dictionary to a JSON-formatted string
with open ("fi4321.txt","w") as file:
    dumpedfile = json.dump([data,data1],file,indent=2)  # The indent parameter is optional and makes the output more readable

# Print the JSON-formatted string
print(dumpedfile)

# Deserialize the JSON-formatted string back to a Python object
with open ("fi4321.txt","r") as file:
    loadedfile=json.load(file)
    print(loadedfile)

